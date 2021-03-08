file = open("Test1.txt",'w')
sample = ['1','2','3','4','5']
for i in sample:
    file.write("{}\n".format(i))
