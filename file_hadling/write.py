#file handling
##read
##write
##udate
##
##open()-->to access the file
##var=open('file.exe','mode')---.mode-->which specify the operations.


#write
'''f=open('file1.txt','w')
f.write('hello everyone\n')#single line data
f.writelines(['good afternoon\n','had your launch\n','hey everyone\n','this is file handling\n'])
f.write('have a great day\n')
f.close()'''

#read
try:
    f=open('file1.txt','r')
    #data=f.readline()#one line or reads line by line
    #data=f.read()#complete file it will read
    data=f.readlines()#reads in the form of list values
except:
    print('file is not present')
else:
    print(data)
    
              
