tmbh=0 #var for total
a=0 #var for num
mdl=100000000 #frst
grwth = [int(0), int(0), int(mdl)*.1, int(mdl)*.1, int(mdl)*.5, int(mdl)*.5, int(mdl)*.5, int(mdl)*.2]
for i in grwth:
    tmbh = tmbh+i
    a+=1
    print("laba bulan ke :",a," sebesar ",i,)
print("total laba adalah: ",tmbh)
