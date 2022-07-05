import time

i = 0
while i <= 6:
    file_name = r'C:\Users\msi\Documents\hosts.txt'
    with open(file_name, 'a+', encoding='utf-8') as file2:
        file2.write(str(i) + '\n')
        i += 1