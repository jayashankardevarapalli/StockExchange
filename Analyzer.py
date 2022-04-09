print("\n\t\tSTOP LOSS CALCULATOR\t\t\n")
print("\n")
print("\n")

def swing_trade(s_p,sl,risk):
    diff = s_p - sl
    quantity = (risk / diff)
    profits = diff * 2 + s_p-diff
    print("\n")
    print("\n My Analysis!!!!")
    print("\n")
    print("Your STOP LOSS should be: ", s_p-diff)
    print("\nBuying Quantity should be: ", int(quantity))
    print("\nThen Your Profit will be: ", profits)
    print("\nClose the trade when you hit", profits,". That's all you could get with this trade!!!")

def intra_day():
    pass

def user_choice(uo):
    if uo == 1:
        intra_day(s_p,sl,risk)
    elif uo == 2:
        swing_trade(s_p,sl,risk)
    elif uo == 3:
        intra_day(s_p,sl,risk) && swing_trade(s_p,sl,risk)
    else:
        pass

#stock_name = input("\nEnter the stock name: ")
#investment = float(input("\nEnter the total money you want to invest: "))
uo = int(input("Which Trade You wanna do: 1) Intraday or 2) Swing Trade or 3) Both"))
s_p = float(input("\nEnter the stock price: "))
sl = float(input("\nEnter the lowest price of stock: \n \t or \nLowset price of the current and previous candle compared: \n \t or \nEnter your own low price: "))
risk = float(input("\nEnter the amount of money you can risk (You are ready to lose): "))
user_choice(uo)
