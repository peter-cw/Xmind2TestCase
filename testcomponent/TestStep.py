from .TestComponent import TestComponent
class TestStep(TestComponent):
    def __init__(self,step_num=1,step_action='',expected_result=''):
        self.step_num =step_num
        self.step_action = step_action
        self.expected_result = expected_result

    def to_dict(self):
        print('这是测试步骤')