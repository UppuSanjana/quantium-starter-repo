import pandas as pd


file1 = pd.read_csv("data/daily_sales_data_0.csv")
file2 = pd.read_csv("data/daily_sales_data_1.csv")
file3 = pd.read_csv("data/daily_sales_data_2.csv")
sales_data = pd.concat([file1, file2, file3], ignore_index=True)
sales_data = sales_data[sales_data["product"] == "pink morsel"]
sales_data["price"] = sales_data["price"].replace("[$]", "", regex=True)
sales_data["price"] = sales_data["price"].astype(float)
sales_data["Sales"] = sales_data["quantity"] * sales_data["price"]
final_data = sales_data[["Sales", "date", "region"]]
final_data.columns = ["Sales", "Date", "Region"]
final_data.to_csv("formatted_sales.csv", index=False)
print("Processing completed successfully!")
print("Output saved as formatted_sales.csv")