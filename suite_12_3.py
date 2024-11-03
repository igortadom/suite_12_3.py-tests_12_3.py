import tests_12_2
import unittest
import module_12_1
import tests_12_3





rttestST = unittest.TestSuite()
rttestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
rttestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rttestST)

