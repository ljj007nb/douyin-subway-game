# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 
# @Author  :
import uuid
import live_url as liveUrl

from playwright.sync_api import sync_playwright as playwright


def filterResponse(response):
    if 'https://live.douyin.com/webcast/im/fetch/' in response.url:
        # print("<<", response.url)
        with open('./douyinLiveFile/' + uuid.uuid4().hex, 'wb') as file:
            file.write(response.body())
    else:
        # print("--", response.url)
        pass
    return response


def log_request(intercepted_request):
    print("a request was made:", intercepted_request.url)


def run(pw):
    browser = pw.webkit.launch(headless=True)
    page = browser.new_page()

    page.on("response", filterResponse)
    # 直播间 地址  你们自己写
    page.goto(liveUrl.url())
    return page




def startMonitoring():
    with playwright() as pw:
        page = run(pw)
        #直播间停留时间 单位ms 需要你们自己敲定  也可以永久驻留
        page.wait_for_timeout(100000000)


startMonitoring()
# https://live.douyin.com/webcast/im/fetch/
