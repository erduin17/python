#list_example_0.py Em
filelist1 = ["img_001.png","img_007.png","img_002.png","img_009.png"]
filelist2 = ["img-001.png","img-002.png","img-003.png","img-004.png"]

for i in range (0, 4):
    #print(filelist1[i],filelist2[i])
    print ("mv "+filelist1[i]+ " "+filelist2[i]+";")
