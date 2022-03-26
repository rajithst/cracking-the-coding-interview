MAX = 1000


# Replaces spaces with %20 in-place and returns
# new length of modified string. It returns -1
# if modified string cannot be stored in str[]
def replaceSpaces(string):
    # Remove remove leading and trailing spaces
    string = string.strip()

    i = len(string)

    # count spaces and find current length
    space_count = string.count(' ')

    # Find new length.
    new_length = i + space_count * 2

    # New length must be smaller than length
    # of string provided.
    if new_length > MAX:
        return -1

    # Start filling character from end
    index = new_length - 1

    string = list(string)

    # Fill string array
    for f in range(i - 2, new_length - 2):
        string.append('0')

    # Fill rest of the string from end
    for j in range(i - 1, 0, -1):

        # inserts %20 in place of space
        if string[j] == ' ':
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index = index - 3
        else:
            string[index] = string[j]
            index -= 1

    return ''.join(string)


# Driver Code
if __name__ == '__main__':
    s = "Mr John Smith "
    s = replaceSpaces(s)
    print(s)