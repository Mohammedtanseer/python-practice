bill = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Number of people: "))

tip_amount = (bill * tip_percent) / 100
total  = bill + tip_amount
per_person = total / people

print("--- Bill Summary ---")
print(f"Tip:  {tip_amount:.2f}")
print(f"Total: {total:.2f}")
print(f"Per person: {per_person:.2f}")

