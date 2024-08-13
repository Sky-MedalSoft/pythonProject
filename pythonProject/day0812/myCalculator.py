def calculate(expression):
    def parse_number(expr, index):
        """从给定的索引开始解析一个数字。
        遍历字符串，直到遇到非数字字符，将连续的数字字符转换为一个整数。
        返回解析的数字和当前索引。"""
        number = 0
        while index < len(expr) and expr[index].isdigit():
            number = number * 10 + int(expr[index])
            index += 1
        return number, index

    def parse_factor(expr, index):
        """"解析一个因子，可以是括号内的表达式或一个数字。
        如果遇到左括号 (，则递归解析括号内的表达式，直到遇到右括号 )。
        否则，调用 parse_number 解析一个数字。"""
        if expr[index] == '(':
            index += 1
            result, index = parse_expression(expr, index)
            if expr[index] == ')':
                index += 1
            return result, index
        else:
            return parse_number(expr, index)

    def parse_term(expr, index):
        """解析一个表达式，表达式是由加法和减法操作符连接的项。
        它首先解析一个项，然后循环解析后续的加法和减法操作符及其对应的项，并进行相应的计算。"""
        result, index = parse_factor(expr, index)
        while index < len(expr) and expr[index] in ('*', '/'):
            operator = expr[index]
            index += 1
            factor, index = parse_factor(expr, index)
            if operator == '*':
                result *= factor
            elif operator == '/':
                result /= factor
        return result, index

    def parse_expression(expr, index):
        """该函数解析一个表达式，表达式是由加法和减法操作符连接的项。
        它首先解析一个项，然后循环解析后续的加法和减法操作符及其对应的项，并进行相应的计算。"""
        result, index = parse_term(expr, index)
        while index < len(expr) and expr[index] in ('+', '-'):
            operator = expr[index]
            index += 1
            term, index = parse_term(expr, index)
            if operator == '+':
                result += term
            elif operator == '-':
                result -= term
        return result, index

    # 去除表达式中的空格。
    # 从索引0开始解析整个表达式。
    # 返回计算结果。
    expr = expression.replace(' ', '')
    result, _ = parse_expression(expr, 0)
    return result


print(calculate(input("Enter expression(请使用英文输入法): ")))
