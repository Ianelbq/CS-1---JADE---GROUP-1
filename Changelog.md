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

print("\nYour General Weighted Average is:")


if grade >= 96 and grade <= 100:
    print("GWA: 1.00")
    print("Status: EXCELLENT")
elif grade >= 90 and grade <= 95:
    print("GWA: 1.25")
    print("Status: VERY GOOD")
elif grade >= 85 and grade <= 89:
    print("GWA: 1.50")
    print("Status: VERY GOOD")
elif grade >= 78 and grade <= 84:
    print("GWA: 1.75")
    print("Status: GOOD")
elif grade >= 72 and grade <= 78:
    print("GWA: 2.00")
    print("Status: GOOD")
elif grade >= 66 and grade <= 72:
    print("GWA: 2.25")
    print("Status: SATISFACTORY")
