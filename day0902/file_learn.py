f1 = open('bill.txt', 'r', encoding='utf-8')
f2 = open('bill.txt.pak', 'w', encoding='utf-8')
f2.write(f1.readline())
content = f1.readlines()
for line in content:
    if "正式" in line:
        f2.write(line)
f1.close()
f2.close()
