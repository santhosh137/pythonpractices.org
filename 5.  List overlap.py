a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]


#list_comp=[c.append(b[x]) if b[x]==(a[i] for i in range(len(a))) for x in range(len(b)) else pass]
#print (list_comp)


# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             if b[j] in c:
#                 pass
#             else:
#                 c.append(b[j])
#
#
# print (c)



#list_comp= [c.append(b[i]) if a[k]==b[i] for k in range(len(a)) for i in range(len(b)) else pass]
#list_comp=[print (a[k],b[i]) for k in range(len(a)) for i in range(len(b))]
def list_overlap(a,b):
    list_comp= ["pass" if b[j] in c  else c.append(a[i]) if a[i]==b[j] else "pass" for i in range(len(a)) for j in range(len(b)) ]

    print (c)

if __name__== "__main__":
    list_overlap(a, b)








