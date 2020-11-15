from pyecharts import options as opts
from pyecharts.charts import *
from pyecharts.globals import ThemeType


x_data =['apple','huawei','xiaomi','oppo','vivo','meizu']
y_data =[123,153,89,107,98,23]                                  #数据

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))                                       #括号内可添加样式主题。Bar()为直方图

    .add_xaxis(x_data)                          #添加x轴数据
    .add_yaxis('2019年各厂家手机销量',y_data)               #y轴数据
    .add_yaxis('2020年',[150,300,120,160,100,20])

    .set_global_opts(                                           #全局配置
        title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
        legend_opts =opts.LegendOpts(pos_left='40%',orient='vertival',legend_icon='diamond'),       #中间标题样式更改
        tooltip_opts=opts.ToolboxOpts(is_show=True,pos_left='1'),
        visualmap_opts=opts.VisualMapOpts(is_show=True),
        datazoom_opts=opts.DataZoomOpts(is_show=True)

    )

    .set_series_opts(                            #图表系列配置
        label_opts=opts.LabelOpts(is_show=True, color='black'),
        linestyle_opts=opts.LineStyleOpts(is_show=True, width=10, type_='dotted'),
        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"), ])                 #指示出最大值

    )
    )
bar.render("HTML/直方图.html")
