from unittest import TestCase
from player import Player
from devtools import DevTools
from referee import Referee
from manager import Manager
from player_interface import TournamentUpdateType

class TestManager(TestCase):

	# An overridden Manager for testing purposes. Lets use control the size of the board so we can test
	# certain scenarios.
	class ManagerFake(Manager):
		def __init__(self, players, rows, cols):
			super().__init__(players=players)
			self.rows = rows
			self.cols = cols

		# Overwritten createGames class that allows for custom board sizes
		def createGames(self, playerGroupings):
			for grouping in playerGroupings:
				self.currentRoundReferees.append(Referee(grouping, self.rows, self.cols, self.default_num_fish, randomSeed=self.seed))
			self.results.append([])

	# Overwritten Player for testing purposes. Will never respond in time to notifications from the Manager.
	class slowPlayer(Player):
		def notifyTournamentUpdate(self, msg):
			a = 1
			while(True):
				a +=1
			return msg


	def setUp(self) -> None:
		self.playerA0 = Player(1, "adam")
		self.playerA1 = Player(2, "bart")
		self.playerA2 = Player(5, "3293421")
		self.playerA3 = Player(3, "#@*$#")
		self.playerA4 = Player(6, "#*$#")
		self.playerA5 = Player(16, "@d@m")
		self.playerA6 = Player(16, "A6")
		self.playerA7 = Player(1, "Cal")
		self.playerA0Slow = self.slowPlayer(1, "adam")
		self.playerA1slow = self.slowPlayer(1, "Cal")

		self.playerListA = [self.playerA0, self.playerA1, self.playerA2, self.playerA3, self.playerA4, self.playerA5, self.playerA6, self.playerA7]
		self.playerListB = [self.playerA0, self.playerA1, self.playerA2, self.playerA3, self.playerA4]
		self.playerListC = [self.playerA7, self.playerA4, self.playerA1, self.playerA5, self.playerA0, self.playerA3]
		self.playerListD = [self.playerA0, self.playerA1, self.playerA2, self.playerA3]
		self.playerListE = [self.playerA0, self.playerA1, self.playerA2]
		self.playerListESlow = [self.playerA0, self.playerA1slow, self.playerA2]
		self.playerListDSlow = [self.playerA0Slow, self.playerA1, self.playerA2, self.playerA3]

		self.managerA = Manager(self.playerListA)
		self.managerB = Manager(self.playerListB)
		self.managerC = Manager(self.playerListC)
		self.managerD = Manager(self.playerListD)
		self.managerDSlow = Manager(self.playerListDSlow)
		self.fakeManager = self.ManagerFake(self.playerListE, 3, 3)
		self.fakeManagerSlow = self.ManagerFake(self.playerListESlow, 3, 3)
		self.fakeManager2 = self.ManagerFake(self.playerListA, 3, 3)
		self.managerBigTournament = None

	# Sets up a tournament of 32 players
	def setUpBigTournament(self):
		plist = []
		for n in range(32):
			cur_name = "Player " + str(n)
			plist.append(Player(n, cur_name))
		self.managerBigTournament = Manager(plist)

	# Runs a large tournament. Mainly to see how performance is.
	def test_big_tournament(self):
		self.setUpBigTournament()
		self.managerBigTournament.runTournament()
		results1 = self.managerBigTournament.results[-1]
		self.managerBigTournament.runTournament()
		results2 = self.managerBigTournament.results[-1]
		self.assertEqual(results1, results2)

	def test_inform_players_of_start(self):
		acks = self.managerA.informPlayersOfStart()
		tournamentStartMessage = {'type': TournamentUpdateType.TournamentStart, 'body': 'Tournament Starting'}
		expected_acks = {}
		for player in self.managerA.players:
			expected_acks[player.id] = tournamentStartMessage
		self.assertEqual( expected_acks, acks)


	def test_inform_player_round_results(self):
		self.managerA.runRound()
		win_acks, lose_acks = self.managerA.informPlayerRoundResults()
		print(win_acks,"\n", lose_acks)
		advancingMessage = {'type': TournamentUpdateType.RoundWin, 'body': 'You are advancing to the next round'}
		nonAdvancingMessage = {'type': TournamentUpdateType.RoundLoss, 'body': 'You have been eliminated'}
		expected_win_acks = {}
		expected_lose_acks = {}
		# expected_acks = {}
		for player in self.managerA.queryResults(Manager.WINNERS):
			expected_win_acks[player]= advancingMessage
		for player in self.managerA.queryResults(Manager.LOSERS):
			expected_lose_acks[player]= nonAdvancingMessage
		self.assertEqual( expected_win_acks, win_acks)
		self.assertEqual( expected_lose_acks, lose_acks)

	def test_inform_players_of_end(self):
		self.fakeManager.seed = 1
		self.fakeManager.runTournament()
		self.fakeManager.informPlayersOfEnd()
		self.assertEqual(self.playerListE, self.fakeManager.TournamentWinners)

	# Tournament with a player who fails to acknowledge victory
	def test_inform_players_of_end_player_too_slow(self):
		self.fakeManagerSlow.seed = 1
		# self.fakeManagerSlow.runTournament()
		self.fakeManagerSlow.informPlayersOfEnd()
		self.assertEqual([self.playerA0, self.playerA2], self.fakeManagerSlow.TournamentWinners)

	# Tournament with one winner who doesn't acknowledge victory
	def test_inform_players_of_end_no_winner_response(self):
		self.managerDSlow.seed = 1
		self.assertEqual([], self.managerDSlow.runTournament())

		# Reference where player does respond
		self.managerD.seed = 1
		self.assertEqual([self.playerA0], self.managerD.runTournament())

	# 8 Players should go 4-4
	def test_allocate_players_no_backtrack(self):
		self.assertCountEqual(self.managerA.allocatePlayers(self.playerListA),
							  [[self.playerA0, self.playerA1, self.playerA3, self.playerA2],
							   [self.playerA7, self.playerA4, self.playerA5, self.playerA6]])

	# 6 Players should go 4-2
	def test_allocate_players_simple_backtrack(self):
		self.assertCountEqual(self.managerC.allocatePlayers(self.playerListC),
							  [[self.playerA7, self.playerA1, self.playerA4, self.playerA5],
							   [self.playerA0, self.playerA3]])

	# 5 Players should go 3-2
	def test_allocate_players_complex_backtrack(self):
		self.assertCountEqual(self.managerB.allocatePlayers(self.playerListB),
							  [[self.playerA0, self.playerA1, self.playerA3],
							   [self.playerA2, self.playerA4]])

	def test_create_games(self):
		groupings = self.managerA.allocatePlayers(self.playerListA)
		self.managerA.createGames(groupings)
		self.assertEqual(len(self.managerA.currentRoundReferees), 2)

	def test_create_random_games(self):
		groupings = self.managerA.allocatePlayers(self.playerListA)
		self.managerA.seed = 1
		self.managerA.createGames(groupings)
		refs = self.managerA.currentRoundReferees
		board = [[4, 0, 2, 0], [3, 3, 3, 5], [3, 1, 0, 3], [0, 3, 3, 4]]
		#DevTools.visualizeState(refs[0].state)
		self.assertCountEqual(DevTools.tileToIntArray(refs[0].state.board.tiles), board)
		self.assertCountEqual(DevTools.tileToIntArray(refs[1].state.board.tiles), board)

	# Tests that a game of 3 (9 penguins) on a 9 tile board leads to a stalemate with 3 winners
	def test_check_tournament_over_same_winners(self):
		self.fakeManager.seed = 1
		self.fakeManager.runTournament()
		self.assertEqual(self.fakeManager.results[-1][0]["winners"], ['adam', 'bart', '3293421'])

	# Tests that a game of 4 and a game of 2 players both lead to a stalemate that leads to
	# all 6 becoming winners
	def test_check_tournament_over_same_winners_multiple_games(self):
		fakeM = self.ManagerFake(self.playerListC, 2, 4)
		fakeM.runTournament()
		game1winners = fakeM.results[-1][0]["winners"]
		game2winners = fakeM.results[-1][1]["winners"]
		self.assertEqual(len(game1winners), 4)
		self.assertEqual(len(game2winners), 2)

	def test_check_is_tournament_over_final_game(self):
		self.managerD.initializeRound()
		self.assertTrue(self.managerD.checkIsTournamentOver())

	def test_check_is_tournament_over_decisive_winner(self):
		self.managerD.seed = 1
		self.managerD.createGames(self.managerD.allocatePlayers(self.managerD.getAdvancingPlayers()))
		for ref in self.managerD.currentRoundReferees:
			self.managerD.results[-1].append(ref.play())
		self.assertTrue(self.managerD.checkIsTournamentOver())
		self.assertEqual(len(self.managerD.results[-1]), 1)
		self.assertEqual(["adam"], self.managerD.queryResults("winners"))

	def test_run_tournament(self):
		groupings = self.fakeManager2.allocatePlayers(self.playerListA)
		self.assertFalse(self.fakeManager2.checkIsTournamentOver())
		self.fakeManager2.seed = 1094
		self.fakeManager2.runTournament()
		self.assertTrue(self.fakeManager2.checkIsTournamentOver())
		final_results = self.fakeManager2.results[-1]
		self.assertEqual(self.fakeManager2.results[-1][0]["winners"][0], "adam")

	# Running a tournament twice should return the same winners if no randomization
	def test_run(self):
		self.managerA.runTournament()
		results1 = self.managerA.results[-1]
		self.managerA.runTournament()
		results2 = self.managerA.results[-1]
		self.assertEqual(results1, results2)
