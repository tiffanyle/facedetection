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
    #print "arr", arr
    with open("facePaths-TestLabels1.txt", "a") as myfile:
        string = ''
        if arr[5]=='m':
            string='1'+'\n'
        elif arr[5] == 'f':
            string='2'+'\n'
        else:
            pass
        
        #print string
        myfile.write(string)
