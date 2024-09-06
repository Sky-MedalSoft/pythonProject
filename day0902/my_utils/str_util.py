def str_reverse(s):
    return s[::-1]
def  substr(s, x, y):
    """
    对字符串进行切片
    :param s:
    :param x:
    :param y:
    :return:
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse('hello'))