import sys

def read_file(file_name,read_format='r',read_all=True,read_lines=True,print_content=False,starting=1,ending=sys.maxsize):
    """
        Utility function to read file
        Parameters:
            file_name(str): Fully qualified file name. Required !
            read_format(str): file open format. Default - r
            read_all(Boolean): True for reading entire file. False for readling iteratively. Default - True
            read_lines(Boolean): True for reading line. False for reading character by character. Default - True
            print_content(Boolena): True for printing file content while reading. False for no print. Default - False
            starting(int): Starting point for file reader. Default - 1
            ending(int): Till what point file is to be read. Default - sys.maxsize
        Returns:
            list(str): File Contents as a list
    """

    result = list()

    if (read_lines and not read_all):
        print("Reading total of [{}] lines, each line with format [{}]".format(ending,read_format))
        with open(file_name,read_format) as reader:
            ctr = 1
            for line in reader:
                if (ctr>=starting):
                    result.append(line)
                    if print_content: print("line # [{}] --> [{}]".format(ctr,line))
                if (ctr>=ending): break
                ctr+=1

    elif (not(read_lines and read_all)):
        print("Reading total of [{}] characters, each character with format[{}]".format(ending,read_format))
        with open(file_name,read_format) as reader:
            ctr = 1
            for char in reader.readline():
                if (ctr>=starting):
                    result.append(char)
                    if print_content: print("character # [{}] --> [{}]".format(ctr,char))
                if (ctr>=ending): break
                ctr+=1

    elif (read_lines and read_all):
        print("Reading entire file with format[{}]".format(read_format))
        with open(file_name,read_format) as reader:
            ctr = 1
            lines = reader.readlines()
            if print_content: print("lines read [{}]".format(len(lines)))
            result = lines
    
    else:
        print("Unsupported combination --> read_lines:[{}] | read_all:[{}]".format(read_lines,read_all))

    return result

# https://www.kaggle.com/hwassner/TwitterFriends/download
file_name = '/Users/dmohanakumarchan/Downloads/TwitterFriends.csv'

read_file(file_name,read_all = False,print_content=True,ending=1)
# Reading each line with format [r]
# line # [1] --> [id,screenName,tags,avatar,followersCount,friendsCount,lang,lastSeen,tweetId,friends
# ]

read_file(file_name,read_lines=False,read_all = False,print_content=True,read_format='rb',ending=5)
# Reading each character with format[r]
# character # [1] --> [i]
# character # [2] --> [d]
# character # [3] --> [,]
# character # [4] --> [s]
# character # [5] --> [c]

assert(read_file(file_name,read_lines=False,starting=1,ending=2)==list(["i",'d']))

read_file(file_name,read_lines=False,read_all = False,print_content=True,read_format='rb',starting=4,ending=13)
# Reading total of [13] characters, each character with format[rb]
# character # [4] --> [s]
# character # [5] --> [c]
# character # [6] --> [r]
# character # [7] --> [e]
# character # [8] --> [e]
# character # [9] --> [n]
# character # [10] --> [N]
# character # [11] --> [a]
# character # [12] --> [m]
# character # [13] --> [e]

from_file = read_file(file_name)
print(len(from_file))
# Reading entire file with format[r]
# 40001
