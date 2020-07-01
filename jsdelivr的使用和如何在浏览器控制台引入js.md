## jsdelivr的使用和如何在浏览器控制台引入js

*因为需要在chrome控制台执行自己写的 js 脚本，为了方便，把 js文件托管到 github*

下面介绍 jsdelivr的使用

- [ ] 第一步，把要使用的 js文件 的仓库进行 release

![](https://github.com/zyl-fun/pic/blob/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200701193024.png?raw=true)

- [ ] 第二步，进入你要使用的js文件，保存其路径

```shell
https://github.com/zyl-fun/pic/blob/master/mybook/hook.js
#注意此时为 master分支，需要修改为刚才添加的tag版本
https://github.com/zyl-fun/pic/blob/v1.0.1/mybook/hook.js
```

- [ ] 第三步，替换为 CDN

```shell
#注意替换的规则
https://github.com/zyl-fun/pic/blob/v1.0.1/mybook/hook.js
https://cdn.jsdelivr.net/gh/zyl-fun/pic@v1.0.1/mybook/hook.js
```

- [ ] 最后，使用，我需要在 chrome 控制台使用

```shell
#粘贴到控制台，src 为 jsdelivr地址
var script = document.createElement('script');
script.src = "https://cdn.jsdelivr.net/gh/zyl-fun/pic@v1.0.1/mybook/hook.js";
document.getElementsByTagName('head')[0].appendChild(script);
```

------

[jsdelivr官网](https://www.jsdelivr.com/?docs=gh)

![](https://github.com/zyl-fun/pic/blob/master/%E6%88%91%E5%92%8C%E4%BD%A0%E5%A6%88%E5%A6%88%E4%BC%9A%E6%B0%B8%E8%BF%9C%E7%88%B1%E4%BD%A0.png?raw=true)