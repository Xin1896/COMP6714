import copy
splits= []
q = ['A','B','C']
list1 = [['A A','A B','A C'],['A B']]
for i in list1:
    print(i)
    n = []
    q_list = copy.deepcopy(q)
    for j in i:
        print(j)
        
        n += j.split()
    print(n)
    for k in n:
        if k in q_list:
            q_list.remove(k)
            #print(q)
        else:
            #print(j)
            break
    else:
        #print(q_list)
        splits.append((i,q_list))
print(splits)
        