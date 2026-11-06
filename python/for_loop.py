#program to count the frequency of a charachter
'''s=input("enter a string:")
ch=input("enter a character to count:")
count=0
for i in s:
    if ch==i:
        count+=1
print(f'frequency of{ch} in{s} is:{count}')'''

#program to find the length of a collection without using len()
'''s=eval(input("enter the collection:"))
count=0
for i in s:
    count+=1
print("length of the collection:",count)'''



#wap to extract all the key value pairs from the dictionery
#only if the keys are string and values are integers
'''d=eval(input("enter the collection:"))
out={}
for i in d:
    if type(i)==str:
        if type(d[i])==int:
            out[i]=d[i]
print(out)'''

#wap to get the following output usig len ()
#s='power star'
#out={power:5,star:4}
s=input("enter the string")
out={}
word=''
l=0
for i in s:
    if i!=' ':
        word=word+i
        l+=1
    else:
        out[word]=len(word)
        word=''
        l=0
out[word]=l
print(out)
            
    
