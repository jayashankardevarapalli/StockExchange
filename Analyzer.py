print("\n\t\tSTOP LOSS CALCULATOR\t\t\n")
print("\n")
print("\n")

def swing_trade(s_p,sl,risk,investment):
    diff = s_p - sl
    quantity = (risk / diff)
    profits = diff * 2 + s_p-diff
    while(1):
        if risk > investment:
            print("\n Your risk is more than the investment.")
            break
        else:
            pass
        print("\n")
        print("\n My Analysis!!!!")
        print("\n")
        print("\nYour STOP LOSS should be: ", s_p-diff)
        print("\nQuantity you could buy with your investment: ")
        print("\nGeneral Buying Quantity should be: ", int(quantity))
        print("\nThen Your Profit will be: ", profits)
        print("\nClose the trade when you hit", profits,". That's all you could get with this trade!!!")

def intra_day(s_p,sl,risk,investment):
    pass

def user_choice(uo):
    if uo == 1:
        intra_day(s_p,sl,risk)
    elif uo == 2:
        swing_trade(s_p,sl,risk,investment)
    elif uo == 3:
        intra_day(s_p,sl,risk) and swing_trade(s_p,sl,risk)
    else:
        pass


investment = float(input("\nEnter the total money you want to invest: "))
uo = int(input("\nWhich Trade You wanna do: 1) Intraday or 2) Swing Trade or 3) Both: "))
s_p = float(input("\nEnter the stock price: "))
sl = float(input("\nEnter the lowest price of stock: \n \t or \nLowset price of the current and previous candle compared: \n \t or \nEnter your own low price: "))
risk = float(input("\nEnter the amount of money you can risk (You are ready to lose): "))
user_choice(uo)
