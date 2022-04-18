def add(*nums):
    total = 0
    for number in nums:
        total = total + number

    return total

print(add(1,2,3,4,5,6,7,8,1))

def calc(**kwargs):
