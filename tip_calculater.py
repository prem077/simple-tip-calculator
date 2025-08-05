print("welcome to tip calculater")
bill=float(input("enter the total bill $:"))
tip_percent=float(input("enter the tip, 10 12 15:"))
cal=(bill * tip_percent) /100
final_bill=bill+cal
split=int(input("who many people to split ?"))
print(f"for each person to pay:{final_bill/split}")