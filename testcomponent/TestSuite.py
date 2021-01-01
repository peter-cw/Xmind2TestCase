from .TestComponent import TestComponent

class TestSuite(TestComponent):
    def __init__(self,name='', details='', testcase_list=None, sub_suites=None, statistics=None):
        self.name = name
        self.test_comp_list = []

    def to_dict(self):
        print()