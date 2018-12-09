import sys

#finds most frequent substring of length k in a string
def freq_count(string, k):
    d = {}
    for i in range (0, len(string) - k):
        if string[i: i + k] in d:
            d[string[i: i + k]] += 1
        else:
            d[string[i: i + k]] = 1
    max = 0
    kmers = []
    for i in d:
        if d[i] > max:
            max = d[i]
            kmers.clear()
            kmers.append(i)
        elif d[i] == max:
            kmers.append(i)
        else:
            pass
    for i in kmers:
        print(i, end = " ")

#Parses file values. Returns 0 on error state.
def read_data(data):
    try:
        string = data.readline().strip()
        k = int(data.readline().strip())
    except ValueError:
        print("File improperly formatted. See documentation.")
        return 0
    return string, k


try:
    data = open(sys.argv[1], 'r')
    list = read_data(data)
    if list == 0:
        pass
    else:
        freq_count(list[0], list[1])
    data.close()
except IndexError:
    print("Requires input of file as the second command line argument. Please try again.")
except IOError:
    print("This file does not exist, try again later.")
