# 我在工作中用到的xpath解析规则

![img](%E5%9B%BE%E7%89%87/20181026150157860.jpg)

---

```shell
a[not(contains(text(),'不限'))]

//span[contains(text(),'招聘人数')]/../i/text()    父路径

normalize-space(//dl[@class='zw_a']/dt/text())  去掉 \t\n\r 字符

substring-before(//div[contains(@class,'pubtime-jobintro')]/text(),'更新')

selector.xpath('//div[@id="content"]//tr[position()>1]/td[2]/a/@href')  位置参数

//div[contains(text(),'联 系 人：')]/following-sibling::div[1]    获取当前节点的下一个相邻节点

substring-after(//a[contains(text(),'尾页')]/@href,'page=')

//div[contains(@class,'posJobSort')]//a/@href

//h3[contains(text(),'职位详情')]/parent::div[1]/following-sibling::div[1]//text()

#在使用模板的时候，如果是异步请求，需要加上请求头，用户身份和token,在获取详情页入口的时候，如果拿取不到数据，select:xpath regex: //*  查看获取到数据的格式，再进行改正

//span[contains(text(),'开发商')]/parent::div/following-sibling::div/a/text()

(//img[starts-with(@src,'https://static.damengxiang.me/files/qrcode/')]/@src)[1]
//上面是以标签的模糊属性进行定位，并且只取第一个元素，用括号括起来

//元素匹配
page_num = html.xpath("//ul[contains(@class,'pagination')]/li[last()-1]/a/text()")
```

