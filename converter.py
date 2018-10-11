print("How many kilometers did you cycle today?")
kms = input()
print("Okay you said " + kms + "km")
miles = float(kms) / 1.60934
print(f"Your {kms} km ride is equal to {round(miles, 2)} miles")
