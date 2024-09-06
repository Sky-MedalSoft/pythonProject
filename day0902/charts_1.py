from pyecharts.charts import Line


def create_line_chart(x_data, y_data, series_name):
    try:
        # 创建一个折线图对象
        line = Line()

        # 添加X轴数据
        line.add_xaxis(x_data)
        # 添加Y轴数据，并指定系列名称
        line.add_yaxis(series_name, y_data)

        # 渲染图表
        line.render()
    except Exception as e:
        print(f"An error occurred: {e}")


# 示例调用
create_line_chart(["ming", "zhang"], [1, 2], "score")
