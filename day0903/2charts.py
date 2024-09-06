from pyecharts.charts import Map
from pyecharts import options as opts

map = Map()

data = [
    ("北京市", 100),
    ("上海市", 300),
    ("山东省", 500),

]

map.add("示例地图", data, "china")

# 配置地图选项
map.set_global_opts(
    title_opts=opts.TitleOpts(title="中国地图示例"),
    visualmap_opts=opts.VisualMapOpts(max_=500)
)

# 指定生成的HTML文件路径
map.render()
