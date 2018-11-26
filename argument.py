#defalt value argument

print('gender is :')
def get_gender(sex='Other'):
    if sex is 'm':
        sex='male'
    elif sex is 'f':
        sex='female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()

# key argument

def full_sentence(name='sadi',action ='ate',item='burger'):
    print(name,action,item)

full_sentence()
full_sentence('sakil','eat','rich')
full_sentence(item='fucha')
full_sentence(action='eat')

#flexible number argument

def add_number(*args):
    total=0
    for a in args:
        total +=a
    print(total)

add_number(3)
add_number(23, 5)

#unpacking argument

def helth_calculator(age, apples_ate, cigs_smoked):
    anwer = (100-age)+(apples_ate*3.5)-(cigs_smoked*2)
    print(anwer)

sadi_data=[23, 20 ,0]
helth_calculator(sadi_data[0], sadi_data[1], sadi_data[2])
helth_calculator(*sadi_data)

#Dictionary

classmates = {'sadi':'B.sc engineering','raad':'master'}
print(classmates['sadi'])

for v, k in classmates.items():
    print(v,':', k);