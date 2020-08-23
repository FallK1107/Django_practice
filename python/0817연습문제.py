a = ["Life", "is", "too", "short", "you", "need", "python"]

if("wife") in a:
    print("wife")
elif("python") in a and ("you") not in a:
    print("python")
elif("shirt") not in a:
    print("shirt")
elif("need") in a:
    print("need")
else:
    print("none")

i = 0
sum = 0
while(i < 1000):        
    i += 1       
    if(i%3 != 0): continue 
    sum = sum + i     
print(sum)

n = 0
while(n < 5):
	n += 1
	print("*" * n)

for x in range(1,101):
    print(x)

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for b in A:
	sum = sum + b
avg = sum / len(A)
print(avg)
