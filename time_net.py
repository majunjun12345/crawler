import os
import requests
from pyquery import PyQuery as pq


class Model():
    """
    基类, 用来显示类的信息
    """

    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Movie(Model):
    """
    存储电影信息
    """

    def __init__(self):
        self.name = ''
        self.jury = ''
        self.score = 0
        self.quote = ''
        self.cover_url = ''
        self.ranking = 0


def cached_page(url):
    folder = 'cached'
    if not os.path.exists(folder):
        os.makedirs(folder)

    # 为什么不能用find（）
    if '-' in url:
        filename = '{}.html'.format(url.split('-', 1)[-1].split('.', 1)[0])
        # print(filename)
    else:
        filename = '1.html'
        # print(filename)

    # 妈的
    path = os.path.join(folder, filename)
    # path.replace('\\', '/')
    # print(path)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
            return s
    else:
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
        return r.content


def movie_from_li(li):
    e = pq(li)
    m = Movie()
    # 怎么找到父元素众多类子元素中的第一个
    m.name = e('.mov_con').find('.px14').find('a').text()
    m.jury = e('.mov_point').find('p').text()
    # 怎么精简，主演怎么合并到一起
    m.score = e('.mov_point').find('.total').text() + e('.mov_point').find('.total2').text()
    # print(e('.mov_point').find('.total').text() + e('.mov_point').find('.total2').text())
    m.quote = e('.mt3').text()
    m.cover_url = e('img').attr('src')
    m.ranking = e('.number').find('em').text()
    return m


def movies_from_url(url):
    page = cached_page(url)
    e = pq(page)
    # find（）方法可以返回一个列表（如果找的元素较多的话）
    lis = e('#asyncRatingRegion').find('li')
    # print(lis)
    movies = [movie_from_li(i) for i in lis]
    return movies


def main():
    for i in range(1, 11):
        if i == 1:
            url = 'http://www.mtime.com/top/movie/top100/'
        else:
            url = 'http://www.mtime.com/top/movie/top100/index-{}.html'.format(i)
        movies = movies_from_url(url)


    # url = 'http://www.mtime.com/top/movie/top100/'
    # movies = movies_from_url(url)
        print('top100 movies', movies)


if __name__ == '__main__':
    main()
