from tkinter import *
import requests
import json

h=Tk()
h.title("portfolio app")
h.iconbitmap("favicon.ico")

def font_color(amount):
    if amount>=0:
        return "green"
    else:
        return "red"

def my_portfolio():
    a=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=c12c42c1-4a21-4858-8382-ca78168cd8fd")
    b=json.loads(a.content)
    coins=[
    {"symbol":"BTC",
    "amount_owned":2,
    "price_per_coin":3200},
    {
    "symbol":"ETH",
    "amount_owned":100,
    "price_per_coin":2.05},
    {
    "symbol":"XRP",
    "amount_owned":152,
    "price_per_coin":22
    },
    {
    "symbol":"USDT",
    "amount_owned":52,
    "price_per_coin":12
    },
    {
    "symbol":"LINK",
    "amount_owned":52,
    "price_per_coin":12
    }
    ]
    total_profit_loss=0

    coin_row=1

    total_current_value=0

    for i in range(0,5):
        for coin in coins:
            if b["data"][i]["symbol"]==coin["symbol"]:
                total_paid=coin["amount_owned"]*coin["price_per_coin"]
                current_value=coin["amount_owned"] * b["data"][i]["quote"]["USD"]["price"]
                profit_loss_per_coin=b["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                total_profit_loss_coin = profit_loss_per_coin + coin["amount_owned"]
                total_profit_loss=total_profit_loss + total_profit_loss_coin
                total_current_value = total_current_value + current_value



                """print(b["data"][i]["name"]+"------"+b["data"][i]["symbol"])
                print("price-${0:.2f}".format(b["data"][i]["quote"]["USD"]["price"]))
                print("number of coin:",coin["amount_owned"])
                print("total amount_owned:","${0:.2f}".format(total_paid))
                print("current value:","${0:.2f}".format(current_value))
                print("profit_loss_per_coin:","${0:.2f}".format(profit_loss_per_coin))
                print("total_profit_loss_coin:","${0:.2f}".format(total_paid))"""


                name=Label(h,text=b["data"][i]["symbol"],bg="black",fg="white",font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                name.grid(row=coin_row,column=0,sticky=N+S+E+W)

                price=Label(h,text="${0:.2f}".format(b["data"][i]["quote"]["USD"]["price"]),bg="black",fg="white",font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                price.grid(row=coin_row,column=1,sticky=N+S+E+W)

                no_of_coins=Label(h,text=coin["amount_owned"],bg="black",fg="white",font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                no_of_coins.grid(row=coin_row,column=2,sticky=N+S+E+W)

                amount_paid=Label(h,text="${0:.2f}".format(total_paid),bg="black",fg="white",font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                amount_paid.grid(row=coin_row,column=3,sticky=N+S+E+W)

                current_value=Label(h,text="${0:.2f}".format(current_value),bg="black",fg=font_color(float("{0:.2f}".format(current_value))),font="LAto 12",padx="2",pady="2",borderwidth="2",relief="groove")
                current_value.grid(row=coin_row,column=4,sticky=N+S+E+W)

                profit_loss_per_coin=Label(h,text="${0:.2f}".format(profit_loss_per_coin),bg="black",fg=font_color(float("{0:.2f}".format(profit_loss_per_coin))),font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                profit_loss_per_coin.grid(row=coin_row,column=5,sticky=N+S+E+W)

                total_profit_loss_coin=Label(h,text="${0:.2f}".format(total_paid),bg="black",fg=font_color(float("{0:.2f}".format(total_paid))),font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                total_profit_loss_coin.grid(row=coin_row,column=6,sticky=N+S+E+W)

                coin_row=coin_row + 1


    tc=Label(h,text="${0:.2f}".format(total_current_value),bg="black",fg="white",font="Lato 12",padx="2",pady="2",borderwidth="2",relief="groove")
    tc.grid(row=coin_row,column=4,sticky=N+S+E+W)

    total_profit_loss_coin=Label(h,text="${0:.2f}".format(total_profit_loss),bg="black",fg=font_color(float("{0:.2f}".format(total_profit_loss))),font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
    total_profit_loss_coin.grid(row=coin_row,column=6,sticky=N+S+E+W)


    b=""

    update=Button(h,text="update",bg="red",fg="white",command=my_portfolio,font="Lato 12",padx="2",pady="2",borderwidth="2",relief="groove")
    update.grid(row=coin_row + 1,column=6,sticky=N+S+E+W)


name=Label(h,text="Coin name",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
name.grid(row=0,column=0,sticky=N+S+E+W)

price=Label(h,text="price",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
price.grid(row=0,column=1,sticky=N+S+E+W)

no_of_coins=Label(h,text="Coin Owned",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
no_of_coins.grid(row=0,column=2,sticky=N+S+E+W)

amount_paid=Label(h,text="total amount paid",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
amount_paid.grid(row=0,column=3,sticky=N+S+E+W)

current_value=Label(h,text="current_value",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
current_value.grid(row=0,column=4,sticky=N+S+E+W)

profit_loss_per_coin=Label(h,text="profit_loss_per_coin",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
profit_loss_per_coin.grid(row=0,column=5,sticky=N+S+E+W)

total_profit_loss_coin=Label(h,text="total_profit_loss_coin",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
total_profit_loss_coin.grid(row=0,column=6,sticky=N+S+E+W)

my_portfolio()

h.mainloop()

print("program completed")
