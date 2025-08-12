str1 = "CADBZABCD"

def longest_substring(str1):
    left,right=0,0
    mydict={}
    maxi=0
    while(right<len(str1)):

        if(str1[right] in mydict ):
            left=max(left,mydict[str1[right]]+1)

        maxi=max(maxi,(right-left)+1)
        mydict[str1[right]]=right
        right+=1
    return maxi

print(longest_substring(str1))