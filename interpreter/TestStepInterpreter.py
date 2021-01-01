from .BaseInterpreter import BaseInterpreter
from testcomponent.TestComponent import TestComponent

class TestStepInterpreter(BaseInterpreter):
    __next_interpreter = None

    def __init__(self,component:TestComponent):
         self.component = component

    def set_next_interpreter(self,interpreter:BaseInterpreter):
        self.__next_interpreter = interpreter




    def handle(self,component):
        if self.component.has_next():

            pass
        else:
            #最后一个步骤为测试用例标题
            self.__next_interpreter.handle(component)
