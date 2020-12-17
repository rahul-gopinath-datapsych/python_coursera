'''
Requirement: Provided the list of numbers. calculate statistics, such as total Sum, total Count of numbers,
Mean, Duplicate count in the list, smallest and largest number.
'''

# list of numbers used in testing
num_list=[14,67,84,4354,3453,22,3,444,52,9,435,84,9,99,22,53,15,12,14,4354]

# Intializing few variables to calc sum and count
count=0
sum=0
largest_number=None
smallest_number=None
#sorting list in ascending
num_list.sort()

# intiating fixed iteration to calc basic stats
for i in num_list:
    count=count+1
    sum=sum+i
    if largest_number is None:
        largest_number=i
    elif i>largest_number:
        largest_number=i
    if smallest_number is None:
        smallest_number=i
    elif i<smallest_number:
        smallest_number=i
#calc mean for the list of numbers
mean=sum/count

# Taking count of dupliate numbers in the list
dup_count=0
i=0
while i+1<len(num_list):
    if num_list[i]==num_list[i+1]:
        dup_count+=1
        i+=1
    else:
        i+=1
    

print("Basic stats for the numbers provided in the list",num_list,"as below")
print('''Total Sum: {sum}
Total Number Count: {count}
Mean:{mean} 
Duplicate Count: {dup_count}
Largest Number: {largest_number}
Smallest Number: {smallest_number}
'''.format(sum=sum,mean=mean,count=count,dup_count=dup_count,largest_number=largest_number,smallest_number=smallest_number))

