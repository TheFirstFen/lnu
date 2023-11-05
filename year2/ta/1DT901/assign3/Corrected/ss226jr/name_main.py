# Using data class name
import name as nm

# create and initialize a name object
me = nm.Name("Jonas", "Lundberg")
print(me.to_string())
print(me.get_first())
print(me.get_last())

# create an empty name object
you = nm.Name()
you.set_first("Arnold")
you.set_last("Palmer")
print(you.get_short_name())
