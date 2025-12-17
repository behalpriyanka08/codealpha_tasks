stock_price = { "AAPL": 180,"TSLA": 250,"GOOGL": 140,"MSFT": 330}
total_investment = 0
portfolio = []

n = int(input("Enter number of different stocks : "))

for i in range(n):
    stock = input("Enter stock name : ").upper()
    quantity = int(input("Enter quantity of stock : "))

    if stock in stock_price :
        price = stock_price[stock]
        investment = price * quantity
        total_investment += investment
        portfolio.append(f"stock - Qty : {quantity} , Value : {investment}")
    else:
        print("Stock not available")
    
print("---Portfolio Summary---")
for item in portfolio:
         print(item)
print("Total Investment :", total_investment)


save = input("Do you want to save file {Yes/No}").lower()

if save =="yes":
   f = open("portfolio.txt","w")
   f.write("Stock Portfolio Summary")
   for item in portfolio:
       f.write(item+ "\n")
   f.write("Total Investment : {total_investment}Rs ") 
print("Data saved in text file")  
    