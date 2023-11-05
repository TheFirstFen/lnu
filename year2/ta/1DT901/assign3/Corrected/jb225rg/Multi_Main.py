import MultiDisplay as multi

md = multi.MultiDisplay()

# function calls and print outs
md.set_message("Hello World!")
md.set_count(3)
print(md.to_string())
md.display()

md.set_display("Goodbye cruel world!", 2)
print(md.to_string())
print("Currant message:", md.get_message())
