 #Write a class Movie with attributes title and rating using the __init__() constructor.
#Define a method to display the movie’s title and rating.
class Movie:
    title = "err"
    def __init__(self,title,rating):
        self.title=title
        self.rating = rating

    def display_movie(self):
        print(f"{self.title},{self.rating}")

    def hit_movie(self):
        if self.rating>=100:
            print("hit")
        else:
            print("not hit")
    def update_method(self,new_rarin):
        self.rating =new_rarin

a = Movie("e",78)
print(a.title)
a.display_movie()
a.rating =100
a.display_movie()
a.update_method(77)
a.display_movie()
a.hit_movie()
print(Movie.title)




#Create a BankAccount class with private attributes for account_number and balance.
#Add methods to check balance, deposit, and withdraw funds.
#Try accessing the balance directly and observe the result.

class Bankaccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance

    def check_balance(self):
        print(self.__balance)

    def deposit(self,amount):
        self.__balance+= amount

    def withdraw(self,amount):
        self.__balance-= amount


user = Bankaccount(1222,90)
user.check_balance()
user.deposit(100)
user.check_balance()
user.withdraw(200)
user.check_balance()