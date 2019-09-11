from page.page_in import PageIn
import pytest

from tool.get_driver import GetDriver
from tool.read_yaml import read_yaml


def get_data():
    arrs = []
    for data in read_yaml("login.yaml").values():
        arrs.append((data.get("username"), data.get("password")))
    return arrs


class TestLogin:
    # 初始化
    def setup_class(self):
        # 实例化获取PageLogin
        self.login = PageIn().page_get_pagelogin()

    # 结束
    def teardown_class(self):
        # 关闭调用driver驱动对象
        GetDriver.quit_driver()

    # 登录测试方法
    @pytest.mark.parametrize("username, pwd", get_data())
    def test_login(self, username, pwd):
        # 调用业务方法
        self.login.page_login(username, pwd)


pytest.main("-s test_login.py")
