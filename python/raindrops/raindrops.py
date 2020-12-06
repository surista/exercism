def convert(number):
    sol = ""
    if number % 3 == 0:
        sol += "Pling"
    if number % 5 == 0:
        sol += "Plang"
    if number % 7 == 0:
        sol += "Plong"
    if number %3  != 0 and number %5  != 0 and number % 7 != 0:
        return str(number)

    return sol

