# nested if wap to check vowels or consonent
'''ch=input("enter a character:")
if 'A'<=ch<='Z' or 'a'<=ch<='z':
    if ch in 'aeiouAEIOU':
        print("vowel")
    else:
        print("consonent")
else:
    print("it is not a alphabet")'''



#wap to print the the middle value of a list if it palindrome string
'''l=eval(input("enter list:"))
if len(l)%2!=0:
    
    if (type(l[len(l)//2])==type(str)):
        
        print("string is present cond2")
        
        if(type(l[len(l)//2])==[len(l)//2][::-1]):
            
            print("it is palindrome cond3")
else:
     print("it is not a palindrome cond3") OR '''

'''l=eval(input("enter list:"))
if len(l)%2!=0:
    mid=l[len(l)//2]
    if type(mid)==str:
        if mid==mid[::-1]:
            print('the list contains a palindrome str as mid value')
        else:
            print(mid,'is not a palindrome')
    else:
        print(mid,'is not a string')
else:
    print('the list does not have middle value') '''

#wap to check reverse of a string ,string starts with vowel,ends with special character
l=input("enter a string:")
if l[0] in 'aeiouAEIOU':
    if not ('A'<=l[-1]<='Z') and not('a'<=l[-1]<='z') and  not('0'<=l[-1]<='9'):
        print(s[::-1],'starts with vowel and ends with special char')
    else:
        print('not a special char')
else:
    print('not start with a vowel')
        

    
   
    
