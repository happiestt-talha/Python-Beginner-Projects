class customer:
    def __init__(self, a, b, c, d):
        kot = 'Welcome to State Bank of Pakistan'
        print(f"***   {kot:^20}   ***\n")
        self.name = a
        self.wealth = b
        self.acc = c
        self.Rank = d

    def get_data(self):
        self.name = input("Enter your name: ")
        self.wealth = int(input("Enter your wealth: "))
        self.acc = input("Enter your account number: ")
        self.Rank = int(input("Enter your rank: "))

    def show_profile(self):
        print("Name:", self.name)
        print("wealth:", self.wealth)
        print("Account Number:", self.acc)
        print("Your Current Rank:", self.Rank)


c1 = customer("Talha", 12, '4003815', 1)
# c1.get_data()
c1.show_profile()
