from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType

china = map(
    Map3D(init_opts=opts.InitOpts(width='1500px',height='1000px',bg_color='#EBEBEB'))               #设置地图大小及颜色

    .add_schema(
        itemstyle_opts=opts.ItemStyleOpts(
            color = '#CDBA96',
            opacity= 1,
            border_width=0.8,
            border_color="rgd(62,215,213)",
        ),
        map3d_label=opts.Map3DLabelOpts(
            is_show=True,
            text_style=opts.TextStyleOpts(
                color="#CEF9F4",font_size=16,background_color="rgba(0,0,0)"
            ),
        ),
        emphasis_label_opts=opts.LabelOpts(is_show=True),                           #地图整体颜色
        light_opts=opts.Map3DLightOpts(
            main_color="#FFEBCD",
            main_intensity=1.2,
            main_alpha=55,
            main_beta=10,
            ambient_intensity=0.3
        ),
    )
    .add(series_name="",data_pair="",maptype=ChartType.MAP3D)

    .set_global_opts(                                                           #全局设置地图属性
        title_opts=opts.TitleOpts(title="全国行政区划分图"),
        visualmap_opts=opts.VisualMapOpts(is_show=True),
        tooltip_opts=opts.TooltipOpts(is_show=False),

    )
    .render("HTML/map3d_china_base.html")
)
