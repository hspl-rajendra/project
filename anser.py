
numbers = [0,1,2,3,4,5,6,7,50,51,52,53,55,58]
print("\nList Odd numbers:")
oddNumbers = list(filter(lambda x: x%2 != 0, numbers))
print(oddNumbers)
