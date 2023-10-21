print(11*2)



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1 : : 2])



lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

res_lst = []
for i in range(0, len(lst1)):
    res_lst.append(lst1[i] + lst2[i])
print(res_lst)
