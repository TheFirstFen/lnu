import MultiDisplay as multi

# program starts
md = multi.MultiDisplay()

(md.set_message("Hello World!"))
print(md.set_count(3))
print(md.to_string())
md.display()

md.set_display("Goodbye cruel world!", 2)
print(md.to_string())
print("Current message:", md.get_message())
