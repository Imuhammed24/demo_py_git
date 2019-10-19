class ParentClass:
    var1 ="i am var1"
    var2 ="i am var2"

parentObject=ParentClass()


class ChildClass(ParentClass):
    pass

childObject=ChildClass()
print(childObject.var1)
