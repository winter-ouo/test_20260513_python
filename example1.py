import numpy as np
import csv

products = []
price = []
stock = []
discount = []

with open("Stock_1.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f) #DictReader = 用欄位名稱讀 CSV

    for row in reader:
        products.append(row["Product"])
        price.append(float(row["Price"]))
        stock.append([float(row["Stock_A"]),float(row["Stock_B"]),float(row["Stock_C"])])
        discount.append(float(row["Discount"]))

products = np.array(products)
price = np.array(price)
stock = np.array(stock)
discount = np.array(discount)

total_stock = stock.sum(axis=1)
total_value = price * total_stock
discount_price = price * discount

hot = np.argmax(total_stock)
low = np.argmin(total_stock)

with open("Stock_OK.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Product", "Stock", "Value", "Discount", "Hot", "Low"])#寫入 CSV 一列，low可有可沒有

    for i in range(len(products)):
        w.writerow([
            products[i],
            total_stock[i],
            total_value[i],
            discount_price[i],
            i == hot,
            i == low
        ])