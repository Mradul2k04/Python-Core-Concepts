#TASK -1  E-commerce

def calculate_total(items,tax_rate):
    final_amt=0
    if tax_rate<0 or tax_rate>1:
        raise ValueError("Tax rate must be in range")
    for price in items:
        if price<0:
            raise ValueError("Items price can not be negative")
        else:
            final_amt+=price+(price*(tax_rate/100))
    return round(final_amt,2)