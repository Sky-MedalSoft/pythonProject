str = "Tianjin Institute of Software Engineering"
count = 0;
for _ in str:
    if (_ == 'a'):
        count += 1
print(f"{str}中含有{count}个'a'字母。")

#%%
x: int = 100
count = 0
for i in range(0,x):
    if (i%2==0):
        count += 1
print(f"从0到{x}中，偶数的个数为{count}。")
#%%
i = 1
for _ in range (9):
    j = 1
    for j in range(1,i+1):
        print(f"{j} x {i} = {i*j}\t", end="")
        j += 1
    print()
    i += 1

