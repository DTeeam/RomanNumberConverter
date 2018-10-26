for number in range(1, 1001, 1):
	romanNumber = ""
	print(number)

	while number > 0:
		if(number >= 1000):
			romanNumber += "M"
			number -= 1000
			continue
		if(number >= 900):
			romanNumber += "CM"
			number -= 900
			continue
		if(number >= 500):
			romanNumber += "D"
			number -= 500
			continue
		if(number >= 400):
			romanNumber += "CD"
			number -= 400
			continue
		if(number >= 100):
			romanNumber += "C"
			number -= 100
			continue
		if(number >= 90):
			romanNumber += "XC"
			number -= 90
			continue
		if(number >= 50):
			romanNumber += "L"
			number -= 50
			continue
		if(number >= 40):
			romanNumber += "XL"
			number -= 40
			continue
		if(number >= 10):
			romanNumber += "X"
			number -= 10
			continue
		if(number >= 9):
			romanNumber += "IX"
			number -= 9
			continue
		if(number >= 5):
			romanNumber += "V"
			number -= 5
			continue
		if(number >= 4):
			romanNumber += "IV"
			number -=4
			continue
		if(number >= 1):
			romanNumber +="I"
			number -=1
			continue		
	print(romanNumber)
	print()

