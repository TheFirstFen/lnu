import MultiDisplay as multi

md = multi.MultiDisplay()
md.set_message("Hello World")
md.set_count(3)                           #set_count mangel "repeat stirng" will repeat string three times "Hello world"
print(md.to_string())
md.display()

md.set_display("Goodbye cruel world!", 2)   # repeat "Goodbye....... two onec"
md.display()                                #give a last messeage and and how many times repeat
print(md.to_string())
print("Current message:", md.get_message())      
