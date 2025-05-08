while True:
	print("Check palindrome, \nWanna stop the game? Type quit\n")
	A = input()
	
	if A.lower() == 'quit':
		print("\nGoodbye!\n")
		break

	cleaned = ''.join(char.lower() for char in A if char.isalnum())

	if cleaned == cleaned[::-1]:
		print("it is a palindrome")
		print(f"{cleaned} == {cleaned[::-1]}")
	else:
		print(f"it's not a palindrome {cleaned} is not the same as {cleaned[::-1]}")
	

