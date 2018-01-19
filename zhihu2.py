# 动态爬虫
# 注入 js 事件，不断滚动鼠标
# 直到找到目标数据
# 需要驱动（library），且加入环境变量中

import config

import platform

import os

from splinter import Browser


def add_chrome_webdriver():
    print(platform.system())
    working_path = os.getcwd()
    library = 'library'
    path = os.path.join(working_path, library)
    os.environ['PATH'] += '{}{}{}'.format(os.pathsep, path, os.pathsep)
    print(os.environ['PATH'])


def add_cookie(browser):
    for part in config.cookie.split('; '):
        kv = part.split('=')
        d = {kv[0]: kv[1]}
        browser.cookies.add(d)
    print(browser.cookies.all())


def scroll_to_end(browser):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')


def start_crawler():
    # 火狐浏览器的配置文件，里面有各网站的密码等
    option = config.profile
    # 垃圾 chrome 有 bug https://bugs.chromium.org/p/chromium/issues/detail?id=617931
    # 不能 --user-data-dir 和 --headless 一起用
    # 改回用 cookie

    with Browser(profile=option) as browser:
        url = "https://www.zhihu.com"
        # 先访问一个 url，才能设置这个 url 对应的 cookie
        browser.visit(url)
        # add_cookie(browser)
        # 设置好 cookie 后，刷新页面即可进入登录状态
        browser.reload()

        print('browser.html1:', browser.html)
        scroll_to_end(browser)
        found = False

        while not found:
            print('loop')
            found = browser.is_text_present('1 天前')
            if found:
                print('拿到了最近1天动态')
                print('browser.html2:', browser.html)
                break
            else:
                scroll_to_end(browser)


def main():
    add_chrome_webdriver()
    start_crawler()


if __name__ == '__main__':
    main()
