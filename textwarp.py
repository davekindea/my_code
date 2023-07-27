import textwrap

def wrap(string, max_width):
    a=""
    i=0
    while i<len(string):
        a=a+string[i:(i+max_width)]+"\n"
        i+=max_width
    return a

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
