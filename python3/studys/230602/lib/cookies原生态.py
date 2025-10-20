# -*- coding: utf-8 -*-
# time: 2023/7/6 15:25
# file: cookies原生态.py
# author: wht

import requests

HOST = 'http://124.223.33.41:7081'


def login(in_data):
    url = f'{HOST}/api/mgr/loginReq'
    resp = requests.post(url, data=in_data)
    print('响应内容---> ', resp.text)
    print('响应头数据---> ', resp.headers)
    print('响应cookies---> ', resp.cookies)
    return resp.cookies


class Lesson:
    def __init__(self, cookies):
        self.cookie = cookies

    def lesson_list(self, in_data):
        url = f'{HOST}/api/mgr/sq_mgr/'
        resp = requests.get(url, params=in_data, cookies=self.cookie)
        resp.encoding = 'unicode_escape'
        print('课程列表--->', resp.text)


if __name__ == '__main__':
    in_data = {'username': 'auto', 'password': 'sdfsdfsdf'}

    cookie = login(in_data)
    print("cookie:",cookie)
    list_data = {'action': 'list_course', 'pagenum': 1, 'pagesize': 20}

    lesson = Lesson(cookie)
    lesson.lesson_list(list_data)


# 响应内容--->  {"retcode": 0}
# 响应头数据--->  {'Content-Type': 'application/json', 'X-Frame-Options': 'SAMEORIGIN', 'Content-Length': '14', 'Vary': 'Cookie', 'Set-Cookie': 'sessionid=ujimpv3ojr0cr0tleqvc7av8yp55rcrs; HttpOnly; Path=/', 'Date': 'Mon, 13 May 2024 07:11:07 GMT', 'Server': '0.0.0.0'}
# 响应cookies--->  <RequestsCookieJar[<Cookie sessionid=ujimpv3ojr0cr0tleqvc7av8yp55rcrs for 124.223.33.41/>]>
# 课程列表---> {"retcode": 0, "retlist": [{"id": 5117, "name": "前置脚本", "desc": "0001", "display_idx": 0}, {"id": 5179, "name": "全局课程22", "desc": "化学课程", "display_idx": 0}, {"id": 5180, "name": "大学物理1", "desc": "大学物理11", "display_idx": 0}, {"id": 5181, "name": "大学物理1222", "desc": "大学物理11", "display_idx": 0}, {"id": 5182, "name": "55555", "desc": "6666", "display_idx": 0}, {"id": 5183, "name": "555558", "desc": "6666", "display_idx": 0}, {"id": 5194, "name": "初中化学245555", "desc": "初中化学课程2452", "display_idx": 0}, {"id": 5195, "name": "初中化学24523333", "desc": "初中化学课程24523333", "display_idx": 0}, {"id": 3124, "name": "测试sss332", "desc": "test11", "display_idx": 1}, {"id": 5027, "name": "呜呜呜1", "desc": "专门学习哭", "display_idx": 1}, {"id": 5035, "name": "44", "desc": "dtrtgd", "display_idx": 1}, {"id": 5037, "name": "语文", "desc": "语文", "display_idx": 1}, {"id": 5047, "name": "语文123", "desc": "三生三世", "display_idx": 1}, {"id": 5057, "name": "233", "desc": "", "display_idx": 1}, {"id": 5058, "name": "qwq", "desc": "qwq", "display_idx": 1}, {"id": 5064, "name": "test111", "desc": "111", "display_idx": 1}, {"id": 5069, "name": "20240321", "desc": "测试专用", "display_idx": 1}, {"id": 5118, "name": "语文——", "desc": "语文课", "display_idx": 1}, {"id": 5119, "name": "语文2", "desc": "语文课", "display_idx": 1}, {"id": 5120, "name": "语文3", "desc": "语文课", "display_idx": 1}], "total": 76}
