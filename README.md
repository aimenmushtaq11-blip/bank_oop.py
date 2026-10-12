# bank_oop.py
The account is a class. __init__ sets up the owner and balance, while deposit(), withdraw() and show() act on it. The methods mutate the object directly instead of returning a new one. The balance is protected by the class, so it can't go negative through normal use. Each account keeps its own separate balance.

Both run the same steps and print 120.00. The difference is only in how the data is stored and changed.
