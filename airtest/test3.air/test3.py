# -*- encoding=utf8 -*-
__author__ = "xingdao_1"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
xy = poco.get_screen_size()
x = xy[0]
y = xy[1]
# swipe((x*0.9,y*0.5),(x*0.1,y*0.5),duration=1)
poco(desc="IT桔子").click()

print("*************************************")
sleep(4)
poco(name="com.itjuzi.app:id/iv_logo").click()
poco(text="默认排序").click()
poco(text="更新时间").click()
# poco("android.widget.LinearLayout").click()
num = 0
while 1:
    num += 1
    info_list = poco(name = "com.itjuzi.app:id/company_new_name_txt")
    title_list = [title.get_text() for title in info_list]
    for title in title_list:
        print(title)
#         poco(text=title).click()
#         sleep(1)
#         desc = ""
#         info_1 = poco(name="com.itjuzi.app:id/tv_event_head_detail_title")
#         if info_1:
#             desc += info_1.get_text()
#         info_2 = poco(name="com.itjuzi.app:id/tv_event_head_detail_content")
#         if info_2:
#             desc += info_2.get_text()
#         basic_info = ""
#         info_3 = poco(name="com.itjuzi.app:id/com_desc_txt")
        
#         if info_3:
#             basic_info = info_3.get_text()
#         print(desc)
#         tags = ""
#         tag_list = poco(name = "com.itjuzi.app:id/com_tags_layout").child(name="android.widget.TextView")
#         if tag_list:
#             for i in tag_list:
#                 tags += i.get_text()
#                 tags += " "
#         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#         print(desc)
#         print(basic_info)
#         print(tags)
#         keyevent("BACK")
            
    swipe((x*0.5,y*0.9),(x*0.5,y*0.1),duration = 0.5)
    swipe((x*0.5,y*0.9),(x*0.5,y*0.1),duration = 0.5)
    swipe((574,1922),(747,632),duration = 3)
    sleep(2)
    if num == 4:
        break
     




