import re
import random

print("\nPASSWORD GENERATOR")
print("-----")

min_char = 0
while min_char < 1:
	length = input("\nMinimum Password Length: ")
	if re.search(r'\d', length):
		min_char = int(length)
		
		if min_char < 1:
			print("Minimum Length Must be Greater Than 0. Please Try Again.")
	else:
		print("Invalid Input. Please Try Again.")

max_char = 0
while max_char < min_char:
	length = input("\nMaximum Password Length: ")
	if re.search(r'\d', length):
		max_char = int(length)
		
		if max_char < min_char:
			print(f"Maximum Length Must be Greater Than or Equal To {min_char}. Please Try Again.")
	else:
		print("Invalid Input. Please Try Again.")

pass_len = random.randrange(min_char, max_char+1)

pass_str = 0
while pass_str < 1 or pass_str > 4:
	strength = input("\nPassword Strength (1-4): ")
	if re.search(r'\d', length):
		pass_str = int(strength)
		
		if pass_str < 1 or pass_str > 4:
			print("Invalid Strength Level. Please Try Again.")
	else:
		print("Invalid Input. Please Try Again.")

chars = "abcdefghijkmnpqrstuxyz"
if pass_str > 1:
	chars = chars + "ABCDEFGHJKMNPQRSTXYZ"
if pass_str > 2:
	chars = chars + "23456789"
if pass_str > 3:
	chars = chars + "@#$_&-+()/*!?^|{}[]"

password = ""
for i in range(0, pass_len):
    n = random.randrange(0, len(chars))
    
    password = password + chars[n]

print("\nPassword: " + password)
