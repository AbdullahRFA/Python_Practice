

with open("hello.txt") as My_file:
    for line in My_file:
        print(line.strip())
        
print('\n')
with open("server.log") as server_log:
    for line in server_log:
        if 'ERROR' in line:
            print("Error ditect in : ",line)


    