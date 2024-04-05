# Using data class Name
import Name as nm

# Creat and initialize a Name object
me = nm.Name("Jonas", "Lundberg")
print(me.to_string())
print(me.get_first())
print(me.get_last())

# Creat an empty Name object
you = nm.Name()
you.set_first("Arnold")
you.set_last("Palmer")
print(you.get_short_name())
