
#Sum all in the list

def sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
numbers = list(map(int,input().split()))
print(sum(numbers))
  
