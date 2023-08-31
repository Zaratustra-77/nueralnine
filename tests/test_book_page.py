import unittest
from utils.driver_setup import DriverSetUp
from src.common.actions import Actions
from src.pages.book_page import Book_page


class TestBP(DriverSetUp):
    URL = 'https://www.neuralnine.com'

    def setUp(self) -> None:
        super().setUp()
        self.driver.get(self.URL)
        self.b00k_page = Book_page(self.driver)
        self.Actions = Actions(self.driver)

    def tes_1(self):
        assert 1==1