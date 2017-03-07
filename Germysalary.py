#This program will convert an hourly pay rate into an annual salary
#This program assumes a 40 hour work week paid for 52 weeks of the year (in USD)
hours=40
aweeks=52
query=raw_input("Please enter your hourly pay rate: $")
rate=float(query)
salary=hours*aweeks*rate
print "Your salary is $","%.2f" % salary
