from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


def desired_caps():
    # Desired Capabilities of my mobile
    desired_capabilities = {
        "deviceName": "1",
        "platformName": "Android",
        "udid": "33766e229904",
        "platformVersion": "7.0",
        "appPackage": "com.bose.bosemusic",
        "appActivity": "com.bose.madrid.SplashScreenActivity"
    }
    global drivers
    drivers = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)



class Sign_up:

    # Method for sign up
    def sign_up_btn(self):
        time.sleep(2)
        # Click on Sign up button
        drivers.find_element_by_id("com.bose.bosemusic:id/register_button").click()
        # drivers.find_element_by_xpath("//div[@class='android.view.View' and [@text,'Create My Bose']").click()
        # drivers.find_element_by_xpath("//div(@text, 'Create My Bose')")
        time.sleep(35)
        # Clicking on Sign in with email
        # drivers.find_element_by_xpath('//android.view.View [@text, "Sign up with Email"]').click()
        drivers.find_element_by_xpath("//android.view.View[@index,'2']").click()

    def fill_signup_details(self):
        # Writing Email ID
        drivers.find_element_by_xpath(
            "//*android.view.View/android.view.View[2]/android.widget.EditText").send_keys(
            "abcc@gmail.com")

        # Writing Password
        drivers.find_element_by_xpath(
            "//*android.view.View/android.view.View[3]/android.widget.EditText").send_keys(
            "Prak@123")

        # Writing User Name
        drivers.find_element_by_xpath(
            "//*android.view.View/android.view.View[4]/android.widget.EditText").send_keys(
            "Prakshal")

        # Writing Last name
        drivers.find_element_by_xpath(
            "//*android.view.View/android.view.View[5]/android.widget.EditText").send_keys(
            "Shah")

        # Opening Dropdown
        drivers.find_element_by_xpath(
            "//*android.view.View/android.view.View[6]/android.widget.Spinner").click()
        time.sleep(3)

        touch = TouchAction(drivers)

        # Looping elements until India not shown into frame (15 times)
        for i in range(15):
            touch.press(x=475, y=1551).move_to(x=459, y=284).release().perform()
            time.sleep(2)

        # Selecting the India from Dropdown menu
        drivers.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                     ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                     ".FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]").click()

        # click on SignUp button
        drivers.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
            ".view.View/android.view.View/android.view.View/android.view.View/android.view.View["
            "8]/android.widget.Button").click()

    def sign_up_submit_btn(self):
        # click on SignUp button
        drivers.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
            ".view.View/android.view.View/android.view.View/android.view.View/android.view.View["
            "8]/android.widget.Button").click()

    def privacy_policy_radiobtn(self):
        # Terms of use
        drivers.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                     ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                                     ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                                     "/android.view.View/android.view.View[4]/android.view.View/android.view.View").click()

        # Privacy Policy
        drivers.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                     ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                                     ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                                     "/android.view.View/android.view.View[5]/android.view.View/android.view.View").click()

        # End User Licence Agreement
        drivers.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                     ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                                     ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                                     "/android.view.View/android.view.View[6]/android.view.View/android.view.View").click()

    def I_agree_btn(self):
        # I Agree
        drivers.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                     ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                                     ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                                     "/android.view.View/android.view.View[7]/android.widget.Button").click()

    def allow_permissions_signup(self):
        # Allow Notifications window (Clicking on 'GOT IT')
        drivers.find_element_by_id("com.bose.bosemusic:id/primary_button").click()
        # Allowing Location Access
        drivers.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                     ".FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup["
                                     "1]/android.widget.FrameLayout/android.widget.TextView").click()

        # Allowing from popup
        drivers.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

    def open_profile(self):
        # Opening the profile
        drivers.find_element_by_id("com.bose.bosemusic:id/item_account_settings").click()

    def sign_out_btn(self):
        # Scrolling to the end for signout
        touch = TouchAction(drivers)
        touch.press(x=484, y=1835).move_to(x=546, y=267).release().perform()
        drivers.find_element_by_id("com.bose.bosemusic:id/button").click()


# Method for login
def sign_in_btn():
    # Clicking on 'Sign in'
    drivers.find_element_by_id("com.bose.bosemusic:id/login_button").click()
    time.sleep(10)
    # Clicking on 'Sign in with Email'
    drivers.find_element_by_xpath("//*android.view.View/android.view.View[2]").click()


def fill_login_details():
    # Writing Login ID
    drivers.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                                 ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                                 "/android.view.View/android.view.View[2]/android.widget.EditText"). \
        send_keys("abcc@gmail.com")

    # Writing Password
    drivers.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                                 ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                                 "/android.view.View/android.view.View[3]/android.widget.EditText"). \
        send_keys("Prak@123")


def login_btn():
    # Clicking on Sign in
    drivers.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                                 ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                                 "/android.view.View/android.view.View[5]/android.widget.Button").click()


def allowing_permissions_login():
    # Allow notificaton
    drivers.find_element_by_id("com.bose.bosemusic:id/primary_button").click()
    # Allow Location
    drivers.find_element_by_id("com.bose.bosemusic:id/round_button").click()
    # Allowing from popup
    drivers.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
