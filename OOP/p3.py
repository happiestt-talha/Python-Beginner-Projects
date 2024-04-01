class customer:
    def __init__(self):
        kot = 'Welcome to State Bank of Pakistan'
        print(f"***   {kot:^20}   ***")
        self.name = "Unknown"
        self.wealth = 0
        self.acc = "N/A"
        self.Rank = 0

    def get_data(self):
        self.name = input("Enter your name: ")
        self.wealth = int(input("Enter your wealth: "))
        self.acc = input("Enter your account number: ")
        self.Rank = int(input("Enter your rank: "))

    def show_profile(self):
        print(self.name)
        print(self.wealth)
        print(self.acc)
        print(self.Rank)


c1 = customer()
c1.get_data()
c1.show_profile()
