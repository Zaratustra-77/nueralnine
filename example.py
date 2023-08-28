import unittest
from unittest import TestCase
class Car(TestCase):



    def setUp(self) -> None:
        print('running')

    def test_hello(self):
        print('Hello')
        assert 1 == 1


    def test_sup(self):
        print('sup')
        assert 1 == 1

    def tearDown(self) -> None:
        print('goodbye')

