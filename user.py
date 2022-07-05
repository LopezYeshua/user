class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"\nUser Info:")
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points -= amount
        if self.gold_card_points > 0:
            print(self.gold_card_points)
        else:
            print("Not enough")

u1 = User('Yeshua', 'Lopez', 'lopez@email.com', '22')
u2 = User('Not', 'Yeshua', 'yeshua.email.com', '22')

print(u1.first_name)
print(u2.first_name)
u1.display_info()
u2.enroll()
u1.enroll()
u1.spend_points(50)
u2.spend_points(80)
u1.display_info()
u2.display_info()
u1.enroll()
u1.spend_points(150)
