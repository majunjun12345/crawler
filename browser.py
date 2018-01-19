import platform

import os
from time import sleep
# 最早的时候大家都会使用 Phantomjs 来实现headless，但是多多少少会有一些不足的地方。
# 现在 Chrome 和 Firefox 都已经提供了相应的 headless 模式，而且 Splinter 也已经集成。
from splinter import Browser


# 将驱动加入环境变量，也可以手动加入，也可以把驱动放置于 python 的环境变量中
def add_chrome_webdriver():
    print('platform.system():',platform.system())
    working_path = os.getcwd()
    print('working_path:', working_path)
    library = 'library'
    path = os.path.join(working_path, library)
    print('path:', path)
    os.environ['PATH'] += '{}{}{}'.format(os.pathsep, path, os.pathsep)
    print(os.environ['PATH'])


def find_website():
    # 默认是火狐浏览器，部署在服务器打开无头模式，本地测试可以打开图形界面
    # with Browser('chrome', headless=True) as browser:
    with Browser() as browser:
        # Visit URL
        url = "http://www.baidu.com"
        browser.visit(url)

        input = browser.find_by_css('#kw')
        input.fill('知乎')

        # Find and click the 'search' button
        button = browser.find_by_css('#su')
        # Interact with elements
        button.click()

        if browser.is_text_present('发现更大的世界'):
            print("Yes, the official website was found!")
        else:
            print("No, it wasn't found... We need to improve our SEO techniques")


def main():
    add_chrome_webdriver()
    find_website()


if __name__ == '__main__':
    main()
