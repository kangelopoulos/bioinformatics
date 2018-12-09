import sys

def pattern_count(string, substring):
    count = 0
    for i in range(len(string) - len(substring)):
        print(string[i:i+len(substring)])
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

try:
    mydata = open(sys.argv[1],'r')
except IndexError:
    print("This program requires a second command line argument in the form of a data file.")
    exit()

string = mydata.readline().strip()
substring = mydata.readline().strip()
print(string + "/" + substring + "\n")
print(pattern_count(string, substring))

mydata.close()
