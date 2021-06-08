#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 13:08
# @Author  : AsiHacker
# @Site    : 
# @File    : mingyanSpider.py
# @Software: PyCharm
import datetime

import xlwt
from faker import Faker
from tqdm import tqdm

msg = """
           <<<信息生成器>>>
ar_EG- Arabic (Egypt)    阿拉伯语 - 埃及
ar_PS- Arabic (Palestine)阿拉伯语 - 巴勒斯坦
ar_SA- Arabic (Saudi Arabia)阿拉伯语 - 沙特阿拉伯
bg_BG- Bulgarian    保加利亚语 - 保加利亚
cs_CZ- Czech       捷克语 - 捷克
de_DE- German      德语 - 德国
dk_DK- Danish      丹麦语 - 丹麦
el_GR- Greek      希腊语 - 希腊
en_AU- English (Australia)  英语 - 澳大利亚
en_CA- English (Canada)  英语 - 加拿大
en_GB- English (Great Britain)  英语 - 英国
en_US- English (United States) 英语 - 美国
es_ES- Spanish (Spain)    西班牙语 - 西班牙
es_MX- Spanish (Mexico)    西班牙语- 墨西哥
et_EE- Estonian      爱沙尼亚语 - 爱沙尼亚
fa_IR- Persian (Iran)    波斯语 - 伊朗
fi_FI- Finnish    芬兰语 - 芬兰
fr_FR- French    法语 - 法国
hi_IN- Hindi      印地语 - 印度
hr_HR- Croatian  克罗地亚语 - 克罗地亚
hu_HU- Hungarian  匈牙利语 - 匈牙利
hy_AM- Armenian 亚美尼亚语 - 亚美尼亚
it_IT- Italian   意大利语 - 意大利
ja_JP- Japanese  日语 - 日本
ko_KR- Korean  朝鲜语 - 韩国
ka_GE- Georgian (Georgia) 格鲁吉亚语 - 格鲁吉亚
lt_LT- Lithuanian  立陶宛语 - 立陶宛
lv_LV- Latvian拉脱维亚语 - 拉脱维亚
ne_NP- Nepali尼泊尔语 - 尼泊尔
nl_NL- Dutch (Netherlands)  德语 - 荷兰
no_NO- Norwegian  挪威语 - 挪威
pl_PL- Polish  波兰语 - 波兰
pt_BR- Portuguese (Brazil)  葡萄牙语 - 巴西
pt_PT- Portuguese (Portugal)  葡萄牙语 - 葡萄牙
ru_RU- Russian  俄语 - 俄国
sl_SI- Slovene 斯诺文尼亚语 - 斯诺文尼亚
sv_SE- Swedish  瑞典语 - 瑞典
tr_TR- Turkish    土耳其语 - 土耳其
uk_UA- Ukrainian  乌克兰语 - 乌克兰
zh_CN- Chinese (China)  （简体中文）
zh_TW- Chinese (Taiwan) （繁体中文）
------性别------
M:男 F:女


@Author  : AsiHacker
"""


def save_excel(data_list: list, file_name: str):
    """

    :param data_list: 保存列表
    :param file_name: 文件名称
    :return:
    """
    f = xlwt.Workbook()
    # 创建sheet
    sheet1 = f.add_sheet(u8bf7编码的解码'sheet1', cell_overwrite_ok=True)
    # 生成第一行

    for h in range(len(data_list)):
        title_list = list(data_list[h].keys())
        for l in range(len(title_list)):
            sheet1.write(h, l, data_list[h][title_list[l]])  # 顺序为x行x列写入第x个元素
    f.save(f'{file_name}.xls')


if __name__ == '__main__':
    print(msg)
    country = input('请输入国家<默认 中国>：') or 'zh_CN'
    f = Faker(locale=country)
    sex = input('请输入性别<默认 不限>：') or None
    count = input('请输入数量<默认 100>：') or 100
    print(country, sex, count)
    save_list = list()
    jdt = tqdm(range(int(count)))
    for i in jdt:
        jdt.set_description(f"正在生成 国家：{country} 性别：{sex} by:AsiHacker")
        save = f.profile(sex=sex)
        save_list.append({k: str(v) for k, v in save.items()})
    file_name = input('请输入保存名称：') or str(datetime.datetime.now())
    save_excel(save_list, file_name)
    input('生成完毕！请按任意建退出！')
