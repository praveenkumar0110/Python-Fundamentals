class account:
    def __init__(self,balance):
      self. __balance = balance

    def deposit(self,amout):
      self. __balance += amout

    def getbalance(self):
      return self. __balance
    
a = account(2000)
a.deposit(9000)

print(a.getbalance())  



# tips:
# __ double underscore like private class