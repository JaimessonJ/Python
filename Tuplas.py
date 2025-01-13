my_tuple = tuple()
my_other_tuple = ()
 
my_tuple = (24, "Alejandro", 1.79)
my_other_tuple = (65, 58, 99)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Alejandro"))
print(my_tuple.index(1.79))

#my_tuple[1] = 2 # Una tupla es inmutable

my_sum_tuples = my_tuple + my_other_tuple
print(my_sum_tuples)

print(my_sum_tuples[3:5])