try:
    total_value = float(input("Enter total value: "))
    if total_value == 0:
        print("Your total value cannot be zero.")
        exit()

    value = float(input("Enter value: "))
    calculation = (value / total_value) * 100
    print(f"That is {calculation}%")

except ValueError:
    print("You need to enter a number. Run the program again.")



numb = 5
try:
    result = numb / 0
except ZeroDivisionError:
    print("You cannot divide by Zero" )
except ValueError:
    print("You need to enter a number. Run the program again.")