print(" *** Digit count and Summation ***")
innum=input("Enter an integer : ")
innum=int(innum)
lennum=len(str(innum))
innum=str(innum)
i=0
sumnum=0

while i< len(str(innum)):
    sumnum= sumnum+int(innum[i])
    i=i+1
formatted_num = format(int(innum), ",")
print(f"number = {formatted_num}")

print(f"Total digits are:  {lennum}")
print(f"Summation = {sumnum}")