"""
环境配置文件
"""
URL = 'https://onlineweb.zhihuishu.com/onlinestuh5'

USER_NAME = '13819501004'
PASSWORD = 'Ranok666'

COOKIE_LIST = [
    {'domain': '.zhihuishu.com', 'expiry': 1677561740, 'httpOnly': False, 'name': 'exitRecod_EQNr9WOJ', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '2'},
    {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'jt-cas', 'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': 'eyJraWQiOiJFRjRGMjJDMC01Q0IwLTQzNDgtOTY3Qi0wMjY0OTVFN0VGQzgiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJjb20uemhpaHVpc2h1IiwiYXVkIjoiQ0FTIiwic3ViIjoi6YeR5q2jIiwiaWF0IjoxNjc3MzAyNTQwLCJleHAiOjE2NzczODg5NDAsImp0aSI6ImFlOTg2NTIyLWU2MmEtNDFlNy05MTVhLTRjNTE4MzY3ZTc4YyIsInVpZCI6ODA3NTQ3MjgzfQ.RpySpar1aCURD0XxYhCw1t3XxG_pAM5UGMipRYtbpVBXM9BRUDy3LveAp9rJ2oLv-AR5dgNAaqOZlzpJSIDYQA'},
    {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'CASLOGC', 'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': '%7B%22realName%22%3A%22%E9%87%91%E6%AD%A3%22%2C%22myuniRole%22%3A0%2C%22myinstRole%22%3A0%2C%22userId%22%3A807547283%2C%22headPic%22%3A%22https%3A%2F%2Fimage.zhihuishu.com%2Fgxk%2Fzd%2Fandroid%2F202110%2F8F3BDE65613C54451791E7E97629B44A_s3.png%22%2C%22uuid%22%3A%22EQNr9WOJ%22%2C%22mycuRole%22%3A0%2C%22username%22%3A%22f61d2e37cdf0429f985bdafc78b4817b%22%7D'},
    {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'CASTGC', 'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': 'TGT-309210-boloZEmszeanpqiV3prhf5y9wUcFBZNjSbVTmj69bOA2BLjRxP-passport.zhihuishu.com'}
]

SIGN_IN_BUTTON = '//span[@class="wall-sub-btn"]'
SIGN_IN_USER = '//input[@type="text" and @name="username"]'
SIGN_IN_PASSWORD = '//input[@type="password" and @name="password"]'

LESSONS = '//div[@class="item-left-course"]'
AD1 = '//i[@class="iconfont iconguanbi"]'
AD2 = '//a[@href="javascript:void(0);"]'

SOUND = '//div[@class="volumeIcon"]'
PLAY = '//div[@id="playButton"]'

CLASS = '//div[@class="fl cataloguediv-c"]'
CLASS_NAME = '//span[@class="catalogue_title"]'