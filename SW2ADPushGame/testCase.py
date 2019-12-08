import unittest
from Tile import *
import numpy as np

class Test_tile(unittest.TestCase):

    def setUp(self):
        self.m1 = Tiles()
        self.m2 = Tiles()

    def tearDown(self):
        pass

    def test_Normal(self):
        t1 = np.array([
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,0,0,0,0,0,0,-1],
            [-1,0,4,4,0,0,0,-1],
            [-1,0,4,4,3,0,0,-1],
            [-1,0,0,0,3,0,0,-1],
            [-1,0,0,0,1,0,0,-1],
            [-1,0,0,0,0,0,0,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1]
            ])
        self.m1.move(1,0)
        self.assertEqual(self.m1.display(),str(t1))

if __name__ == '__main__':
    unittest.main()
