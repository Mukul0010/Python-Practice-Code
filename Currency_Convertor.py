# Write a program to convert the currency


# Currency Converter Program

with open('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}

for line in lines:
    line = line.strip()
    if not line:   # skip blank lines
        continue

    # split on any whitespace (handles tabs + spaces)
    parsed = line.split()

    # currency name is everything except last two numbers
    currency_name = " ".join(parsed[:-2])
    to_inr = float(parsed[-2])   # 1 foreign currency = ? INR
    from_inr = float(parsed[-1])  # 1 INR = ? foreign currency

    currencyDict[currency_name] = (to_inr, from_inr)

# ---- User Input ----
amount = float(input("Enter amount in INR:\n"))
print("\nAvailable currencies:\n")
for item in currencyDict.keys():
    print(item)

currency = input("\nPlease enter one of the above currency names:\n")

if currency in currencyDict:
    to_inr, from_inr = currencyDict[currency]
    converted = amount * from_inr   # INR → Foreign currency
    print(f"\n{amount} INR = {converted:.4f} {currency}")
else:
    print("❌ Currency not found in the list.")
