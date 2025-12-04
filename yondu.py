# yondu.py

# Ask for inputs
num_pirates = int(input("How many pirates: "))
num_units = float(input("How many units: "))

# Each pirate gets 3 units at the start
initial_cut = 3 * num_pirates
remaining_units = num_units - initial_cut

# Yondu takes 13% of the remaining
yondu_share = remaining_units * 0.13
yondu_share = round(yondu_share, 2)

# Remaining after Yondu
left_after_yondu = remaining_units - yondu_share

# Peter gets 11% of what's left
peter_share = left_after_yondu * 0.11
peter_share = round(peter_share, 2)

# Remaining after Peter
left_after_peter = left_after_yondu - peter_share

# Crew share per person (including Yondu + Peter + all pirates)
crew_share = left_after_peter / num_pirates
crew_share = round(crew_share, 2)

# Output results
print(f"Yondu's share: {yondu_share}")
print(f"Peter's share: {peter_share}")
print(f"Crew's share: {crew_share}")
