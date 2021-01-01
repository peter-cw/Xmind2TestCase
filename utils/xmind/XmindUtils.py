import xmind
from xmind.core.sheet import SheetElement
import os
import logging
logger = logging.getLogger('XmindUtils')
console = logging.StreamHandler()
console.setLevel(level=logging.DEBUG)

logger.addHandler(console)
logger.setLevel(level=logging.DEBUG)
# logger.setLevel(level='DEBUG')
class XmindUtils(object):

    def __init__(self,file):
        self.path = self.get_absolute_path(file)
        self.workwork = xmind.load(self.path)
        self.sheet_list = self.workwork.getSheets()
        self.current_sheet = self.workwork.getPrimarySheet()

    @staticmethod
    def get_absolute_path(file:str):
        '''

        :param file:xmind文件名
        :return:
        '''
        filename,suffix = os.path.splitext(file)
        # print(suffix)
        logger.debug(msg=suffix)
        if not suffix == '.xmind':
            return ValueError('{} is not a xmind file'.format(file))

        current_path = os.path.abspath(__file__)
        root_path = os.path.abspath(os.path.join(current_path,'../../..'))
        # print(root_path)
        xmind_path = root_path+os.sep+'xmind_dir'
        abs_path = xmind_path+os.sep+file
        return abs_path

    def get_data(self,sheet:SheetElement):
        # xmind_file = self.get_absolute_path(file)
        # workbook = xmind.load(xmind_file)
        # print(workbook.getSheets())
        # print(workbook.getWorkbookElement())
        # print(workbook.getSheets()[0].getLocalName())
        # print(workbook.getPrimarySheet().__str__())
        pass

    def get_sheet_by_index(self,index):
        if self.check_sheet_index(index):
            self.sheet_list[index]
        return False

    def set_current_sheet(self,sheet_index:int):
        if self.check_sheet_index(sheet_index):
            self.current_sheet = self.sheet_list[sheet_index]
        return False


    def check_sheet_index(self,index):
        if not isinstance(index,int):
            logger.info(msg='index must be a int ')
            # raise TypeError('index must be a int ')
            return False
        if not index in range(len(self.sheet_list)):
            logger.info(msg='index out of boundry')
            # raise TypeError('index must be a int ')
            return False
            # raise IndexError('index out of boundry')


    def get_current_sheet(self):
        return self.current_sheet

    def custom_parse_xmind(workbook):
        elements = {}

        def _echo(tag, element, indent=0):
            title = element.getTitle()
            elements[element.getID()] = title
            print('\t' * indent, tag, ':', pipes.quote(title))

        def dump_sheet(sheet):
            root_topic = sheet.getRootTopic()
            _echo('RootTopic', root_topic, 1)

            for topic in root_topic.getSubTopics() or []:
                _echo('AttachedSubTopic', topic, 2)

            for topic in root_topic.getSubTopics(xmind.core.const.TOPIC_DETACHED) or []:
                _echo('DetachedSubtopic', topic, 2)

            for rel in sheet.getRelationships():
                id1, id2 = rel.getEnd1ID(), rel.getEnd2ID()
                print('Relationship: [%s] --> [%s]' % (elements.get(id1), elements.get(id2)))

        for sheet in workbook.getSheets():
            _echo('Sheet', sheet)
            dump_sheet(sheet)

xmind_obj = XmindUtils('百度官网.xmind')
# abs_path = xmind_obj.get_absolute_path('百度官网.xmind')
# xmind_obj.get_data(abs_path)
# xmind_obj.check_sheet_index('l')
current_sheet = xmind_obj.get_current_sheet()
root_topic = current_sheet.getRootTopic()
print(root_topic.getTitle())
# workbook = xmind.load(r'C:/Users/mayn/PycharmProjects/XMind2TestCase/xmind_dir/百度官网.xmind')

# sheets = workbook.getSheets()
# print(len(sheets))
# print(sheets[0].getRootTopic().getTextContent())
# data = workbook.getData()
# print(data)


# print(XmindUtils().get_absolute_path('test.xmind'))
# print(os.path.splitext('test.xmind'))
test_suite_root = root_topic.getTitle()
sub_topics = root_topic.getTopics()
st_dict = dict()
for st in sub_topics:
    st_dict[st.getTitle()] = st
from constant.constant import *
for t in st_dict.keys():
    if t in CaseType.get_cls_attr_public().values():
        pass

from testcomponent.TestSuite import TestSuite
from testcomponent.TestCase import TestCase
from testcomponent.TestStep import TestStep






