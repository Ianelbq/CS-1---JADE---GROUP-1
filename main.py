q1 = float(input("Enter First Quarter (Q1): "))
print("Your First Quarter is:", round(q1, 2))

print("\n")

q2 = float(input("Enter Second Quarter (Q2): "))
q2f = round(((q1 + (2 * q2)) / 3), 2)
print("Your Second Quarter is:", q2f)

print("\n")

q3 = float(input("Enter Third Quarter (Q3): "))
q3f = round(((q2f + (2 * q3)) / 3), 2)
print("Your Third Quarter is:", q3f)

print("\n")

q4 = float(input("Enter Fourth Quarter (Q4): "))
q4f = round(((q3f + (2 * q4)) / 3), 2)
print("Your Fourth Quarter is:", q4f)

grade = q4f

print("\nYour General Weighted Average is:", grade)


# STATUS PART
if grade >= 96 and grade <= 100:
    gwa = "1.00"
    status = "EXCELLENT"

elif grade >= 90 and grade <= 95:
    gwa = "1.25"
    status = "VERY GOOD"

elif grade >= 85 and grade <= 89:
    gwa = "1.50"
    status = "VERY GOOD"

elif grade >= 78 and grade <= 84:
    gwa = "1.75"
    status = "GOOD"

elif grade >= 72 and grade <= 78:
    gwa = "2.00"
    status = "GOOD"

elif grade >= 66 and grade <= 72:
    gwa = "2.25"
    status = "SATISFACTORY"

elif grade >= 60 and grade <= 65:
    gwa = "2.50"
    status = "SATISFACTORY"

elif grade >= 55 and grade <= 60:
    gwa = "2.75"
    status = "FAIR"

elif grade >= 50 and grade <= 54:
    gwa = "3.00"
    status = "FAIR"

elif grade >= 40 and grade <= 50:
    gwa = "4.00"
    status = "FAILED ON CONDITION"

else:
    gwa = "5.00"
    status = "FAILED"



print("Equivalent GWA:", gwa)
print("Status:", status)
