#print(i)

def count(list_of_num):
    even = 0
    odd = 0

    for i in list_of_num:
        if i % 2 ==0:
            even +=1
        else:
            odd +=1
    return even, odd

list_of_num = [32,21, 64, 100,13]

even,odd = count(list_of_num) 
print(even)
print(odd)