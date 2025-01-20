# list 

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [25, 52, 42, 43, 16, 18, 22, 25]

print(my_list)
print(len(my_list))

my_other_list = [25, 1.79, "Coke", "Water"]

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
#print(my_other_list[-5]) IndexError: list index out of range
#print(my_other_list[4]) IndexError: list index out of range

print(my_other_list.count(25))
print(my_list.count(25))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)
#print(my_list - my_other_list)

my_other_list.append("Pepsi")
print(my_other_list)

my_other_list.insert(1, "Red")
print(my_other_list)

my_other_list[1] = "Blue"
print(my_other_list)

my_other_list.remove("Blue")
print(my_other_list)

print(my_list)
my_list.remove(25)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)
    
del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])


my_list = "Hola Python"
print(my_list)
print(type(my_list))