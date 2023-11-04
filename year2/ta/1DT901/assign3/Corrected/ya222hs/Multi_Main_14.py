import MultiDisplay_14 as multi

# Program starts
md = multi.MultiD()

md.message_("Hello World!")
md.count_(3)
print(md.string())                  # print-out
md.disp()                           # print-out

md.disp_("Goodbye cruel world!", 2)
md.disp()    # print-out
print(md.string())                        # print-out
print("Current message:", md.get_message())
