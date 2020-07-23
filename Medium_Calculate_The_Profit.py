"""
You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars),
and the starting inventory. Return the total profit made, rounded to the nearest dollar.
Assume all of the inventory has been sold.

"""

def profit(cost_price,sell_price,inventory):
    profit = (sell_price-cost_price)*inventory
    return round(profit,0)
