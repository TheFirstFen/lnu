from name import Name
# Program starts
me = Name("Jakob", "Persson")
gn = me.get_name()
print(gn)
f = me.get_first()
print(f)
L = me.get_last()
print(L)


you = Name()
you.set_first("Arnold")
you.set_last("Palmer")
print(you.short_name())
