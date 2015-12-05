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
def getBucket(x):
    if x >=0 and x<4:
        return 1
    elif x>=4 and x<8:
        return 2
    elif x>=8 and x<15:
        return 3
    elif x>=15 and x<25:
        return 4
    elif x>=25 and x<38:
        return 5
    elif x>=38 and x<48:
        return 6
    elif x>=48 and x<60:
        return 7
    else:
        return 8


print 'length', len(content)
for i in range(0,len(content)+1):
    print "content", type(content[i])
    arr = content[i].split()
    count = 0
    #print "arr", arr
    with open("facePaths-TrainLabels1.txt", "a") as myfile, open('facePaths-AgeLabels1.txt', 'a') as agefile:
        string = ''
        if arr[5]=='m' or arr[4] == 'm' and arr[3] != 'None':
            label='1'+'\n'
            myfile.write(label)

            agestring = ''
            if arr[3]=='(0,':
                agestring = '1'+'\n'
            elif arr[3] =='(4,':
                agestring= '2'+'\n'
            elif arr[3] =='(8,':
                agestring= '3'+'\n'
            elif arr[3] =='(15,':
                agestring= '4'+'\n'
            elif arr[3] =='(25,':
                agestring= '5'+'\n'
            elif arr[3] =='(38,':
                agestring= '6'+'\n'
            elif arr[3] =='(48,':
                agestring= '7'+'\n'
            elif arr[3] =='(60,':
                agestring='8'+'\n'
            else:
                try:
                    int(arr[3])
                    bucket = getBucket(int(arr[3]))
                    agestring = str(bucket) + '\n'
                except:
                    agestring='5'+'\n'
 
            agefile.write(agestring)
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
        elif arr[5] == 'f' or arr[4] == 'f' and arr[3] != 'None':
            label='2'+'\n'
            myfile.write(label)

            agestring = ''
            if arr[3]=='(0,':
                agestring = '1'+'\n'
            elif arr[3] =='(4,':
                agestring= '2'+'\n'
            elif arr[3] =='(8,':
                agestring= '3'+'\n'
            elif arr[3] =='(15,':
                agestring= '4'+'\n'
            elif arr[3] =='(25,':
                agestring= '5'+'\n'
            elif arr[3] =='(38,':
                agestring= '6'+'\n'
            elif arr[3] =='(48,':
                agestring= '7'+'\n'
            elif arr[3] =='(60,':
                agestring='8'+'\n'
            else:
                bucket = getBucket(int(arr[3]))
                agestring = str(bucket) + '\n'
            agefile.write(agestring)
            
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
