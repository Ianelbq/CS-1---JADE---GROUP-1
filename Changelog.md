q1 = float(input("Enter First Quarter (Q1): "))
print("Your First Quarter is:", round(q1,2))


q2 = float(input("Enter Second Quarter (Q2): "))
q2f = round(((q1 + (2 * q2)) / 3),2)
print("Your Second Quarter is:", q2f)

q3 = float(input("Enter Third Quarter (Q3): "))
q3f = round(((q2f + (2 * q3)) / 3),2)
print("Your Third Quarter is:", q3f)

q4 = float(input("Enter Fourth Quarter (Q4): "))
q4f = round(((q3f + (2 * q4)) / 3),2)
print("Your Fourth Quarter is:", q4f)

grade =q4f
