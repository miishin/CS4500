import unittest
import referee


class MyTestCase(unittest.TestCase):

    # Set up function
    # Make a new referee for every test
    def setUp(self):
        self.ref = referee.Referee(3, 4, 3, [1, 2, 3])

    # tests setup phase of our referee
    # once done all penguins should be placed
    def test_setup(self):
        self.ref.run_setup()
        self.assertEqual(self.ref.phase, referee.Phases.GAMEPLAY)
        penguins = self.ref.state.occupied_tiles()
        self.assertCountEqual(penguins, [(0, 0), (2, 0), (4, 0), (6, 0), (1, 1), (3, 1), (5, 1), (7, 1), (0, 2)])

    def test_gameplay(self):
        self.ref.run_setup()
        self.ref.run_gameplay()
        self.assertEqual(self.ref.phase, referee.Phases.GAME_OVER)
        penguins = self.ref.state.occupied_tiles
        self.assertCountEqual(penguins, [(0, 0), (2, 0), (4, 0), (6, 0), (2, 2), (4, 2), (6, 2), (7, 1), (0, 2)])

if __name__ == '__main__':
    unittest.main()
