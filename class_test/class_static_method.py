class CustomClass:

    # instance method
    def add_instance_method(self, a, b):
        print('add_instance_method, self: ' + str(self) + ', id(self): ' + str(id(self)))
        return a + b

    # classmethod
    @classmethod
    def add_class_method(cls, a, b):
        print('add_class_method, cls: ' + str(cls) + ', id(cls): ' + str(id(cls)))
        return a + b

    # staticmethod
    @staticmethod
    def add_static_method(a, b):
        print('add_static_method')
        return a + b


c = CustomClass()
print(CustomClass.add_instance_method(None, 3, 5))
print(CustomClass.add_instance_method(1, 3, 5))
print(c.add_instance_method(3, 5))
print(c.add_instance_method(3, 5))

print(CustomClass.add_class_method(3, 5))
print(c.add_class_method(3, 5))

print(CustomClass.add_static_method(3, 5))
print(c.add_static_method(3, 5))

r"""
add_instance_method, self: None, id(self): 140711530371200
8
add_instance_method, self: 1, id(self): 140711530600208
8
add_instance_method, self: <class_test.class_static_method.CustomClass object at 0x0000014F587DC970>, id(self): 1440298682736
8
add_instance_method, self: <class_test.class_static_method.CustomClass object at 0x0000014F587DC970>, id(self): 1440298682736
8
add_class_method, cls: <class 'class_test.class_static_method.CustomClass'>, id(cls): 1440300078848
8
add_class_method, cls: <class 'class_test.class_static_method.CustomClass'>, id(cls): 1440300078848
8
add_static_method
8
add_static_method
8
"""