price=eval(input("Enter the regular price="))
fresh=int(input("Enter the no/- of fresh loaves purchased="))
old=int(input("Enter the no/- of old loaves purchased="))
fresh_amt=fresh*price
old_amt=old*(price*(40/100))
total=fresh_amt+old_amt
print("Regular price= %.2f" % price)
print("Amount for new loaves= %.2f" % fresh_amt)
print("Amount for old loaves= %.2f" % old_amt)
print("Total price= %.2f" % total)
