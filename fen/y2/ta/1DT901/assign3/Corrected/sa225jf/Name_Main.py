import Name as nm
# cod will print first and last name then in new row print just first name in another row print also just last name
me = nm.Name()
me.first = "Jonas"
me.last = "Lundberg"
# call funktions                                                                                                                                                      
print(me.get_first_last())
print(me.get_first())
print(me.get_last())

#here print first letter of name then a point behinde  and last name
you = nm.Name()
you.first = "Arnold"
you.last = "Palmer"
print(you.get_short_name())