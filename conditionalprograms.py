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


x = input("What is your name? ").capitalize().strip().title() # This will take the input from the user, remove any leading or trailing whitespace, and convert it to title case (first letter of each word capitalized)
print(f"Hello {x}!")
match x:
    case "Harry" | "Hermione" | "Ron":
        print ("Your House is Gryffindor!")
    case "Draco":
        print ("Your House is Slytherin!")  
    case _:
        print ("I don't know which house you belong to.")
