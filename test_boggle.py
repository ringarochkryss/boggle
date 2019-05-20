import unittest
import boggle
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
    """our test suite for boggle solver
    """
    
    def test_can_create_an_empty_grid(self):
            """test to see if we can create an empty grid
            """
            grid = boggle.make_grid(0, 0)
            self.assertEqual(len(grid), 0)
    
    def test_grid_size_is_width_times_height(self):
        """test is to ensure that the total size of the grid
        is equal to widht * height
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        
    def test_grid_coordinates(self):
        """Test to ensure that all the coordinates
        inside of the grid can be accessed
        """
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)
        
    def test_grid_is_filled_with_letters(self):
        """ensure that each the coordinates in the grid
        contains letters
        """
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
    
    def test_neighbours_of_a_position(self):
        """ensure that a position has 8 neighbours
        """
        coords = (1, 2)
        neighbours = boggle.neighbours_of_a_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
    
    #Here comes a complicated test that gives us comfidence 
    #our neigbours datastructure is correct
    
    def test_all_grid_neighbours(self):
        """ensure that alla of the grid positions have neighbours
        """
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbours), len(grid))
        for pos in grid:
            others = list(grid) #creates a new list from the dictionary's keys
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
            
    #Let's write a test to turn a path of positions into
    #words of letters -here's the test:
    def test_converting_a_path_to_a_word(self):
        """ensure that paths can be converted to words
            our test checks that path to world function returns the
            same string we manually construct in the test
        """
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
    
    #to find a word in the grid
    def test_search_grid_for_word(self):
        """
        ensure that certain patterns can be found i a path_to_word
        """
        grid={(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = 'EEE'
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]
        
        foundWords = boggle.search(grid, dictionary)
        
        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)
    
    def test_load_dictionary(self):
        """Test that the get_dictionary function returns a dictionary
        that has a lenght greater than 0
        you can find serveral dictionaries on the internet, here we use:
        bogwords.txt google it and paste in a own txt-file named words.
        """
        
        dictionary = boggle.get_dictionary('words.txt')
        self. assertGreater(len(dictionary), 0)