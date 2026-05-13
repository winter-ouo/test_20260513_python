import numpy as np
import csv

# 建立空 list
product_id = []
product_name = []
stock_quantity = []
unit_price = []
sales_volume = []

# =========================
# 讀取 CSV
# =========================
with open("HW_20260513_dataset.csv", "r", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:

        # 商品編號
        product_id.append(row["Product_ID"])

        # 商品名稱
        product_name.append(row["Product_Name"])

        # 庫存數量
        stock_quantity.append(float(row["Stock_Quantity"]))

        # 單價
        unit_price.append(
            float(
                row["Unit_Price"]
                .replace("$", "")
                .replace(",", "")
                .strip()
            )
        )

        # 銷售量
        sales_volume.append(float(row["Sales_Volume"]))

# =========================
# 轉成 numpy array
# =========================
product_id = np.array(product_id)
product_name = np.array(product_name)
stock_quantity = np.array(stock_quantity)
unit_price = np.array(unit_price)
sales_volume = np.array(sales_volume)

# =========================
# (1) 計算每個商品的總庫存價值
# =========================
inventory_value = stock_quantity * unit_price

# =========================
# (2) 找出最暢銷商品（可多人並列）
# =========================

# 找最大銷售量
max_sales = np.max(sales_volume)

# 找所有最大銷售量的位置
best_seller_indices = np.where(sales_volume == max_sales)[0]

# =========================
# (3) 計算 9 折後收入
# =========================

# 原始收入
revenue = unit_price * sales_volume

# 9折後收入
discount_revenue = revenue * 0.9

# =========================
# 輸出 CSV
# =========================
with open("HW_20260513_OK.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    # 標題列
    writer.writerow([
        "Product_ID",
        "Product_Name",
        "Inventory_Value",
        "Revenue_90%",
        "Best_Seller"
    ])

    # 寫入資料
    for i in range(len(product_name)):

        # 判斷是否為最暢銷商品
        if i in best_seller_indices:
            best = "Best Seller"
        else:
            best = ""

        writer.writerow([
            product_id[i],
            product_name[i],
            round(inventory_value[i], 2),
            round(discount_revenue[i], 2),
            best
        ])

# =========================
# 額外印出最暢銷商品
# =========================
print("最暢銷商品：")

for i in best_seller_indices:
    print(product_name[i])