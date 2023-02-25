import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from setting import *


def wait(func):
    wait_time = 1

    def inside_func(*args, **kwargs):
        time.sleep(wait_time)
        return func(*args, **kwargs)

    return inside_func


class skip_lesson:

    @staticmethod
    def get_browser():
        """
        获得一个有界面的浏览器对象
        :return:browser
        """
        return webdriver.Chrome()

    @staticmethod
    def get_on_ui_browser():
        """
        获得一个无界面的浏览器对象
        :return: browser
        """
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片
        browser = webdriver.Chrome(chrome_options=chrome_options)
        return browser

    def find_all_element(self, XPATH, wait_time=10):
        """
        寻找满足条件的所有控件
        :param XPATH: xpath语句
        :param wait_time: 最长等待时间
        :return: 控件
        """
        return WebDriverWait(self.browser, wait_time).until(EC.presence_of_all_elements_located((By.XPATH, XPATH)))

    def find_element(self, XPATH, wait_time=10):
        """
        寻找控件
        :param XPATH: xpath语句
        :param wait_time: 最长等待时间
        :return: 控件
        """
        return WebDriverWait(self.browser, wait_time).until(EC.presence_of_element_located((By.XPATH, XPATH)))

    def add_cookie(self):
        """
        为浏览器添加cookie信息,并且刷新界面
        :return: None
        """

        for cookie in COOKIE_LIST:
            self.browser.add_cookie(cookie)

        self.browser.refresh()

    def click_element(self, element):
        """
        用于点击定位到的元素
        :param element:元素
        :return: None
        """
        self.browser.execute_script("arguments[0].click()", element)

    def sign_in(self):
        """
        实现用户登录
        :return: None
        """
        # 输入用户名
        self.input = self.find_element(SIGN_IN_USER)
        self.input.send_keys(USER_NAME)

        # 输入用户密码
        self.password = self.find_element(SIGN_IN_PASSWORD)
        self.password.send_keys(PASSWORD)

        # 点击登录按钮
        self.sign_in_button = self.find_element(SIGN_IN_BUTTON)
        self.click_element(self.sign_in_button)

        input()
        # 打印最新的有效cookie
        print(self.browser.get_cookies())

    def get_all_lesson(self):
        """
        获取当前所有的课程信息
        :return: lessons
        """
        self.lessons = self.find_all_element(LESSONS)

    @wait
    def close_sound(self):
        """
        用于关闭声音
        :return:None
        """
        self.sound = self.find_element(SOUND)
        self.click_element(self.sound)

    def play_is(self):
        """
        获取当前视频的播放状态
        :return: None
        """
        button = self.find_element(PLAY)
        return False if button.get_attribute('class') == 'playButton' else True

    def close_ad(self):
        """
        关闭广告
        :return:None
        """
        time.sleep(1)

        ad1 = self.find_element(AD1)
        self.click_element(ad1)
        time.sleep(1)

        ad2 = self.find_element(AD2)
        self.click_element(ad2)
        time.sleep(1)

    def get_all_video(self):
        """
        获取当前窗口下的所有视频
        :return: videos
        """
        videos = self.find_all_element(CLASS)
        names = [x.text for x in self.find_all_element(CLASS_NAME)]

        return zip(videos, names)

    def play_lesson(self):
        """
        播放该课程
        :return:None
        """
        try:
            self.close_ad()  # 关闭广告
        except:
            pass

        classes = self.get_all_video()  # 获取所有的视频课程
        for lesson, name in classes:
            print(f"正在播放视频:《{name}》")
            self.click_element(lesson)      # 进入视频界面
            time.sleep(10)
            self.close_sound()  # 关闭声音
            time.sleep(10)
            if self.play_is():  # 视频处于暂停状态时，开启播放
                play_button = self.find_element(PLAY)
                self.click_element(play_button)

            time.sleep(10)
            print(f'视频《{name}》已播放结束')

            input()

    def start(self):
        """
        开始所有刷课
        :return:None
        """
        self.get_all_lesson()  # 获取当前界面的所有课程
        for lesson in self.lessons:
            self.click_element(lesson)  # 进入网课
            time.sleep(1)
            self.play_lesson()

    def __init__(self, update=False):
        self.browser = self.get_browser()
        self.browser.implicitly_wait(10)  # 设置静态等待时间

        self.browser.get(URL)

        if update:
            self.sign_in()  # 登录
        else:
            self.add_cookie()
            self.start()

        input()


if __name__ == '__main__':
    root = skip_lesson()
