immutable_var=(1,2.7,"sun",True)
print(immutable_var)
#immutable_var[2]=7  - является ошибкой, т.к строка "sun",
# которую мы хотим заменить на 7, является неизменяемым объектом



mutable_list=[1,"a","sun",True]
print(mutable_list)
mutable_list[2]=7
print(mutable_list)