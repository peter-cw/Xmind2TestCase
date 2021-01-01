from object.ReflectionUtilsObject import ReflectionUtilsObject
class VersionInfo():
    title_ar_no = '关联需求编号'
    title_project_info = '项目信息'
    title_desigher = '设计人员'
    title_state = '状态'

class CaseType(ReflectionUtilsObject):
    title_func = '功能测试'
    title_security = '安全测试'
    title_performance = '性能测试'
    title_compatibility = '兼容性测试'

    def test(cls):
        print('测试方法')


print(CaseType.get_cls_attr_public())
print(CaseType.get_cls_methods_public())
