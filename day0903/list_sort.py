# 准备列表
my_list = [["a", 33], ["b", 55], ["c", 11]]


# 基于带名函数进行排序
def choose_sort_key(element):
    return element[1]

my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)

# 基于lamda排序
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)
