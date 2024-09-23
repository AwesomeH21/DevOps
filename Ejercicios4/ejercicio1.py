nums = []
for i in range(0,10,1):
    num = int(input( (f"Ingrese el número {i+1}: ") ))
    nums. append(num)
mAx = max(nums)
mIn = min(nums)

print(f"El mayor número es: {mAx}")
print(f"El menor número es: {mIn}")
