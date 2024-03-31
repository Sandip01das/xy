def naive_string_matching(text,pattern):
    n=len(text)
    m=len(pattern)
    
    for i in range(n-m+1):
        j=0
        while j<m and (text[i+j]==pattern[j]):
            j+=1
        if j==m:
            print("Pattern found at index",i)
            return
    print("No match found")

text=input("Enter the text:")
pattern=input("Enter the pattern to search:")
naive_string_matching(text,pattern)


