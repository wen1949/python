from pyecharts import options as opts

from pyecharts.charts import Map

from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

c = (
    Map(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))

    .add("世界地图",[list(z) for z in zip(Faker.country,Faker.values())],"world")               #加载地图实例,从Faker上获取数据

    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False)
                    )                                   #显示图标

    .set_global_opts(
        title_opts=opts.TitleOpts(title="世界地图实例"),                                         #设置标题
        visualmap_opts=opts.VisualMapOpts(max_=200)
                    )
    .render("HTML/word_max.html")                                            #生成html超文本文件
)