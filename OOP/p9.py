class Bank:
    def __init__(self, bal):
        print("Welcome To State Bank Of pakistan")
        self.__balance = bal

    def deposit(self, bal):
        self.__balance += bal

    def withdraw(self, bal):
        if self.bal <= self.__balance:
            self.__balance -= bal
        else:
            return 'Thora Maal ha'

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Your Balancr is {self.__balance:.2f}"
