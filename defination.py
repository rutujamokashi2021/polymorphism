#polymophims -- having may forms
#means functon with same name having differnt signatures or being used for different types
#len()
print(len("rutuja"))
print(len([18, 12, 13]))
print(len({'one : hello', 'two : world'}))


# polymorphism with operator
num1 = 1
num2 = 2
print(num1 + num2)
str1 = 'hello'
str2 = 'world'
print(str1 + str2)

# user-defined function


#polymorphism with class method
class India():
    def capital(self):
        print("new delhi")

    def lang(self):
        print("hindi")

    def type(self):
        print("developeing")


class USA():
    def capital(self):
        print("washington")

    def lang(self):
        print("english")

    def type(self):
        print("developed")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.lang()
    country.type()

