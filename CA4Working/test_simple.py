
import unittest

from simple import get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('Data.txt')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])
        self.assertEqual('2015-11-27', commits[0]['date'])
        self.assertEqual('16:57:44', commits[0]['time'])
        self.assertEqual('Fri', commits[0]['day'])      
        
    def test_last_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[421]['author'])
        self.assertEqual('r1491146', commits[421]['revision'])
        self.assertEqual('2015-07-13', commits[421]['date'])
        self.assertEqual('09:21:48', commits[421]['time'])
        self.assertEqual('Mon', commits[421]['day'])         

if __name__ == '__main__':
    unittest.main()
