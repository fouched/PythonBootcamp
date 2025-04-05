class User:

    def __init__(self, userid: str, username: str):
        self.userid = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1




user_1 = User("001", "Fouche")
user_2 = User("002", "Olivia")

user_1.follow(user_2)

print("user 1")
print("followers:", user_1.followers)
print("following:",user_1.following)
print("user 2")
print("followers:", user_2.followers)
print("following:",user_2.following)



