ans = True
while ans:
	print("""
	Välj svårighetsgrad:
	
	1. EZ
	2. Standard
	3. Pro
	""")
	
	ans = input("")
	if ans == "1":
		import random
		siffra = random.randint(1,10)
		
		print("Gissa på en siffra mellan 1 och 10.")
		
		gissning = int(input())
		
		if gissning == siffra:
			print("Rätt gissat!")
		elif gissning < siffra:
			print("För litet. Gissa på ett större tal.")
		elif gissning > siffra:
			print("För stort. Gissa på ett mindre tal.")
		
	elif ans == "2":
		import random
		siffra = random.randint(1,100)
		
		print("Gissa på en siffra mellan 1 och 100.")
		
		gissning = int(input())
		
		if gissning == siffra:
			print("Rätt gissat!")
		elif gissning < siffra:
			print("För litet. Gissa på ett större tal.")
		elif gissning > siffra:
			print("För stort. Gissa på ett mindre tal.")
	
	elif ans == "3":
		import random
		siffra = random.randint(1,1000)
		
		print("Gissa på en siffra mellan 1 och 1000.")
		
		gissning = int(input())
		
		if gissning == siffra:
			print("Rätt gissat!")
		elif gissning < siffra:
			print("För litet. Gissa på ett större tal.")
		elif gissning > siffra:
			print("För stort. Gissa på ett mindre tal.")
		
		
		
		
		
input()
