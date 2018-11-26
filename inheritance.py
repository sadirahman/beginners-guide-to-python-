class Parent():

    def print_last_name(self):
        print('rahman')

class Child():

    def print_first_name(self):
        print('sadi')

# Multiple inheritance
class Grandchild(Parent,Child):
    def print_nick_name(self):
        print('Gutu')

sadi = Grandchild()
sadi.print_first_name()
sadi.print_last_name()
sadi.print_nick_name()

sq = Child()
sq.print_first_name()