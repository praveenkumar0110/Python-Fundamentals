class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   
    def deposit(self, amount):
        self.__balance += amount  

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"{self.name}'s balance: {self.__balance}")



pk = BankAccount("Praveen", 455)


pk.deposit(1000)
pk.check_balance()


# actually 3 OOPs concepts apply

# 1) Class and Object
# 2)Encapsulation (Data hiding)
# 3)Abstraction (Hide internal logic)


