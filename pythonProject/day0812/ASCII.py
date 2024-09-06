# 生成从a到z的列表
alphabet_list = [chr(i) for i in range(ord("a"), ord("z") + 1)]
print(alphabet_list)
# ord("a")：ord 函数返回字符 "a" 的 ASCII 码值，即 97。
# ord("z") + 1：ord 函数返回字符 "z" 的 ASCII 码值，即 122，然后加 1 得到 123。
# range(ord("a"), ord("z") + 1)：生成一个从 97 到 122 的整数序列。
# chr(i)：chr 函数将 ASCII 码值转换回对应的字符。
alphabet_list = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
print(alphabet_list)
