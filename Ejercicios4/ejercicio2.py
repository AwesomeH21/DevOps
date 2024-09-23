lis1=[]
lis2=[]
for i in range(0,5,1):
    agg=int(input("Dame un número x "))
    lis1.append(agg)
for i in range(0,5,1):
    agg=int(input("Dame un número y "))
    lis2.append(agg)
diff=[agg for agg in lis1 if agg not in lis2]

print(f"Elementos de la primera lista que no están en la segunda {diff}")