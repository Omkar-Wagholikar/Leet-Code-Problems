# https://leetcode.com/problems/longest-palindromic-substring/
def checkPalindrome(at, inp):
    counta, countb = 0, 0
    #  # Dobule middle
    for i in range(0,len(inp)):
        if at-i <0 or at+i+1 >= len(inp):
            # print("Loop exceeded")
            break
        if inp[at+i+1] == inp[at-i]:
            counta+=1
            # print(at-i, at+i+1)
            # print(inp[at-i:at+i+2])
            counta = i
        else:
            # print("Breaking loop")
            break
    # print(inp[at-counta:at+counta+2], counta)

    #  # Single middle

    for i in range(0,len(inp)):
        if at-i <0 or at+i >= len(inp):
            # print("Loop exceeded")
            break
        if inp[at+i] == inp[at-i]:
            countb = i
            # print(at-i, at+i)
            # print(inp[at-i:at+i+1])
        else:
            # print("Breaking loop")
            break
    # print(countb)
    # print(inp[at-countb:at+countb+1], countb)

    if counta > countb:
        return inp[at-counta:at+counta+2]
    else:
        return inp[at-countb:at+countb+1]
    

    # return counta

# inp = "aabcbaba"
# inp = "aabccbaba"
inp = "cbbd"
print(checkPalindrome(3, inp))

