def sum_of_multiples(limit, values):
    multiples = set()
    for val in values:
        if val > 0:
            for multiple in range(val,limit,val):
                multiples.add(multiple)
    return sum(multiples)