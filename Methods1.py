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


# Class for Signup, it contains all SignUp functions
class Sign_up:

    # Method for sign up
    def sign_up_btn(self):
        time.sleep(2)
        # Click on Sign up button
        drivers.find_element_by_id("com.bose.bosemusic:id/register_button").click()
        time.sleep(35)

        # Clicking on Sign in with email
        drivers.find_element_by_xpath('//*[contains(@text, "Sign up with Email")]').click()

    # Method to fill details
    def fill_signup_details(self):
        # Writing Email ID
        drivers.find_element_by_xpath("//android.view.View[2]/android.widget.EditText").send_keys("zvbzw@gmail.com")
        time.sleep(1)

        # Writing Password
        drivers.find_element_by_xpath("//android.view.View[3]/android.widget.EditText").send_keys(
            "Prak@123")

        # Writing User Name
        drivers.find_element_by_xpath(
            "//android.view.View[4]/android.widget.EditText").send_keys(
            "Prakshal")

        # Writing Last name
        drivers.find_element_by_xpath(
            "//android.view.View[5]/android.widget.EditText").send_keys(
            "Shah")

        # Opening Dropdown
        drivers.find_element_by_xpath("//*[contains(@text, 'United States')]").click()
        time.sleep(3)

        touch = TouchAction(drivers)

        # Looping elements until India not shown into frame (15 times)
        for i in range(15):
            touch.press(x=475, y=1551).move_to(x=459, y=284).release().perform()
            time.sleep(2)

        # Selecting the India from Dropdown menu
        drivers.find_element_by_xpath("//*[contains(@text,'India')]").click()

        # click on SignUp button
        drivers.find_element_by_xpath("//*[contains(@text,'Sign Up')]").click()

    # Method to Check all privacy radio button and click oon I Agree
    def privacy_policy(self):
        # Terms of use
        drivers.find_element_by_xpath("//android.view.View[4]").click()

        # Privacy Policy
        drivers.find_element_by_xpath("//android.view.View[5]").click()

        # End User Licence Agreement
        drivers.find_element_by_xpath("//android.view.View[6]").click()

        # I Agree
        drivers.find_element_by_xpath("//android.view.View[7]").click()

# Function to open Profile
def open_profile():
    # Opening the profile
    drivers.find_element_by_id("com.bose.bosemusic:id/item_account_settings").click()

# Function for Signout
def sign_out_btn():
    # Scrolling to the end for signout
    touch = TouchAction(drivers)
    touch.press(x=484, y=1835).move_to(x=546, y=267).release().perform()
    drivers.find_element_by_id("com.bose.bosemusic:id/button").click()


# Function to Allow permissions
def allow_permissions():
    # Allow notificaton
    drivers.find_element_by_id("com.bose.bosemusic:id/primary_button").click()
    time.sleep(10)
    # Allow Location
    drivers.find_element_by_id("com.bose.bosemusic:id/round_button").click()
    time.sleep(3)

    # Allowing from popup
    drivers.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    time.sleep(5)


# Class for Login contains all Login functions
class Login:

    # Method for login
    def sign_in_btn(self):
        # Clicking on 'Sign in'
        drivers.find_element_by_id("com.bose.bosemusic:id/login_button").click()
        time.sleep(30)
        # Clicking on 'Sign in with Email'
        drivers.find_element_by_xpath("//android.view.View[2]").click()

    # Method to write Login details
    def fill_login_details(self):
        # Writing Login ID
        drivers.find_element_by_xpath("//android.view.View[2]/android.widget.EditText"). \
            send_keys("abcc@gmail.com")

        # Writing Password
        drivers.find_element_by_xpath("//android.view.View[3]/android.widget.EditText"). \
            send_keys("Prak@123")

        # Clicking on Sign in
        drivers.find_element_by_xpath("//android.view.View[5]/android.widget.Button").click()