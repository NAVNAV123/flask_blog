def count_substring(string, sub_string):
    x = 0
    for i in range(0, len(string)):
        if string[i] == sub_string[0]:
            if string[i:len(sub_string)] == sub_string:
                x += 1
    return x


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)