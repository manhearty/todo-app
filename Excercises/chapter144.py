import random

while True:
    try:
        lower_bound = input("Enter lower bound of the range or q to quit: ")
        if not lower_bound == "q":
            upper_bound = input("Enter upper bound of the range or q to quit: ")

            if not lower_bound == "q":
                upper_bound = int(upper_bound)
                lower_bound = int(lower_bound)

                if lower_bound > upper_bound:
                    print("The lower bound is greater than the upper bound and hence swapping them")
                    lower_bound, upper_bound = upper_bound, lower_bound

                print(random.randint(lower_bound, upper_bound))
        else:
            print("Bye!")
            break
    except ValueError:
        print("You didn't enter a number.")
        continue