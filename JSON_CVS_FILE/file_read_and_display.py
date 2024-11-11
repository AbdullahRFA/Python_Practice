# This code snippet is reading the contents of two files, 'Introduction.txt' and 'server.log'.
with open('Introduction.txt') as intro:
    for line in intro:
        print(line)

with open('server.log') as server:
    for line in server:
        if 'ERROR' in line:
            print("ERROR ditect at line : ",line)