import Name_13 as nm

# Creat and initialize a Name object
me = nm.Name()
me.first = "Yasin"
me.last = "Alahdab"

print(me.get_first_last())
print(me.get_first())
print(me.get_last())

# Creat an empty Name object
you = nm.Name()
you.first("Arnold")
you.last("Palmer")
print(you.get_short_name())
