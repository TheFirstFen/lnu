import Name as nm


me = nm.Name("Samir", "Ola")
print(me.to_string())
print(me.get_first())
print(me.get_last())

you = nm.Name()
you.set_first("Ahmad")
you.set_last("Mohsen")
print(you.get_short_name())
