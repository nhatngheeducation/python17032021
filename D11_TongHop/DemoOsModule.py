# Demo os module - Lệnh terminal/command line
import os
import subprocess


# Run chương trình
# os.system("dir") # ls
# os.system("notepad.exe")
# os.system("ping google.com")

# Quan tâm kết quả trả vế
result = subprocess.getoutput('ping google.com')
print(result)

# Xử lý từng dòng
lines = result.split('\n')
for line in lines:
    print(line)

# Ghi thời gian ping
filter = "time="
for line in lines:
    if filter in line: # Dòng đang xét có chứa filter
        index = line.index(filter) + len(filter)
        data = line[index:]
        print(data)
        print(data.split()[0])