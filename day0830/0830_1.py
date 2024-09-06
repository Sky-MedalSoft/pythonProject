str = "itheima itcast boxuegu"

print(str.count("it"))

strNew = str.replace(" ", "|")
print(strNew)

strList = strNew.split("|")
print(strList)

# %%
str = "员序程马黑来，nohtyP学"
strS = str[::-1][9:14]
print(strS)


# %%
def usr_info(*args):
    print(args)


usr_info("hello", "world")


def usr_info(**kwargs):
    print(kwargs)


usr_info(name="wang")