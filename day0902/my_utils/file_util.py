def print_file_info(file_name):
    try:
        f = open(file_name, mode='r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError as e:
        print(e)
    finally:
        f.close()
def append_file_info(file_name):
    try:
        f = open(file_name, mode='a', encoding='utf-8')
        f.write("1111")
    except FileNotFoundError as e:
        print(e)
    finally:
        f.close()


if __name__ == '__main__':
    print_file_info('D:\\2.txt')