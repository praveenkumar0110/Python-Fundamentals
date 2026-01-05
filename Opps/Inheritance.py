class parent:
    def display(self):
        print("i'm a parent")
    
class child(parent):
    def show(self):
         print("i'm a child")


c= child();
c.display();
c.show()


# type of inheritance like-------------:

# 1) single inher ----one parent
# 2) muliple inher --- more then one parent
# 3) multi level inher---grand parent like chain
# 4) hierarchical inher --- tree structure