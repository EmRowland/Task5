total_share = 2000 * 40
total_commision = total_share * 0.03
#sales records
total_sold = 2000 * 42.75
sold_commision = total_sold * 0.03
total_bmoney = total_share + total_commision + sold_commision
total_smoney = total_sold

money_left = total_smoney - total_bmoney

print(f"Amount joe paid for the stock is:  ${total_share}")

print(f"Amount of commission joe paid when purchasing the stock is: ${total_commision}")


print(f"Joe sold the stock for : ${total_sold} ")

print(f"Amount of commission Joe paid after selling the stock:  ${sold_commision}" )

print(f"Amount of money left with joe is:${money_left}")

