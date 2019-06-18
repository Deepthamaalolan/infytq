def check_palindrome(word):
    word1=word.lower()
    if word1 == word1[::-1]:
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
