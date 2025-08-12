word1 = ""

def is_palindrome(word_to_check):
    if(len(word_to_check)==0):
        return False
    i,j=0,len(word_to_check)-1
    while(i<j):
        if(word_to_check[i]!=word_to_check[j]):
            return False
        i+=1
        j-=1
    return True
print(is_palindrome(word1))