def is_armstrong_number(number):
    digit_list = [i for i in str(number)]

    sol = sum([int(x)**len(digit_list) for x in digit_list])

    return sol cw== number