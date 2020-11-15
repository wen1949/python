from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType
"""数据"""
x_data =['apple','huawei','xiaomi','oppo','vivo','meizu']
y_data =[123,153,89,107,98,23]

pie = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))                                                           #pie为饼状图
    .add('',[list(z) for z in zip(x_data,y_data)],                  #将数据导入图中
         radius= ["30%","75%"],                                 #饼状图的半径，30%是内半径，70%是外半径
         rosetype="radius"                                      #是否展示成南丁格尔图通过半径区分数据大小，有radius与area两种模式。
         )

    .set_global_opts(                                                         #全局配置
        opts.TitleOpts(title="饼状图的基本示例",subtitle="副标题"),
                    )
    .set_series_opts(                                                          #图表系列配置
        label_opts=opts.LabelOpts(formatter="{b}:{d}%")                             #显示数据的百分比
                     )

    .render('HTML/饼图.html')
)