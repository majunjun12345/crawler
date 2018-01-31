# 普通爬虫

1. 爬虫的原理: url -> html -> model (洗数据) -> 分析
2. request pyquery
```
pip install request
pip install pyquery
``` 
3. `douban1.py` 最基础的爬虫  / 后来加入了 mongodb 数据库
4. `douabn2.py` 爬了多个页面
5. `douabn3.py` 加入了页面缓存功能
    - 代码写错了
    - 页面不规整
    - 老板加需求
    - 有缓存上面三种情况都很容易处理
6. 下载图片
7. 伪装登录状态
8. 动态内容的爬取


# 超高级爬虫

## windows
1. 装依赖 pip install splinter
2. 把 chrome / firefox 驱动加 path

## linux

```bash
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - 
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
sudo apt-get update 
sudo apt-get install unzip google-chrome-stable

wget https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mkdir -p $HOME/bin
mv chromedriver $HOME/bin
echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_rc
source $HOME/.bash_rc
sudo pip3 install splinter
```


# douban3.py 缓存页面内容（方便二次爬取）
![img](https://github.com/majunjun12345/crawler/blob/master/%E5%8A%9F%E8%83%BD%E5%B1%95%E7%A4%BA/%E7%BC%93%E5%AD%98%E9%A1%B5%E9%9D%A2.gif)

# douban4.py 保存图片
![img](https://github.com/majunjun12345/crawler/blob/master/%E5%8A%9F%E8%83%BD%E5%B1%95%E7%A4%BA/%E5%AD%98%E5%9B%BE.gif)
