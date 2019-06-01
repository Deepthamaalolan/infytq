def check_palindrome(word):
    leng=len(word)
    for i in range(0,(leng//2)+1):
        if(word[i]==word[(leng-1)-i]):
            i=i+1 
        else:
            break
    if(i>leng/2):
        status=True
    else:
        status=False
    return status
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
