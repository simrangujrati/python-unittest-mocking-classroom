from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class TestDbHelper(TestCase):
    def setUp(self):
        self.db = DbHelper()

    # def test_salary_without_mocking(self):
    #     dbhelper = DbHelper()
    #     actual = dbhelper.get_maximum_salary()
    #     self.assertEqual(6, actual)

    @patch('src.db_helper.DbHelper')
    def test_salary_with_mocking(self, Mockdbhelper):
        dbhelper = Mockdbhelper()  # create a mock object of Calculator class. This will help to customize output of class methods

       
        dbhelper.get_maximum_salary.return_value = 10000

        Max = dbhelper.get_maximum_salary()   # calling the sum method but the mocked version will actually get called

        
        dbhelper.get_minimum_salary.return_value = 7000

        Min = dbhelper.get_minimum_salary()

        self.assertGreater(Max, Min)







