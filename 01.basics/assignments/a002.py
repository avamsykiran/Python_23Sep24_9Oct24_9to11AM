"""
    An apdcl consumer is billed as per the below tariff
    Category    Consumption Range       Charge/unit
    1           less than 200 units     0.50 INR
                200 to 400              1.10 INR
                401 to 800              2.10 INT
                above 800               3.00 INR
    2           less than 300 units     1.00 INR
                300 to 800              2.10 INR                
                above 800               3.50 INR
    3           less than 800 units     4.50 INR                
                above 800               8.00 INR

    From givne last_month_meter_reading adn current_month_meter_reading
    comput the units_consumed
    Giben the category, fix the rate and compute the payable_amount.
"""    

lmr=456
cmr=789

units = cmr - lmr
print(units)

cat = 2

rate = 0

if cat==1:
    if units<200:
        rate=0.50
    elif units<400:
        rate=1.10
    elif units<800:
        rate=2.10
    else:
        rate=3.00
elif cat==2:
    if units<300:
        rate=1.00
    elif units<800:
        rate=2.10    
    else:
        rate=3.50        
else:
    if units<800:
        rate=4.50    
    else:
        rate=8.00        

print(rate)

amt = units * rate
print(amt)