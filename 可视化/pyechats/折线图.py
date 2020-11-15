from pyecharts.charts import *
from pyecharts.globals import ThemeType
from pyecharts import options as opts

x_data =['apple','huawei','xiaomi','oppo','vivo','meizu']
y_data =[123,153,89,107,98,23]                                  #数据

line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add_xaxis(x_data)
    .add_yaxis('2019年手机销量',y_data)

    .set_global_opts(
        title_opts=opts.TitleOpts(title="主标题",subtitle="副标题")
    )

    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True,color='black')

    )


    .render('HTML/折线图.html')
)