price = float(input("Price: "))
payment = float(input("Payment: "))
change = round(payment - price)
bills_1000 = 0
bills_500=0
bills_200=0
Bills_100=0
bills_50=0
bills_20=0
coins_10=0
coins_5=0
coins_2=0
coins_1=0

print (f"{change} kr")
ills_1000 =change//1000
change= change %1000
bills_500 =change//500
change= change %500
ills_200 =change//200
change= change %200
bills_100 =change//100
change= change %100
bills_50 =change//50
change= change %50
bills_20 =change//20
change= change %20
coins_10 =change//10
change= change %10
coins_5 =change//5
change= change %5
coins_2 =change//2
change= change %2
coins_1 =change//1
change= change %1

print(f"1000kr bills: {bills_1000}")
print(f"500kr bills: {bills_500}")
print(f"200kr bills: {bills_200}")
print(f"100kr bills: {bills_100}")
print(f"50kr bills: {bills_50}")
print(f"20kr bills: {bills_20}")
print(f"10kr coins: {coins_10}")
print(f"5kr coins: {coins_5}")
print(f"2kr coins: {coins_2}")
print(f"1kr coins: {coins_1}")