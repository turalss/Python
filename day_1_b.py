# 1.	Numbers: Example code to add two numbers 50+50 and 100-10 and print it.
a = 50
a += 50
b = 100
b -= 10

print(a)
print(b)

# 2. Calculate

# 30+*6
c = (6/100)* 30
print(c)

# 6^6

d = 6**6
print(d)

# 6+6+6+6+6+6
e = 6+6+6+6+6+6
print(c)

# 4. Below is a mathematical calculation exercise:

def mortgage_calculator(total_amount, interest, months):
    interest = interest / 100
    monthly_interest = interest/12
    numerator = monthly_interest*((1+monthly_interest)**months)
    denominator = (1 + monthly_interest)**months - 1
    payment = float("{0:.2f}".format(total_amount * numerator/denominator ))
    return(payment)

print(mortgage_calculator(800000, 6, 103))









