# comment and uncomment lines with flags in a python file
# usage: python update.py 1 3  
#   comments method_1 and uncomments method_3

import sys

def uncomment(line):
    # ind is short for indentation
    ind_a = len(line) - len(line.lstrip())
    ind_b = 0
    comment = 0
    if line[ind_a] == '#':
        comment = 1
        ind_b = len(line[ind_a+1:]) - len(line[ind_a+1:].lstrip())
    ind = round((ind_a + ind_b - 1) / 4) * 4
    # print(ind_a, ind_b, ind)
    return(' ' * ind + line[ind_a + ind_b + comment:])

def comment(line):
    # ind is short for indentation
    ind = len(line) - len(line.lstrip())
    return(' ' * ind + '# ' + line[ind:])


def change_method(file_contents, old_method, new_method):
    for line_num in range(len(file_contents)):
        line = file_contents[line_num]

        if old_method in line:
            # print(line.replace('\n',''))
            line = comment(line)
            file_contents[line_num] = line
            # print(line)


        if new_method in line:
            # print(line.replace('\n',''))
            old_len = -1
            while old_len != len(line):
                old_len = len(line)
                line = uncomment(line)
            # print(line)
            file_contents[line_num] = line
    return file_contents

# update part of a config file
def update_file(filename, old_method, new_method):
    file_contents = ""
    with open(filename) as file:
        file_contents = file.readlines()

    file_contents = change_method(file_contents, old_method, new_method)

    with open(filename, 'w') as file:
        file.writelines(file_contents)



def perform_tests():
    test_cases = []
    test_lines_1 = [
        "#    asdf",      "#     asdf", 
        " #   asdf",      " #    asdf", 
        "  #  asdf",      "  #   asdf", 
        "   # asdf",      "   #  asdf", 
        "    #asdf",      "    # asdf", 
        "    asdf",       "     asdf", 
    ]
    test_cases.append([test_lines_1, "    asdf", "    # asdf"])
    test_lines_2 = [
        "#    #asdf", 
        " #   #asdf", 
        "  #  #asdf", 
        "   # #asdf", 
        "    ##asdf", 
    ]
    test_cases.append([test_lines_2, "    #asdf", "    # #asdf"])
    test_lines_3 = [
        "#     # asdf", 
        " #    # asdf", 
        "  #   # asdf", 
        "   #  # asdf", 
        "    # # asdf", 
    ]
    test_cases.append([test_lines_3, "    # asdf", "    # # asdf"])
    for case in test_cases:
        for line in case[0]:
            new = uncomment(line)
            if new != case[1]:
                print(line)
                print(new)
                print("")
            new = comment(new)
            if new != case[2]:
                print(line)
                print(new)
                print(case[2])
                print("")

if __name__ == "__main__":
    # perform_tests()

    if len(sys.argv) == 3:
        update_file("test.py", "method_" + sys.argv[1], "method_" + sys.argv[2])
    else:
        old_method = "method_1"
        new_method = "method_3"
        update_file("test.py", old_method, new_method)

