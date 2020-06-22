# pipenv之python超好用的包管理工具

[参考](https://segmentfault.com/a/1190000015389565)
[python环境安装](https://blog.csdn.net/weixin_44038167/article/details/106825067)

[pdf下载](https://github.com/zyl-fun/pic/blob/master/Pipenv%20%E2%80%93%20%E8%B6%85%E5%A5%BD%E7%94%A8%E7%9A%84Python%E5%8C%85%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7.pdf)

## 安装
**pip install pipenv**
**pip3 install pipenv**

## 使用

```bash
mkdir my_python3.7
pipenv install --python 3.7

#命令执行后会在文件夹生成两个文件
>>>Pipfile  Pipfile.lock

#进入&退出环境 
pipenv shell
exit | ctrl + d
```
Pipfile ⾥有最新新安装的包⽂件的信息，如名称、版本等。⽤来在重新安装项⽬依赖或与他⼈共享项⽬时，你可以⽤ Pipfile 来
跟踪项⽬依赖。
Pipfile 是⽤来替代原来的 requirements.txt 的，内容类似下⾯这样。source 部分⽤来设置仓库地址，packages 部分⽤来指定项⽬依 赖的包，dev-packages 部分⽤来指定开发环境需要的包，这样分开便于管理。
*设置仓库地址可以指定国内的镜像源     https://pypi.douban.com/simple*

Pipfile.lock 则包含你的系统信息，所有已安装包的依赖包及其版本信息，以及所有安装包及其依赖包的 Hash 校验信息。

```bash
pipenv install Scrapy==1.4.0 #指定安装包的版本
pipenv install httpie --dev #安装开发环境下的包
pipenv uninstall #卸载
pipenv update #更新
pipenv --venv  #查看虚拟环境目录
pipenv --where #查看项目根目录
pipenv check #检查包的完整性 我这有毛病，不知为何
pipenv graph #查看依赖树
#如果别人的项目中包含的是requirements.txt
pipenv install -r requirements.txt
```