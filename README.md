# 普通爬虫

1. 爬虫的原理: url -> html -> model (洗数据) -> 分析
2. 两个库：request pyquery
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
6. `douban4.py` 加入了下载图片
7.`zhihu1` 伪装登录状态
8. `zhihu2` 动态内容的爬取


# 超高级爬虫

## windows
1. 装依赖 pip install splinter
2. 把 chrome / firefox 驱动加 path


# douban3.py 缓存页面内容（方便二次爬取）
![img](https://github.com/majunjun12345/crawler/blob/master/%E5%8A%9F%E8%83%BD%E5%B1%95%E7%A4%BA/%E7%BC%93%E5%AD%98%E9%A1%B5%E9%9D%A2.gif)

# douban4.py 保存图片
![img](https://github.com/majunjun12345/crawler/blob/master/%E5%8A%9F%E8%83%BD%E5%B1%95%E7%A4%BA/%E5%AD%98%E5%9B%BE.gif)

# zhihu1.py 伪装登陆
![img](https://github.com/majunjun12345/crawler/blob/master/%E5%8A%9F%E8%83%BD%E5%B1%95%E7%A4%BA/%E4%BC%AA%E8%A3%85%E7%99%BB%E5%BD%95.gif)
