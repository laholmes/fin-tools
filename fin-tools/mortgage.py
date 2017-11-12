import pandas as pd


def amortization_table(loan_amount: float, rate: float, monthly_payment: float = 0.):
    table = []
    amount_outstanding = loan_amount
    while amount_outstanding > 0:
        if amount_outstanding == loan_amount:
            table.append(( 
                loan_amount, 
                monthly_payment, 
                loan_amount*(((1+rate)**(1/12)) - 1), 
                monthly_payment-loan_amount*(((1+rate)**(1/12)) - 1)
            ))
            amount_outstanding = loan_amount - monthly_payment-loan_amount*(((1+rate)**(1/12)) - 1)
        else:
            amount_outstanding = table[-1][0] - table[-1][3]
            if amount_outstanding > 0:
                payment = monthly_payment if amount_outstanding > monthly_payment else amount_outstanding*(((1+rate)**(1/12)))

                table.append((
                    amount_outstanding,
                    payment,
                    amount_outstanding*(((1+rate)**(1/12)) - 1),
                    payment-amount_outstanding*(((1+rate)**(1/12)) - 1)
                ))

    return pd.DataFrame(table, columns=['outstanding', 'repayment', 'interest', 'capital_repaid'])


