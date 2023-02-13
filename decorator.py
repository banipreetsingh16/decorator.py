# convert the number to words using decorators

amount = int(input("Enter the number in range 1 to 100: "))
def format(amount):
    """
    This function converts the entered number in to form shown below
    ex. 49 ----->  49.0
    :param amount
    :return
    """
    return f"{amount}.00"

words_name = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',8:'eight',9:'nine', 10:'ten',
            11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',17:'seventeen',18:'eighteen', 19:'ninteen',
            20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty',70:'seventy',80:'eighty',90:'ninty', 100:'hundred', 1000:'thousand'
           }


def word(func, amt):
    for_amount = func(amt)
    for_amount = float(for_amount)
    if for_amount in words_name:
          res = words_name.get(for_amount)
    else:
        rem = for_amount%10
        last_digit = words_name.get(rem)
        first = for_amount // 10
        c = first * 10
        digit = words_name.get(c)
        res=digit+" "+ last_digit
        return res
div = word(format, amount)
print(div)
