customer_list_1 = ["TYSON FOODS", "ATLAS FOODS GROUP"]
customer_list_2 = ["OK FOODS INC", "GROVE SERVICES", "PROTEIN ALLIANCE"]

print("first customer in list 1:", customer_list_1[0])
print("number of customers in list 2:", len(customer_list_2))

# combining all customers into a single list
all_customers = customer_list_1 + customer_list_2
print("all customers:", all_customers)

# add a new customer to the end of the list
all_customers.append("CONAGRA FROZEN FDS")
print("updated list:", all_customers)