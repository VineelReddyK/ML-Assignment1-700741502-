n=int((input("Enter the number of students")))
list= []
kgs = []

for i in range(0,n):
    lbs = int(input())
    list.append(lbs)
length = len(list)
#converting lbs to kgs using separate loop
# standard 1 lB = kg/2.2046
for i in range(length):
    wt = list[i]/2.2046
    kgs.append(wt)
#rounding values to 2 decimal places
round_val = [round(num,2) for num in kgs]
#kgs = '%.2f' kgs
print(round_val)
