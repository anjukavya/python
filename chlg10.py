# Compress Consecutive Characters Task: 
# Write a function that compresses consecutive repeated characters. 
# Store each character followed by its count. 
# Example Input: aaabbccccdaa Example Output: a3b2c4d1a2
def compressTask(word):
    count=1
    result=" " 
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            count+=1
        else:
            result+=word[i]+str(count)
            count=1
    print(result+word[-1]+str(count))
compressTask("aaabbcccaa")

# First Non-Repeating Character 
# Task: Write a function that returns the first character that appears only once in the string. 
# Example Input: aabbcddeff Example Output: First Non-Repeating Character = c
def nonRepeating(word):
    count=1
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            count+=1
        elif count==1:
            print(word[i])
            break
        else:
            count=1
nonRepeating("aabbcddeff")

# Longest Word in a Sentence 
# Task: Write a function that finds the longest word without using split(). 
# Example Input: Python programming improves logical thinking 
# Example Output: Longest Word = programming
def longestWord(word):
    str1=""
    fin_str=""
    for i in word:
        if i!=" ":
            str1+=i
        else:
            if len(str1)>len(fin_str):
                fin_str=str1
            str1=''
    if len(str1)>len(fin_str):
        fin_str=str1  
    print(fin_str)
longestWord("Python programming improves logical thinkingdfee")


# Remove Duplicate Characters Task: Write a function that removes duplicate characters while keeping only their first occurrence. 
# Example Input: programming Example Output: progamin
def removingDup(word):
    str1=""                                                                                                                                                                                             
    for i in word:
        if i in str1:
            str1=str1
        else:
            str1+=i
    print(str1)
removingDup("programming")

# Check Rotation Task: Write a function to check whether one string is a rotation of another.
# Example Input: waterbottle erbottlewat Example Output: Rotation = True
def rotationTask(word1,word2):
    ans=""
    for i in word2:
        if i in word1:
            ans=True
        else:
            ans=False
    print(ans)
rotationTask("waterbottle","erbottlewat")

# Largest Numeric Value Task: Write a function that extracts all numbers from a string and prints the largest number. 
# Example Input: abc12xy450pq89 Example Output: Largest Number = 450
def numericVal(word):
    digit=0
    high=0
    for i in word:
        if "a"<=i<="z" or "A"<=i<="Z":
            digit=0
        else:
            digit=digit*10+int(i)
        if high<digit:
            high=digit
    print(high)
numericVal("abc12xy450pq89")

# Character Frequency Task: Write a function that prints each character and how many times it appears without using count(). 
# Example Input: banana Example Output: b = 1 a = 3 n = 2
def charFrequency(word):
    c=""
    for i in range(len(word)):
        count=1
        if word[i] not in c:
            for j in range(i+1,len(word)):
                if word[i]==word[j]:
                    count+=1
                       
            print(f"{word[i]}={count}")
        c+=word[i]
charFrequency("banana")

# Reverse Words Only Task: Write a function that reverses each word individually while keeping the word order the same. 
# Example Input: Python is awesome Example Output: nohtyP si emosewa
def reverseWord(word):
    str1=""
    str2=''
    for i in word:
        if i!=" ":
            str1+=i
        else:
            str2+=str1[::-1]+" "
            str1=''

    print(str2+str1[::-1])
reverseWord("python is awsome")

# Longest Substring Without Repeating Characters 
# Task: Write a function that finds the length of the longest substring containing no repeated characters. 
# Example Input: abcabcbb Example Output: Length = 3
def subString(word):
    str1=""
    high=0
    for i in word:
        if i not in str1:
            str1+=i  
        else:
            if high<len(str1):
                high=len(str1)
            str1=""
    print(f"Length = {high}")
subString("abcabcbb")

# # Validate Password Strength 
# # Task: Write a function that checks if a password has at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character. 
# # Example Input: Python@123 Example Output: Strong Password
word=input("Enter a word: ")
ans=""
if len(word)>=8:
    for i in range(len(word)):
        if word[i] in ("$","@","&","#","!"):
             special=True
        elif "A"<=word[i]<="Z":
            capital=True           
        elif "a"<=word[i]<="b":
            small=True
        elif "1"<=word[i]<="9":
            digit=True
    if special and capital and  small and digit:
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")
            



    


        






         



            

    



        



    
    