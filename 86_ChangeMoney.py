
# change money
# /

# take an int (amount money give), and return a dictionary of quantity values (money/bill).


def changeMoney(money_give: float):
    types_money = [
        0.01, 0.02, 0.05,  # coper coin.
        0.1, 0.2, 0.5,  # yellow coin.
        1, 2,  # integer coin.
        5, 10, 20, 50, 100  # bills.
    ]

    money_give = castfloatToCent(money_give)  # cast as cent (to avoid float error).

    output = dict()

    while money_give >= 1:

        # find the bigest money type who fit.
        type_money_find = None
        for type_money in types_money[::-1]:
            type_money_cent = castfloatToCent(type_money)
            if type_money_cent > money_give:
                continue
            type_money_find = type_money_cent
            break

        # increment.
        key_type = castCentToStr(type_money_find)
        if key_type in output:
            output[key_type] += 1
        output[key_type] = 1

        # decrement.
        money_give -= type_money_find
    
    print(money_give)  # error of decimal : never user float type for processing money.

    return output


def castfloatToCent(value: float) -> int:
    return int(round(value * 100))

def castCentToStr(value: int) -> str:
    value_str = str(value)
    return value_str[:-2] or '0' + '.' + value_str[-2:]



print(changeMoney(52.22))