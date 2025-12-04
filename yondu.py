# yondu.py

# Ask for inputs
num_pirates = int(input("How many pirates: "))
num_units = float(input("How many units: "))

# Regular crew (excluding Yondu and Peter)
crew_only = num_pirates - 2

# Each regular crew member gets 3 units
initial_cut = 3 * crew_only
remaining = num_units - initial_cut

# Yondu takes 13% of the remaining
yondu_share = round(remaining * 0.13, 2)
after_yondu = remaining - yondu_share

# Peter gets 11% of what's left after Yondu
peter_share = round(after_yondu * 0.11, 2)
after_peter = after_yondu - peter_share

# Divide what's left among all pirates (including Yondu + Peter)
crew_share = round(after_peter / num_pirates, 2)

# Output results
print(f"Yondu's share: {yondu_share}")
print(f"Peter's share: {peter_share}")
print(f"Crew's share: {crew_share}")
