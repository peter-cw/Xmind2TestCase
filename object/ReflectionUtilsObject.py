class ReflectionUtilsObject(object):

    @classmethod
    def get_cls_methods_public(cls):
        members = [attr for attr in dir(cls) if  callable(getattr(cls, attr)) and not attr.startswith("__")]
        # print(members)
        # for m in members:
        #     print(getattr(cls,m))
        # return members
        members_dict = dict()
        for m in members:
            members_dict[m] = getattr(cls,m)
            # print(getattr(cls,m))
        return members_dict

    @classmethod
    def get_cls_methods_private(cls):
        members = [attr for attr in dir(cls) if  callable(getattr(cls, attr)) and  attr.startswith("__") and  not attr.endsswith("__")]
        # print(members)
        for m in members:
            print(getattr(cls,m))
        return members



    @classmethod
    def get_cls_method_protected(cls):
        members = [attr for attr in dir(cls) if  callable(getattr(cls, attr)) and  attr.startswith("_") and  not attr.startsswith("__")]
        # print(members)
        for m in members:
            print(getattr(cls,m))
        return members


    @classmethod
    def get_cls_attr_public(cls):
        members = [attr for attr in dir(cls) if not callable(getattr(cls, attr)) and not attr.startswith("__")]
        # print(members)
        # for m in members:
        #     print(getattr(cls,m))
        members_dict = dict()
        for m in members:
            members_dict[m] = getattr(cls,m)
            # print(getattr(cls,m))
        return members_dict

    @classmethod
    def get_cls_attr_private(cls):
        members = [attr for attr in dir(cls) if  callable(getattr(cls, attr)) and  attr.startswith("__") and  not attr.endsswith("__")]
        # print(members)
        members_dict = dict()
        for m in members:
            members_dict[m] = getattr(cls,m)
            # print(getattr(cls,m))
        return members_dict



    @classmethod
    def get_cls_attr_protected(cls):
        members = [attr for attr in dir(cls) if not callable(getattr(cls, attr)) and  attr.startswith("_") and  not attr.startsswith("__")]
        # print(members)
        for m in members:
            print(getattr(cls,m))
        return members



    def get_ins_methods_public(self):
        members = [attr for attr in dir(self) if  callable(getattr(self, attr)) and not attr.startswith("__")]
        print(members)
        # for m in members:
        #     print(getattr(cls,m))
        # return members
        members_dict = dict()
        base_members = super().get_cls_methods_public()
        print('base_members:',base_members)
        cls_members = self.get_cls_methods_public()
        for m in members:
            if m in cls_members:
                break
            members_dict[m] = getattr(self,m)
            # print(getattr(cls,m))
        return members_dict


class Test(ReflectionUtilsObject):
    cls_attrs = '23333'

    @classmethod
    def cls_method(cls):
        print('this is a cls method')

    def ins_method(self):
        print('this is a instance method')

    def __init__(self):
        self.ins_attr = '6666'


# Test.get_cls_attr_public()
# Test.get_cls_methods_public()
t = Test()
t.get_ins_methods_public()



