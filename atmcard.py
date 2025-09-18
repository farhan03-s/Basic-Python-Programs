atm_card=True
correct_pin=True
acc_locked=False
if atm_card and correct_pin and not acc_locked:
    print("Transaction Successful")
else:
    print("Transaction Failed")
