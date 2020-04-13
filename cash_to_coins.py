dollarAmount = 8.69

def cash_to_coins(**coins):
    bank = {
        'pennies': 0,
        'nickels': 0,
        'dimes': 0,
        'quarters': 0
    }

    dollarAmount = 8.69
    bank["quarters"] = int(dollarAmount / .25)
    remainder = round((dollarAmount % .25), 2)
    bank["dimes"] = int(remainder / .1)
    remainder = round((remainder % .1), 2)
    bank["nickels"] = int(remainder / .05)
    remainder = round((remainder % .05), 2)
    bank["pennies"] = int(remainder / .01)
    remainder = round((remainder % .01), 2)
    print(f'You have {bank} in your account.')


cash_to_coins()