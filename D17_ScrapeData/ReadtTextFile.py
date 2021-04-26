import re

with open(r"data\data.txt", "r") as myfile:
    lines = myfile.readlines()
    for line in lines:
        print(line)
        data = line.split()
        if len(data) > 1:
            print(':'.join(data))

        # \w: character
        x = re.findall("\w*an\d*", line)
        print(x)