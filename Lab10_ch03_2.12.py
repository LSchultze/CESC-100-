joe_pay = 2000*40
joe_sold = 2000*42.75
commission_bought = int(joe_pay)*.03
commission_sold = int(joe_sold)*.03
joe_end = joe_sold-joe_pay-commission_bought-commission_sold
print("Joe payed", joe_pay)
print("Joe sold for", joe_sold)
print("Joe payed", commission_bought, "when he bought the stock.")
print("Joe payed", commission_sold, "when he sold the stock.")
print("In the end, the total profit Joe made was", joe_end)