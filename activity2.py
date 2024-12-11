#Assigning variables
var_actual_cost = int(input("Input the Actual products price "))
var_sales_cost = int(input("Input the price your selling the product for "))
if var_actual_cost < var_sales_cost:
    var_profit = var_sales_cost - var_actual_cost
    print("Total profit ", var_profit)
else:
    var_loss = var_sales_cost - var_actual_cost
    print("Total loss ", var_loss)