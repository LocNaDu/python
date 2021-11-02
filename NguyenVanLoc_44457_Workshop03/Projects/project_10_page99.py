"""
Author: Nguyen Van Loc
Date: 19/09/2021

program that takes the purchase price as input

"""
#getting purchase price

price=float(input('Enter the purchase price: '))

#declaring needed variables

month_number=1 #month number

int_rate=0.12 #interest rate

down_payment=price*.10 #down payment (10% of price)

monthly_payment=(price-down_payment)*.05 #monthly payement= 5% of price-downpayment

#starting balance owed

current_balance=price-down_payment

#displaying heading. here numbers specify the field width, < means left justification and

# s refers to string type values

print('{:<15s} {:<20s} {:<20s} {:<20s} {:<20s} {:<20s}'.format('Month','Starting Balance','Interest to Pay',

      'Principal to Pay','Payment','Ending Balance'))

#looping until balance become 0

while current_balance>0:

    #checking if current balance is less than monthly payment

    if current_balance<monthly_payment:

        #no interest

        int_amt=0

        #remaining balance as principal

        principal=current_balance

        #remaining balance as payment

        payment=current_balance

        ending_balance=0 #end of loop

    else:

        #otherwise, finding each values

        #interest amount

        int_amt=current_balance*(int_rate/12)

        #principal amount

        principal=monthly_payment-int_amt

        #total payment

        payment=int_amt+principal

        #ending balance

        ending_balance=current_balance-principal

    #displaying everything. here d refers to decimal, f refers to floating point numbers

    #.2 refers to the floating point number's precision

    print('{:<15d} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f}'.format(month_number, current_balance, int_amt,

                                                                             principal, payment, ending_balance))

    #updating current balance and month number

    current_balance=ending_balance

    month_number+=1