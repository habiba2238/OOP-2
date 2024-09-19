# Initial list of customer names
customers = ["Alice", "Bob", "Charlie", "David", "Eve"]

# a. Access the third customer in the list and print their name
third_customer = customers[2]  # Lists are zero-indexed, so the third customer is at index 2
print("Third customer:", third_customer)

# b. Change the name of the second customer to "Ben"
customers[1] = "Ben"  # The second customer is at index 1
print("Updated customer list after changing the second customer:", customers)

# c. Add a new customer named "Frank" to the end of the list
customers.append("Frank")  # Append adds the customer to the end of the list
print("Updated customer list after adding Frank:", customers)

# d. Remove the customer "David" from the list
customers.remove("David")  # Remove "David" from the list
print("Updated customer list after removing David:", customers)

# e. Sort the customer names alphabetically and print the final list
customers.sort()  # Sort the list alphabetically
print("Final sorted customer list:", customers)
