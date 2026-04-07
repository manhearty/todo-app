


def strength(password, length, need_digit, need_upper):
    password_strength = {"upper": False, "digit": False}
    # print(password_strength)
    if len(password) > length:
        password_strength["strength"] = True
        for char in password:
            if need_digit and need_upper:
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


print(strength("manoharran9", 8, True, True))