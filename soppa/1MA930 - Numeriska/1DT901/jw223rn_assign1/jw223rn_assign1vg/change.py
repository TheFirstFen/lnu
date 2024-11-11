price = float(input("Price: "))
payment = float(input("Payment: "))

change = payment - price    #calcuates the amount of change to be returned
r_change = round(change)    #rounds the amount of change to the closest integer


c1000 = r_change // 1000    #calculates how many bills of the current bill that needs to be returned, in this case 1000 kr bills.
mon_ret = c1000 * 1000      #mon_ret stores how much money returned by the previous bills. This gets updated by each bill.

c500 = (r_change - mon_ret) // 500
mon_ret = c500 * 500 + mon_ret

c200 = (r_change - mon_ret) // 200
mon_ret = c200 * 200 + mon_ret

c100 = (r_change - mon_ret) // 100
mon_ret = c100 * 100 + mon_ret

c50 = (r_change - mon_ret) // 50
mon_ret = c50 * 50 + mon_ret

c20 = (r_change - mon_ret) // 20
mon_ret = c20 * 20 + mon_ret

c10 = (r_change - mon_ret) // 10
mon_ret = c10 * 10 + mon_ret

c5 = (r_change - mon_ret) // 5
mon_ret = c5 * 5 + mon_ret

c2 = (r_change - mon_ret) // 2
mon_ret = c2 * 2 + mon_ret

c1 = (r_change - mon_ret) // 1


#prints how many of each bills that needs to be returned and the amount of change to be returned
print(f"Change: {r_change} kr")
print(f"1000kr bills: {c1000}")
print(f"500kr bills: {c500}")
print(f"200kr bills: {c200}")
print(f"100kr bills: {c100}")
print(f"50kr bills: {c50}")
print(f"20kr bills: {c20}")
print(f"10kr coins: {c10}")
print(f"5kr coins: {c5}")
print(f"2kr coins: {c2}")
print(f"1kr coins: {c1}")


