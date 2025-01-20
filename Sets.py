my_Set = set()
my_other_set = {}

print(type(my_Set))
print(type(my_other_set)) #Inicialmente es un dicctionary.

my_other_set = {"Water", "Pepsi", 25}

print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Coke")

print(my_other_set) #Un set no es una estructura ordenada.

my_other_set.add("Coke") #Un set no admite repetidos.

print(my_other_set)

print("Coke" in my_other_set)
print("water" in my_other_set)

my_other_set.remove("Coke")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

my_set = {"Water", "Pepsi", 25}
my_list = list(my_set)
print(my_list)

my_other_set = {"Python", "C#", "C++"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_new_set).union({"Java", "C"}))

print(my_new_set.difference(my_Set))