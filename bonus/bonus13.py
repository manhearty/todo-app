feet_inches = input("Enter feet and inches: ")

def parse(feetinches_local):
    parts = feetinches_local.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    feet, inches = parse(feet_inches)
    meters = feet * 0.3048 + inches * 0.0254
    return meters

f, i = parse(feet_inches)
print(f, i)
result = convert(f, i )

if result < 1:
    print("Kid is too small.")
else:
    print("kid can use the slide")