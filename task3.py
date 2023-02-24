#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

(2 points)
'''

def split(input):
    '''
    parameters
    str input - string to be split
    
    return
    str new string with line break in the middle
    '''

    return

def split(s):
    length = len(s)
    half_length = length // 2
    if s[half_length] != " ":
        # Find the last space before the middle point
        i = s.rfind(" ", 0, half_length)
        if i == -1:
            i = half_length
            s1 = s[:i]
        else:
            s1 = s[:i]
        s2 = s[i+1:]
    else:
        s1 = s[:half_length]
        s2 = s[half_length+1:]
    return s1 + "\n" + s2
s=input("input your sentence:")

y=split(s)
print(y)


"""
if __name__ == "__main__":
    sentence = "There is a big balloon in the blue sky"
    assert split(s) == "There is a big ball-\noon in the blue sky"

    sentence = "I am a fat cat"
    assert split(s) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(s) == "I was a\n fat cat"
    """