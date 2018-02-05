import os
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient



class Model(object):

    db = MongoClient().douban1

    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{0} : ({1})'.format(k, v) for k, v in self.__dict__.items())
        # print('properties:', properties)
        s = '\n<{0} \n  {1}>'.format(name, '\n  '.join(properties))
        # print('s:', s)
        return s

    def save(self):
        name = self.__class__.__name__
        # print('save', self.__dict__)
        # self.__dict__ 是类属性的集合（字典）
        _id = self.db[name].save(self.__dict__)
        # print('_id:', self.db[name])
        # self.id = str(_id)


class Movie(Model):

    @classmethod
    def valid_names(cls):
        names = [
            # (字段名, 类型, 默认值)
            ('name', str, ''),
            ('score', int, 0),
            ('quote', str, ''),
            ('cover_url', str, ''),
            ('ranking', int, 0),
        ]
        return names

    """
    存储电影信息
    """
    # def __init__(self):
    #     self.name = ''
    #     self.score = 0
    #     self.quote = ''
    #     self.cover_url = ''
    #     self.ranking = 0


def movie_from_div(div):
    """
    从一个 div 里面获取到一个电影信息
    """
    e = pq(div)

    # 小作用域变量用单字符
    m = Movie()
    m.name = e('.title').text()
    m.score = e('.rating_num').text()
    m.quote = e('.inq').text()
    m.cover_url = e('img').attr('src')
    m.ranking = e('.pic em').text()
    m.save()
    return m


def movies_from_url(url):
    """
    从 url 中下载网页并解析出页面内所有的电影
    """
    r = requests.get(url)
    page = r.content
    e = pq(page)
    items = e('.item')
    # 调用 movie_from_div 
    movies = [movie_from_div(i) for i in items]
    return movies


def main():
    url = 'https://movie.douban.com/top250'
    movies = movies_from_url(url)
    print('top250 movies', movies)


if __name__ == '__main__':
    main()
