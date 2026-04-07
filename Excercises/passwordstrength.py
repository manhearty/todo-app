password_strength = {"upper": False, "digit": False}
#print(password_strength)


def strength(password):
    if len(password) > 8:
        password_strength["strength"] = True
        for char in password:
            if char.isupper():
                password_strength["upper"] = True
            elif char.isdigit():
                password_strength["digit"] = True

    else:
        password_strength["strength"] = False

    if all(password_strength.values()):
        return "Strong Password"
    else:
        return "Weak Password"


print(strength("manoharran9"))