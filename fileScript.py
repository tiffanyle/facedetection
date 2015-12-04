#f = open('fold_0_data.txt', 'r')
count = 0

with open('fold_0_data.txt','r') as f:
    content = f.readlines()
    
print 'length', len(content)
for i in range(0,len(content)+1):
    print "content", type(content[i])
    arr = content[i].split()
    #print "arr", arr
    with open("facePaths.txt", "a") as myfile:
        string = 'faces/'
        string+=arr[0]
        #print arr[0]
        string+='/'
        string+='coarse_tilt_aligned_face.'
        string+=arr[2]
        string+='.'
        string+=arr[1]
        string+='\n'
        #print string
        myfile.write(string)
        
    #if count < 10:
        #print i
 #       count+=1



#userid/course_tilt_aligned_face.[faceid].[originalimage]
