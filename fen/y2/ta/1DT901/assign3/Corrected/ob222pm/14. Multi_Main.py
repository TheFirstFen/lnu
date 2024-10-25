from MultiDisplay import Multi

md = Multi()
md.set_message("Hello world!")
md.set_count(3)
md.to_string()
md.display()

md.set_display("Goodbye cruel world!", 2)
md.display()
md.to_string()
print("Current message:", md.get_message())
