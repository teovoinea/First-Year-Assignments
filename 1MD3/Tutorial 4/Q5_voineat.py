def main():
    sentence = input("Please enter a sentence")
    print(isPalindrome(sentence))
def onlyLetters(s):
    #remove upper case letters
    s = s.lower()
    #remove spaces to handle sentences
    s = s.split()
    #create new string ns, to store s as a string instead of a list of strings
    ns = ""
    #concatenate all strings in s to ns
    for w in s:
        ns = ns + w
    #set s to ns so I don't need to change any code from original function
    #^above step not necessary, just being lazy.....
    return ns
def isPalindrome(s):
    s = onlyLetters(s)
    # uses negative string index
    for i in range(len(s)//2):
        if s[i] != s[-i-1]: return False
    return True
main()
