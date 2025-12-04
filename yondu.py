# yondu.py

# Ask for inputs
num_pirates = int(input("How many pirates: "))
num_units = float(input("How many units: "))

# Regular crew (excluding Yondu and Peter)
crew_only = num_pirates - 2

# Each regular crew member gets 3 units 
initial_cut = 3 * crew_only

# Yondu takes 13% of the TOTAL units
yondu_share = round(num_units * 0.13, 2)

# Peter gets 11% of what's left after Yondu's cut
after_yondu = num_units - yondu_share
peter_share = round(after_yondu * 0.11,2)

# Leftover after crew gifts + Yondu + Peter
leftover = num_units - initial_cut - yondu_share- peter_share

# Crew share per person (including Yondu + Peter + all crew)
crew_share = round(leftover / num_pirates, 2)

# Output results
print(f"Yondu's share: {yondu_share}")
print(f"Peter's share: {peter_share}")
print(f"Crew's share: {crew_share}")
