from pyecharts.charts import Map
from pyecharts import options as opts
import random
from pyecharts.globals import  ThemeType

"""数据"""
province = ['江西','湖南','浙江','新疆','山西','四川']
data = [(i,random.randint(10,150)) for i in province]

_map =(
    Map(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))                      #设置为ios风格的图标 MACARONS

    .add("",data,"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="map-地图基本示例",subtitle="这是副主题"),
        legend_opts= opts.LegendOpts(is_show=True),
        tooltip_opts=opts.ToolboxOpts(is_show=True,pos_left='right'),
        visualmap_opts=opts.VisualMapOpts(max_=200,is_piecewise=True)                       #数据颜色加深
    )
)
_map.render('HTML/地理图.html')