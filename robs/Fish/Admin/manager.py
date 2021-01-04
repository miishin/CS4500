from player import Player
from manager_interface import Manager_Interface
from referee import Referee
from player_interface import TournamentUpdateType
from referee import try_fn_with_timeout

# Wait 3 seconds for players to acknowledge messages
RESPONSE_TIMEOUT_LIMIT = 3


class Manager(Manager_Interface):
	"""
	A Tournament of Fish is run by a Tournament Manager. A Manager is handed a list of Players and
	will group these players into games, creating Referees to run each game. Games are run in rounds,
	with the winners of each round moving onto the next. Players are allocated to games by groups of 4,
	the maximum size of a game, and if the last game has only 1 person, then the last two games are
	split into 3-2.

	A tournament ends under three conditions:
	- There are 0 or 1 players left, in which case there is no winner or one winner.
	- There are 2-4 players left, in which case a final game is run, and the winners of that game are the winners overall
	- Running two rounds in a row returns the same winners (denoting some kind of stalemate going on). In this case
	all those players win.
	"""
	WINNERS = "winners"
	LOSERS = "losers"
	CHEATERS = "cheaters"
	TYPE = "type"
	BODY = "body"
	default_row_size = 4
	default_column_size = 4
	default_num_fish = 1

	def __init__(self, players):
		"""
		A tournament manager runs a game tournament until completion
		:param players: A list of Player objects representing all the players that signed up for a tournament
		"""
		self.players = players
		self.player_mapping = {}
		for player in players:
			self.player_mapping[player.id] = player
		self.results = []
		self.currentRoundReferees =[]
		self.seed = None

	def informPlayersOfStart(self):
		"""
		Informs all participating players that the tournament has begun
		:return: A list of the responses from each player
		"""
		message = {self.TYPE: TournamentUpdateType.TournamentStart, self.BODY: "Tournament Starting"}
		return self.notifyPlayers(self.players, message)

	def informPlayerRoundResults(self):
		"""
		Informs players of whether they are advancing to the next round or if they have been eliminated
		:return: The responses from both the winners and losers of the round
		"""
		winners = self.getAdvancingPlayers()
		winners_message = {self.TYPE: TournamentUpdateType.RoundWin, self.BODY: "You are advancing to the next round"}
		winner_acks = self.notifyPlayers(winners, winners_message)

		losers = self.getNonAdvancingPlayers()
		losers_message = {self.TYPE: TournamentUpdateType.RoundLoss, self.BODY: "You have been eliminated"}
		loser_acks = self.notifyPlayers(losers, losers_message)

		return (winner_acks, loser_acks)

	def informPlayersOfEnd(self):
		"""
		Informs the players remaining at the end of the tournament if they won or lost
		Winners that do not accept their win message become losers
		:return: Both the responses from the winners and the losers
		"""
		self.TournamentWinners = []
		winners = self.getAdvancingPlayers()
		winners_message = {self.TYPE: TournamentUpdateType.TournamentWin, self.BODY: "You have won the tournament"}
		winner_acks = self.notifyPlayers(winners, winners_message)

		for winner in self.getAdvancingPlayers():
			if winner_acks[winner.id]:
				self.TournamentWinners.append(winner)

		losers = self.getNonAdvancingPlayers()
		losers_message = {self.TYPE: TournamentUpdateType.RoundLoss, self.BODY: "You have been eliminated"}
		loser_acks = self.notifyPlayers(losers, losers_message)
		return (winner_acks, loser_acks)

	def notifyPlayers(self, players, message):
		"""
		Sends a message to each player in a list of players
		:param players:
		:param message: TournamentUpdate
		:return: The responses from the players notified
		"""
		responses = {}
		for player in players:
			response = try_fn_with_timeout(player.notifyTournamentUpdate, RESPONSE_TIMEOUT_LIMIT, message)
			responses[player.id] = response
		return responses

	def getAdvancingPlayers(self):
		"""
		Retreives all players advancing to next round (last round's winners)
		:return: List of Player
		"""
		if not self.results:
			return self.players
		return [self.player_mapping[id] for id in self.queryResults(self.WINNERS)]

	def getNonAdvancingPlayers(self):
		"""
		Retreives players who were eliminated in the most recently run round
		:return: List of player
		"""
		if not self.results:
			return []
		return [self.player_mapping[id] for id in self.queryResults(self.LOSERS) + self.queryResults(self.CHEATERS)]

	def queryResults(self, key, round_number=-1):
		"""
		Gets the results for the requested round number. Gets either winners, losers, or cheater according to the given key
		:param key: one of winner, loser, or cheater to get the results for
		:param round_number: the round number to get the results of
		:return: The requested results of the requested round as a list of player id
		"""
		next_players = []
		round_results = self.results[round_number]
		for result in round_results:
			next_players += result[key]
		return next_players

	def allocatePlayers(self, players):
		"""
		Allocates the given players to groups that will play against each other in a game
		:return: List of List of Players
		"""
		player_groupings = []
		maximal_num_players = 4
		for idx in range(len(players)):
			if idx % maximal_num_players == 0:
				player_groupings.append([])
			player_groupings[-1].append(players[idx])
			player_groupings[-1].sort(key=Manager._sort_player_key)
		if len(player_groupings[-1]) == 1: # Check the backtrace case where there is a game of 1 player, split into 3 - 2
			player_groupings[-1].append(player_groupings[-2].pop(3))
			player_groupings[-1].sort(key=Manager._sort_player_key)
		# print(player_groupings)
		return player_groupings

	# Method for sorting a list of players
	@staticmethod
	def _sort_player_key(player):
		return player.age

	def createGames(self, playerGroupings):
		"""
		Creates referees from the groupings of players provided
		:param playerGroupings: List of List of Players defining which players are in a game together
		:return: None. Updates list of current referees
		"""
		for grouping in playerGroupings:
			self.currentRoundReferees.append(Referee(grouping, self.default_row_size, self.default_column_size, self.default_num_fish, randomSeed=self.seed))
		self.results.append([])

	def initializeRound(self):
		"""
		Initializes the current round of games (creates the referees)
		:return: None. Updates list of current referees
		"""
		self.createGames(self.allocatePlayers(self.getAdvancingPlayers()))

	def checkIsTournamentOver(self):
		"""
		A tournament end under the following conditions
			- Two consecutive rounds produce the exact same winners
			- There are only enough players to play one final game (which is played)
			- There are 0 or 1 players remaining
		:return: Boolean whether the tournament has ended
		"""
		current_players = self.getAdvancingPlayers()
		if len(current_players) <= 1:
			return True
		elif len(current_players) <= 4:
			self.runRound()
			return True
		elif len(self.results) > 1 and set(self.queryResults(self.WINNERS, -2)) == set(self.queryResults(self.WINNERS, -1)):
			return True
		else:
			return False

	def runRound(self):
		"""
		Runs the current round of games
		:return: None, mutates self.results
		"""
		self.initializeRound()
		for ref in self.currentRoundReferees:
			self.results[-1].append(ref.play()) #TODO maybe check if this has to be simultaneous (that prob is impossible)
		self.informPlayerRoundResults()
		self.currentRoundReferees = []

	def runTournament(self):
		"""
		Informs players of tournament start, runs the tournament, then sends out results.
		:return: A list of Player, the list of winners of the entire tournament
		"""
		self.informPlayersOfStart()

		while not self.checkIsTournamentOver():
			self.runRound()

		self.informPlayersOfEnd()
		return self.TournamentWinners








