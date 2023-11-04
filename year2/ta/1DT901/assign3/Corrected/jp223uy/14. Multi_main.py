from multi import Multi
# Program starts
multdi = Multi()
multdi.set_message("Hello world!")
multdi.set_count(3)
multdi.to_string()
multdi.display()

multdi.set_display("Goodbye cruel world!", 2)
multdi.display()
multdi.to_string()
print("Current message:", multdi.get_message())
