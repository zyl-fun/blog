# 我在工作中用到的xpath解析规则

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
```

