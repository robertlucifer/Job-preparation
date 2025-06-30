# hardcode method
def valid_palindrome(value):
    result=''
    for x in value:
        if x.isalnum():
            result+=x
    return value==result

# Two Pointer method Worst Case
def valid_palindrome2(value):
    l=0
    r=len(value) -1

    while l < r:
        if value[l] != value[r]:
            return False

        l+=1
        r-=1

    return True

#Two Pointer best case

def valid_palindrome3(question):


    def isalnum(value):
        return (ord("A") <= ord(value) <= ord("Z") or
                ord("a") <= ord(value) <= ord("z") or
                ord("0") <= ord(value) <= ord("9"))
question = "A man, a plan, a canal: Panama"
print(valid_palindrome(question))
print(valid_palindrome2(question))