from tkinter import *
from tkinter import messagebox,Menu
import requests
import json
import sqlite3

h=Tk()
h.title("portfolio app")
h.iconbitmap("favicon.ico")
con=sqlite3.connect("paisa.db")
conobj=con.cursor()

"""conobj.execute("create table if not exists coin(id integer primary key,symbol text,amount integer, price real)")
con.commit()

conobj.execute("insert into coin values(1,'ETH',5,120)")
con.commit()

conobj.execute("insert into coin values(2,'BTC',2,11)")
con.commit()

conobj.execute("insert into coin values(3,'XRP',3,46)")
con.commit()"""

def reset():
    for cell in h.winfo_children():
        cell.destroy()

    app_header()
    my_portfolio()

def nav_app():
    def clear_all():
        conobj.execute("delete from coin")
        con.commit()
        messagebox.showinfo("portfolio notification","coin is deletd in portfolioi successfully")
        reset()
    def close_app():
        h.destroy()

    menu=Menu(h)
    file_item=Menu(menu)
    file_item.add_command(label='clear portfolio',command="clear_all")
    file_item.add_command(label='close portfolio',command="close_app")
    menu.add_cascade(label="file",menu=file_item)
    h.config(menu=menu)






def my_portfolio():
    a=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=c12c42c1-4a21-4858-8382-ca78168cd8fd")
    b=json.loads(a.content)

    conobj.execute("select * from coin")
    coins=conobj.fetchall()



    def font_color(amount):
        if amount>=0:
            return "green"
        else:
            return "red"

    def insert_coin():
        conobj.execute("insert into coin(symbol,price,amount)values(?,?,?)",(symbol_txt.get(),price_txt.get(),amount_txt.get()))
        con.commit()
        messagebox.showinfo("portfolio notification","coin is added in portfolioi successfully")
        reset()


    def update_values():
        conobj.execute("update coin set symbol=?,amount=?,price=? where id=?",(symbol_update.get(),amount_update.get(),price_update.get()))
        con.commit()
        messagebox.showinfo("portfolio notification","coin is updated in portfolioi successfully")
        reset()



    def delete_values():
        conobj.execute("delete from coin where id=?",(portfolio_delete.get()))
        con.commit()
        messagebox.showinfo("portfolio notification","coin is deleted from portfolioi successfully")
        reset()




    total_profit_loss=0

    coin_row=1

    total_current_value=0

    total_amount_paid=0

    for i in range(0,5):
        for coin in coins:
            if b["data"][i]["symbol"]==coin[1]:
                total_paid=coin[2]*coin[3]
                current_value=coin[2] * b["data"][i]["quote"]["USD"]["price"]
                profit_loss_per_coin=b["data"][i]["quote"]["USD"]["price"] - coin[3]
                total_profit_loss_coin = profit_loss_per_coin + coin[2]
                total_profit_loss=total_profit_loss + total_profit_loss_coin
                total_current_value = total_current_value + current_value
                total_amount_paid=total_amount_paid + total_paid


                """print(b["data"][i]["name"]+"------"+b["data"][i]["symbol"])
                print("price-${0:.2f}".format(b["data"][i]["quote"]["USD"]["price"]))
                print("number of coin:",coin["amount_owned"])
                print("total amount_owned:","${0:.2f}".format(total_paid))
                print("current value:","${0:.2f}".format(current_value))
                print("profit_loss_per_coin:","${0:.2f}".format(profit_loss_per_coin))
                print("total_profit_loss_coin:","${0:.2f}".format(total_paid))"""

                portfolio_id=Label(h,text=coin[0],bg="black",fg="white",font="LATO 12",padx="2",pady="2",borderwidth="2",relief="groove")
                portfolio_id.grid(row=coin_row,column=0,sticky=N+S+E+W)


                name=Label(h,text=b["data"][i]["symbol"],bg="black",fg="white",font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                name.grid(row=coin_row,column=1,sticky=N+S+E+W)

                price=Label(h,text="${0:.2f}".format(b["data"][i]["quote"]["USD"]["price"]),bg="black",fg="white",font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                price.grid(row=coin_row,column=2,sticky=N+S+E+W)

                no_of_coins=Label(h,text=coin[2],bg="black",fg="white",font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                no_of_coins.grid(row=coin_row,column=3,sticky=N+S+E+W)

                amount_paid=Label(h,text="${0:.2f}".format(total_paid),bg="black",fg="white",font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                amount_paid.grid(row=coin_row,column=4,sticky=N+S+E+W)

                current_value=Label(h,text="${0:.2f}".format(current_value),bg="black",fg=font_color(float("{0:.2f}".format(current_value))),font="LAto 12",padx="2",pady="2",borderwidth="2",relief="groove")
                current_value.grid(row=coin_row,column=5,sticky=N+S+E+W)

                profit_loss_per_coin=Label(h,text="${0:.2f}".format(profit_loss_per_coin),bg="black",fg=font_color(float("{0:.2f}".format(profit_loss_per_coin))),font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                profit_loss_per_coin.grid(row=coin_row,column=6,sticky=N+S+E+W)

                total_profit_loss_coin=Label(h,text="${0:.2f}".format(total_profit_loss_coin),bg="black",fg=font_color(float("{0:.2f}".format(total_profit_loss_coin))),font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
                total_profit_loss_coin.grid(row=coin_row,column=7,sticky=N+S+E+W)


                coin_row=coin_row + 1

#insert coin

    symbol_txt=Entry(h,borderwidth="2",relief="groove")
    symbol_txt.grid(row=coin_row+1,column=1)

    amount_txt=Entry(h,borderwidth="2",relief="groove")
    amount_txt.grid(row=coin_row+1,column=3)

    price_txt=Entry(h,borderwidth="2",relief="groove")
    price_txt.grid(row=coin_row+1,column=2)

    inser=Button(h,text="add_coin",bg="black",fg="white",command=insert_coin,font="Lato 12",padx="2",pady="2",borderwidth="2",relief="groove")
    inser.grid(row=coin_row + 1,column=4,sticky=N+S+E+W)

#update coin

    portfolioId=Entry(h,borderwidth="2",relief="groove")
    portfolioId.grid(row=coin_row+2,column=0)

    symbol_update=Entry(h,borderwidth="2",relief="groove")
    symbol_update.grid(row=coin_row+2,column=1)

    amount_update=Entry(h,borderwidth="2",relief="groove")
    amount_update.grid(row=coin_row+2,column=2)

    price_update=Entry(h,borderwidth="2",relief="groove")
    price_update.grid(row=coin_row+2,column=3)

    update_button=Button(h,text="update_coin",bg="black",fg="white",command=update_values,font="Lato 12",padx="2",pady="2",borderwidth="2",relief="groove")
    update_button.grid(row=coin_row+2,column=4,sticky=N+S+E+W)

#delete coin

    portfolio_delete=Entry(h,borderwidth="2",relief="groove")
    portfolio_delete.grid(row=coin_row+3,column=0)

    delete_button=Button(h,text="delete coin",bg="black",fg="white",command=delete_values,font="Lato 12",padx="2",pady="2",borderwidth="2",relief="groove")
    delete_button.grid(row=coin_row+3,column=4,sticky=N+S+E+W)





    tc=Label(h,text="${0:.2f}".format(total_current_value),bg="black",fg="white",font="Lato 12",padx="2",pady="2",borderwidth="2",relief="groove")
    tc.grid(row=coin_row,column=5,sticky=N+S+E+W)


    total_amount_ap=Label(h,text="${0:.2f}".format(total_amount_paid),bg="black",fg="white",font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
    total_amount_ap.grid(row=coin_row,column=4,sticky=N+S+E+W)

    total_profit_loss_coin=Label(h,text="${0:.2f}".format(total_profit_loss),bg="black",fg=font_color(float("{0:.2f}".format(total_profit_loss))),font="LAto 12 ",padx="2",pady="2",borderwidth="2",relief="groove")
    total_profit_loss_coin.grid(row=coin_row,column=7,sticky=N+S+E+W)



    b=""

    refresh=Button(h,text="refresh",bg="red",fg="white",command=reset,font="Lato 12",padx="2",pady="2",borderwidth="2",relief="groove")
    refresh.grid(row=coin_row + 1,column=6,sticky=N+S+E+W)

def app_header():
    portfolio_id=Label(h,text="portfolio_id",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    portfolio_id.grid(row=0,column=0,sticky=N+S+E+W)


    name=Label(h,text="Coin name",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    name.grid(row=0,column=1,sticky=N+S+E+W)

    price=Label(h,text="price",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    price.grid(row=0,column=2,sticky=N+S+E+W)

    no_of_coins=Label(h,text="Coin Owned",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    no_of_coins.grid(row=0,column=3,sticky=N+S+E+W)

    amount_paid=Label(h,text="total amount paid",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    amount_paid.grid(row=0,column=4,sticky=N+S+E+W)

    current_value=Label(h,text="current_value",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    current_value.grid(row=0,column=5,sticky=N+S+E+W)

    profit_loss_per_coin=Label(h,text="profit_loss_per_coin",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    profit_loss_per_coin.grid(row=0,column=6,sticky=N+S+E+W)

    total_profit_loss_coin=Label(h,text="total_profit_loss_coin",bg="blue",fg="white",font="LAto 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    total_profit_loss_coin.grid(row=0,column=7,sticky=N+S+E+W)

nav_app()
app_header()
my_portfolio()
h.mainloop()
conobj.close()
con.close()

print("program completed")
