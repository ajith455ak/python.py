def isomorphic(s, t):
    if len(s) != len(t):
        return False    
    mapping = {}
    mapped_chars = set()
    for i in range(len(s)):
        if s[i] in mapping:
            if mapping[s[i]] != t[i]:
                return False
        else:
            if t[i] in mapped_chars:
                return False
            mapping[s[i]] = t[i]
            mapped_chars.add(t[i])
    return True
s=input("enter the string 1:")
t=input("enter the string 2:")
print(isomorphic(s,t))
