R1 = 3.96    # Rate (10 year)
R2 = 4.32    # Rate (20 year)
N1 = 10   # of years (10 year)
N2 = 20   # of years (20 year)
K = 33000000000  # Principal
growth1 = K*((1+(R1/100))**N1)
growth2 = K*((1+(R2/100))**N2)
ten_year_final = growth1
twenty_year_final = growth2
print("10 Year Final Profit:", "$",ten_year_final)
print("20 Year Final Profit:", "$",twenty_year_final)
