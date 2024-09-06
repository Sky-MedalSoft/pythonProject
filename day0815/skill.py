#%%
"""常用占位符：
    字符串：%s
    整数:%d
    浮点数：%f"""
str = 'world'
print("hello %s" % str)

"""
    快速格式化写法 """
name = "sky wen"
print(f"i am {name}")

#%%
# 股价计算
# 定义变量
name = "Example Corp"
stock_price = 100.0 #当前股价
stock_code = "EXMPL" # 股票代码
stock_price_daily_growth_factor = 1.02 # 每日增长系数
growth_days = 30 # 增长天数
# 计算经过增长天数后的股价
future_stock_price = stock_price * (stock_price_daily_growth_factor ** growth_days)
# 使用字符串格式化输出结果
print(f"经过{growth_days}天后，股价变为{future_stock_price:.2f}")
#%%
sum = 0
i = 0
while i  <= 100:
    sum += i
    i += 1
print(sum)
#%%
# 打印九九乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i} \t", end=" ")
        j += 1
    i += 1
    print(" ")