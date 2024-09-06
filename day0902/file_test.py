# read可续读
# 注意：
# *直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
# *当调用flush的时候，内容会真正写入文件
# *这样做是避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写磁盘)
f = open("D:\\1.txt", "r", encoding="utf-8")
print(f.read(10))
print(f.read())
f2 = open("D:\\2.txt", "w", encoding="utf-8")
f2.write("中文")
f2.flush()
f2.close()