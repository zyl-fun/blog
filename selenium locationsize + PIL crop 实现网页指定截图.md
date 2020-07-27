### selenium location/size + PIL crop 实现网页指定部分截图

```python
def shibie(driver,code_img_xpath):
    driver.save_screenshot('code.png') #保存截图
    code_img = driver.find_element_by_xpath(code_img_xpath) #xpath规则
    location = code_img.location #定位元素位置，是一个字典，像素点的位置 key : x , y
    size = code_img.size #定位到图片的大小，是一个字典，宽和高 key : width , heigth
    rangle = (location['x'], location['y'],location['x']+size['width'],location['y']+ size['height'])#截图位置初始化，左， 上， 右， 下
    #开始截图
    i = Image.open('code.png')
    frame = i.crop(rangle)
    frame.save('code.png')
```



![](../pic/%E6%88%91%E5%92%8C%E4%BD%A0%E5%A6%88%E5%A6%88%E4%BC%9A%E6%B0%B8%E8%BF%9C%E7%88%B1%E4%BD%A0.png)