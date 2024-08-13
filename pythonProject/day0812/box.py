# 请使用代码实现以下逻辑：
#
# 某个有两套盲盒套装（每套8个，每个都是不重复的），假设该套装仅有一个隐藏款，开出的概率为 5.6%。
#
# * 假设确定其中有**一个**隐藏款，请问被替换的是哪个
# * 请问每次开盒开出隐藏款的概率是多少
# * 假设有无限的套装可以拆，请开盒直到开出隐藏款
import random

# 定义盲盒套装
box = list(range(1, 17))  # 假设盲盒编号为1-16
chance = 0.056

# 被替换的盲盒

replace = random.choice(box)
print(f"被替换的盲盒编号为：{replace}")

# 每次开盒开出隐藏款的概率是5.6%

# 模拟开核直到开出隐藏
check = 0
while random.random() >= chance:
    check += 1
check += 1
print(f"开了{check}次")
