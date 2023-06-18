#Reverse digits
# Input: 200
# Output: 2
# Explanation: By reversing the digts of 
# number, number will change into 2

n = 7006 # do not write this line when code run on gfg
num = str(n)
nm = num[::-1]
mo =""
iszero = True
for x in nm:
    if x == '0' and iszero == True:
        pass
    if x > '0' or iszero == False:
        iszero = False
        mo += x
fina=int(mo)
print(fina)
