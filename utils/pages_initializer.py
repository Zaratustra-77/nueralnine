from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.home_page import Home_page
from src.pages.book_page import Book_page
from src.common.actions import Actions

def initialize_pages(driver):
    pages = {
        'home_page': Home_page(driver),
        'book_page': Book_page(driver),
        'Actions': Actions(driver),
    }
    return pages