#file handling
##read
##write
##update
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
'''try:
    f=open('file1.txt','r')#if dont mention r it will defaultly read the file.we can extract first five chars by using read(5)
    #data=f.readline()#one line or reads line by line
    #data=f.read()#complete file it will read
    data=f.readlines()#reads in the form of list values
except:
    print('file is not present')
else:
    print(data)'''

#read and write w+ r+ a+
'''f=open('file2.txt','w+')
f.writelines(['today is monday\n','hita loves kappe\n','monday is not mondaying\n'])
f.seek(56)#adjust the curser or pointer
print(f.read())
print(f.tell())#it tells current file pointer positioned
f.close()
'''

'''f=open('file2.txt','r+')
f.seek(10)
f.write('amuku')
print(f.read())
f.close()'''

#image file
'''f=open('image1.png','rb')
data=f.read()
f=open('image2.png','wb')
f.write(data)
f.close()'''

#parsing techniques-->using pickle module---> using dumps() and bytes()
#1.dumps()-->it converts original data to bytes
#2.bytes()--->it converts to bytes to original data

'''import pickle
data=[1,2,3,4,5]
c=pickle.dumps(data)
print(data,c)
f=open('file3.txt','wb')
f.write(c)
f.close()'''
#o/p-->[1, 2, 3, 4, 5] b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'

#
'''import pickle
data=[1,2,3,4,5]
c=pickle.dumps(data)
f=open('file3.txt','rb')
c=f.read()
print(c)'''

#csv file--->1.write row-->single row 2.writerows-->multiple rows
'''import csv
f=open('exam.csv','w',newline='')
ob=csv.writer(f)
ob.writerow(['Name','Contact','RollNo','Marks'])
ob.writerows([['Shinchan',9876634567,10,99],['Dora',8753498765,11,25],['Chutki',9867543209,12,98],['Jaggu',7865432109,13,45]])
f.close()'''

#to reaad and get the output in line byline or comma separated data using newline=''
'''import csv
f=open('exam.csv','r')
ob=csv.reader(f)
for i in ob:
        print(i)'''


#f=open('exam.csv','w',newline='')
#output 
'''['Name', 'Contact', 'RollNo', 'Marks']
['Shinchan', '9876634567', '10', '99']
['Dora', '8753498765', '11', '25']
['Chutki', '9867543209', '12', '98']
['Jaggu', '7865432109', '13', '45']'''

#context maanger
'''import csv
f=open('exam.csv','a')
ob=csv.writer(f)
ob.writerow(['dinku',9988876655,14,87])
f.close()'''


#with keyword--->used to close and open the file
'''with open('exam.csv','a')as f:
    ob=csv.writer(f)
    ob.writerow(['chota bheem',9867453265,15,54])'''

























    
              
