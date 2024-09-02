#longest palindrome  substring from given string
text="RACECAR"
# A
# R
# C
# E
# CEC
# RACECAR
# ACECA
# length=len(text)

# for i in range(0,len(text)):
#     left=i
#     right=i
#     while(left>=0 and right<len(text) and text[left]==text[right]):
#         current_palindrome=text[left:right+1]
#         print(current_palindrome)
#         left=left-1
#         right=right+1
        

#prnt longest palindrome
text="MADAMAM"

length=len(text)

longest_palindrome=""

for i in range(0,length):

    left=i

    right=i

    while( left>=0 and right<len(text)and text[left]==text[right]):

        current_palindrome_text=text[left:right+1]

        if len(current_palindrome_text)>len(longest_palindrome):

            longest_palindrome =current_palindrome_text

        left=left-1

        right=right+1

print(longest_palindrome)        