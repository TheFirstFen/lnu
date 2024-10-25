from name import Name

me = Name("Oliwer", "Brusberg")
print(me.get_name())
print(me.get_first())
print(me.get_last())

you = Name()
you.set_first("Arnold")
you.set_last("Palmer")
print(you.short_name())
