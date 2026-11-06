#wap to get the following output
#s=['jiocinema.com','file.py','web.html','amazon.com','www.org']
#out=['com','py','html','org']

'''s=['jiocinema.com','file.py','web.html','amazon.com','www.org']
out=[]
for i in s:
    a=i.split('.')
    if a[1] not in out:
       out.append(a[1])
print(out)'''


#wap to get the following output
'''n='push maadi khushi padi'
words=n.split()
res={}
for word in words:
    if len(word)%2==0:
        res[word]=word[0]+word[-1]
    else:
        res[word]=word[len(word)//2]
print(res)'''

#longest word
'''s='push maaadi khushi padi'
longest_word=''
for word in s.split():
    if len(word)>len(longest_word):
        longest_word=word
print(longest_word)'''

#in='10100011231' reverse 0->1,1->0
'''s='10100011231'
out=''
for i in s:
    if i=='1':
        out+='0'
    elif i=='0':
        out+='1'
print(out)'''

#s=['jiocinema.com','file.py','web.html','amazon.com','www.org','python.py']
#out=['com':['jio',amazon'],'py':['file','python']'org':['www']
'''s=['jiocinema.com','file.py','web.html','amazon.com','www.org','python.py']
res={}
for i in s:
    s=i.split('.')
    if s[1] not in res:
        res[s[1]]=[s[0]]
    else:
        res[s[1]].append(s[0])
print(res)'''

#wap to find the graetest number preesent in a list of integers
'''l=[12,34,123,56,78,90,456,456,23,67,285]
greatest_num=0
for i in l:
    if i>greatest_num:
        greatest_num=i
print(greatest_num)
#important
greatest=0
sec_greatest=0
for i in l:
     if i>greatest:
         sec_greatest=greatest
         greatest=i
     elif i>sec_greatest:
         second=i
print(greatest,sec_greatest)'''

# 108.wap to get the following output
#in='abacbaacc'
#output in dictionery
s=('abacbaacc')
'''out={}
for i  in s:
     if i not in out:
          out[i]=1
     else:
          out[i]+=1
print(out)'''

for i in set(s):
     d[i]=s.count(i)
print(d)



    
        


    


    
    
