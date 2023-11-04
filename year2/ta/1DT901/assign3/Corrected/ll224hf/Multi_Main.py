import MultiDisplay as multi

# Program starts
md = multi.MultiDisplay()

md.set_message("Hello World!")
md.set_count(3)
print(md.to_string())                  # print-out
md.display()                           # print-out

md.set_display("Goodbye cruel world!", 2)    # print-out
print(md.to_string())                        # print-out
print("Current message:", md.get_message())  # print_out
