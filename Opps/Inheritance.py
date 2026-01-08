# type of inheritance like-------------:
# 1) single inher ----one parent
class parent:
    def display(self):
        print("i'm a parent")
    
class child(parent):
    def show(self):
         print("i'm a child")


c= child();
c.display();
c.show()




# 2) muliple inher --- more then one parent
class Father:
    def father(self):
        print("Father class")

class Mother:
    def mother(self):
        print("Mother class")

class Child(Father, Mother):
    def child(self):
        print("Child class")

c = Child()
c.father()
c.mother()
c.child()

# 3) multi level inher---grand parent like chain
class GrandParent:
    def gp(self):
        print("Grand Parent")

class Parent(GrandParent):
    def p(self):
        print("Parent")

class Child(Parent):
    def c(self):
        print("Child")

c = Child()
c.gp()
c.p()
c.c()

# 4) hierarchical inher --- tree structure
class Parent:
    def show(self):
        print("Parent class")

class Child1(Parent):
    def c1(self):
        print("Child 1")

class Child2(Parent):
    def c2(self):
        print("Child 2")

c1 = Child1()
c2 = Child2()

c1.show()
c1.c1()

c2.show()
c2.c2()
