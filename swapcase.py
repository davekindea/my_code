def swap_case(s):
    x=""
    for i in range (len(s)):
        y=ord(s[i])
        if y>=65 and y<=90:
            x+=s[i].lower()
        elif y>=97 and y<=122:
            x+=s[i].upper()
        else:
            x+=s[i]
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
