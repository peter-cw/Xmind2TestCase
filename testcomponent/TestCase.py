from .TestComponent import TestComponent
class TestCase(TestComponent):
    def __init__(self,name,result,step_list,execution_type=1, importance=2):
        """
        TestCase
        :param name: test case name
        :param version: test case version infomation
        :param summary: test case summary infomation
        :param preconditions: test case pre condition
        :param execution_type: manual:1 or automate:2
        :param importance: high:1, middle:2, low:3
        :param estimated_exec_duration: estimated execution duration
        :param status: draft:1, ready ro review:2, review in progress:3, rework:4, obsolete:5, future:6, final:7
        :param result: non-execution:0, pass:1, failed:2, blocked:3, skipped:4
        :param steps: test case step list
        """
        self.name = name
        self.result = result
        self.step_list = step_list
        self.execution_type = execution_type
        self.importance = importance

    def to_dict(self):
        print('这是测试用例')
        data = {
        'name':self.name ,
        'result':self.result ,
        'step_list':self.step_list,
        'execution_type':self.execution_type,
        'importance':self.importance
        }

        return data