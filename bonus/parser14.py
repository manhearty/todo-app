def parse(feetinches_local):
    parts = feetinches_local.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches
