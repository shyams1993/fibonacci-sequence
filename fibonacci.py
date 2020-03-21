number=int(input("Enter a number: "))	#Get Input from the user (How many numbers from fibonacci series need to be printed)
a,b=0,1									#Initialize a & b to 0 & 1
print(" "+str(a),'\n',b)				#Print both 0,1
for each in range(a,number):			#start a for loop with a and the input number as range
	c=a+b 								#c=a+b
	print(" "+str(c))					#print c
	a,b=b,c								#swap a,b with b,c and get back in the loop	
