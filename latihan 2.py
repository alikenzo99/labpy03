#find and show the maximum value
#the list
list1 = []
while True : #always want you to input
        a=int(input("masukan bilangan : "))
        list1.append(a)
        if a == 0: #if 0 will stop
            break
print("nilai terbesar adalah: ",max(list1)) #showing
