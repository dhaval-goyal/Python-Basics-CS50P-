x = float(input("Select any number 1:"))
y = float(input("Select any number 2:"))
if x > y:
    print(f"{x} is greater than {y}")

elif x == y:
    print(f"{x} is equal to {y}")

else:
    print(f"{y} is greater than {x}")


def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print(f"{x} is an even number.")
    else:
        print(f"{x} is an odd number.") 
        
def is_even(num):
    return True if num % 2 == 0 else False # This will return True if the number is even and False if the number is odd

main()
