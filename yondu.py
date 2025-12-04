# yondu.py

# Ask the user for the number of pirates and the total units
num_pirates = int(input("How many pirates: "))
num_units = float(input("How many units: "))

# There are only two special pirates: Yondu and Peter
# Everyone else gets 3 units right away
regular_crew = num_pirates - 2
initial_cut = round(regular_crew * 3, 2)

# Subtract the 3-unit gifts from the total
remaining = round(num_units - initial_cut, 2)

# Yondu takes 13% of what is left
yondu_share = round(remaining * 0.13, 2)
after_yondu = round(remaining - yondu_share, 2)

# Peter takes 11% of what is left after Yondu
peter_share = round(after_yondu * 0.11, 2)
after_peter = round(after_yondu - peter_share, 2)

# Whatever is still left gets divided evenly among ALL pirates
equal_split = round(after_peter / num_pirates, 2)

# Final amounts each person receives
yondu_total = round(yondu_share + equal_split, 2)
peter_total = round(peter_share + equal_split, 2)
crew_total = round(3 + equal_split, 2)

# Print results
print(f"Yondu's share: {yondu_total:.2f}")
print(f"Peter's share: {peter_total:.2f}")
print(f"Crew's share: {crew_total:.2f}")
