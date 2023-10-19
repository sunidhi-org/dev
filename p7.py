# Function to convert Binary number to Decimal number
def binaryToDecimal(n):
    return int(n,2)
# Function to convert Decimal number To Binary number def
def decimalToBinary(n):
    if(n > 1):
# divide with integral result
# (discard remainder)
        decimalToBinary(n//2)
    print(n%2, end='')
myinput = input("Enter the bunary value: ")
oncecomp = ""
for i in myinput:
    if i == "0":
        oncecomp = oncecomp + "1"
    else:
        oncecomp = oncecomp + "0"

print("1's Compliment of the given binary number is:", oncecomp ) 
decnumber= binaryToDecimal(oncecomp)
decnumber += 1
print("2's Compliment of the given binary number is: ", end='' )
decimalToBinary(decnumber)