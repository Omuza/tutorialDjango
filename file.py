def BMICalc(height, weight):
    result = (height / weight) ** 2

    if result < 18.5:
        return "NIEDOWAGA"
    elif 18.5 >= result >= 25:
        return "NORMA"
    elif 25 > result < 30:
        return "NADWAGA"
    elif result > 30:
        return "OTYŁOŚĆ"