x = float(input("Enter a number: "))#better take input as float rather than integer 
y = float(input("Enter another number: "))
z = x + y
a = x - y
b = x * y   
c = x / y
d = x % y
print(f"The sum is:{z:.2f}") # This will print the sum of x and y with 2 decimal places
print(f"The difference is:{a:.2f}")
print(f"The product is:{b:.2f}")
print(f"The quotient is:{c:.2f}")
print(f"The remainder is:{d:.2f}")
