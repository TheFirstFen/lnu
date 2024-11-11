f_name = input("First name: ")
m_name = input("Middle name: ")
l_name = input("Last name: ")

cap_f_name = f_name.capitalize()
cap_m_name = m_name.capitalize()
cap_l_name = l_name.capitalize()

print(f"Short name: {cap_f_name[0]}. {cap_m_name[0]}. {cap_l_name[0:4]}")