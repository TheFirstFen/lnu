import list_functions as lf

lst = lf.random_list(10)
print("random_list: ", lst)

print("average: ", lf.average(lst) )

print("only_odd: ", lf.only_odd(lst) )

print("to_string: ", lf.to_string(lst) )

print("contains: ", lf.contains([6,7,8,9],7,8) )

print("has_duplicates: ", lf.has_duplicates(lst) )
