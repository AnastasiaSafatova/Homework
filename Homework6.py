print("Решение первого задания")
my_dict={'Anastasia':1995,'Alex':1994,'Georg':1993}
print(my_dict)
print(my_dict['Anastasia'])
my_dict['Pavel']=1990
print(my_dict['Pavel'])
my_dict.update({'Veronica':1992,
                'Maria':1996})
print(my_dict)
my_dict.pop('Alex')
print(my_dict.get('Alex'))
my_dict['Alex']=1994
a=my_dict.pop('Alex')
print(a)
print(my_dict)


print("Решение второго задания")
my_set={1,2,1,3,1,5,3,'Pool',True,(4,7,5)}
print(my_set)
my_set.add('Vania')
my_set.add(6)
my_set.discard(1)
print(my_set)

