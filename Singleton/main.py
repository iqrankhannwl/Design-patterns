from ex_01 import Logger
from ex_02 import Logger2
from ex_03 import Singleton
from ex_04 import SingletonBase


#*=================== Example 01 ===========================*#
log1 = Logger.instance()
log2 = Logger.instance()
print(log1, log2)
print(log2 is log1)

#*=================== Example 02 ===========================*#
log1 = Logger2()
log2 = Logger2()
print(log1, log2)
print(log2 is log1)

#*=================== Example 03 ===========================*#
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)

#*=================== Example 03 ===========================*#
class SingletonChild(SingletonBase):
    ...

signleton = SingletonBase()
child = SingletonChild()

print(child is signleton)
signleton.name = "Base class"
print(child.name)