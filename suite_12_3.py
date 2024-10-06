import unittest
import tests_12_3

mdl12 = unittest.TestSuite()
mdl12.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
mdl12.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(mdl12)
