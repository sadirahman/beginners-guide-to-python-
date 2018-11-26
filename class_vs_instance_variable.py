class Girl():
    gender = 'male'
    def __init__(self, name):
        self.name=name

s = Girl('sadi')
r = Girl('sq')

# class variable
print(r.gender)
print(s.gender)

# instance variable
print(r.name)
print(s.name)


