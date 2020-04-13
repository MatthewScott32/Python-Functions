def calc_dollars(**coins):
    bank = {
        'pennies': coins["pennies"],
        'nickels': coins["nickels"],
        'dimes': coins["dimes"],
        'quarters': coins["quarters"]
    }

    dollar_amount = 0 
    
    dollar_amount += coins['pennies'] * .01 + coins['nickels'] * .05 + coins['dimes'] * .1 + coins["quarters"] * .25

    print(f'You have {dollar_amount} in your account.')


calc_dollars(pennies = 200, nickels = 30, dimes = 10, quarters = 80)