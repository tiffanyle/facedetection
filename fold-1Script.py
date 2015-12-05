count = 0

with open('fold_1_data.txt','r') as f:
    content = f.readlines()
'''
print 'length', len(content)
for i in range(0,len(content)+1):
    print "content", type(content[i])
    arr = content[i].split()
    #print "arr", arr
    with open("facePaths-Test1.txt", "a") as myfile:
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
'''

print 'length', len(content)
for i in range(0,len(content)+1):
    print "content", type(content[i])
    arr = content[i].split()
    count = 0
    #print "arr", arr
    with open("facePaths-TrainLabels1.txt", "a") as myfile:
        string = ''
        if arr[5]=='m' or arr[4] == 'm':
            label='1'+'\n'
            myfile.write(label)
            with open("facePaths-Train1.txt", "a") as myfile2:
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
                myfile2.write(string)
        elif arr[5] == 'f' or arr[4] == 'f':
            label='2'+'\n'
            myfile.write(label)
            with open("facePaths-Train1.txt", "a") as myfile2:
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
                myfile2.write(string)
        else:
            count+=1
            print "COUNT**", count
            pass
        
        #print string
 
print "UNACCOUNTED FOR", count
