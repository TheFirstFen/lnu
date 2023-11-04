n = int(input("Please provide monthly income: "))

if n <= 38000:
    n1 = round(n * 0.30)  # * 0.30 om n är mindre än 38000
    print(f"Corresponding income tax: {n1}")
elif n <= 50000 and n >= 38000:
    n2 = round(n - 38000) * 0.35  # (n - 38000) * 0.35 för 35% skatt
    n_rest = 38000 * 0.30  # 38000 * 0.30 är rest
    print(f"Corresponding income tax: {n2+n_rest}")
elif n >= 50000:
    n3 = round(n - 50000) * 0.40
    n3_1 = 38000 * 0.30
    n3_2 = 12000 * 0.35
    print(f"Corresponding income tax: {n3+n3_1+n3_2}")
else:
    print("Invalid")
