import time
print("NUMBER THINKING GO")
time.sleep(3)
print("You have to think of a number. I will guess it. Enter h for a higher number, l for a lower one and c for a correct guess.")
time.sleep(3)
while True:
	upper = int(input("Enter your number limit: "))
	time.sleep(3)
	print("My guesses start here:")
	time.sleep(1) 
	x = 0
	lower = 1
	s = round((lower + upper) / 2)
	print(s)
	while s != "c":
		time.sleep(1)
		y = input("Is your number higher, lower or is my guess correct? ")
		if y == "h":
			lower = s + 1
		if y == "l":
			upper = s - 1
		x = x + 1
		s = round((lower + upper) / 2)
		print(s)
		if y == "c":
			print(f"Yay! I guessed correctly in {x} tries!")
			break