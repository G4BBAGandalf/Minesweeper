def find_max(a):
    maximum = a[0]
    for number in a:
        if number > maximum:
            maximum = number
    return maximum