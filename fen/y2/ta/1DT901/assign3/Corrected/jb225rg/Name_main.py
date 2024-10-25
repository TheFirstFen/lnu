import Name as nm

# dataclass name
me = nm.Name("Julia", "Bergön")

# print out
print(me.to_string())
print(me.get_first())
print(me.get_last())

# print out
you = nm.Name()
you.set_first("Johan")
you.set_last("Andersson")
print(you.short_name())
