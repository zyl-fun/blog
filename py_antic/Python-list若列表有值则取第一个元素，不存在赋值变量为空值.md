## Python-list若列表有值则取第一个元素，不存在赋值变量为空值

```python
min_name = html.xpath("//div[@class='name']/h1/text()")
min_name = min_name[0] if len(min_name) else ""
```

