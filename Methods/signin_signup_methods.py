import time
import string
import random

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import RemoteDriverServerException

from Locators.Locators import *
from Log.log import *

class test_common_methods:

    @log
    def test_desired_caps(self, platformname, udid, platformversion):
        """
        This method is used to create a mobile driver specific to the attached device.
        :param platformname: Mobile device platformname android/ios
        :param udid: UDID of mobile device
        :param platformversion: Mobile device platform verions
        """
        try:
            # Desired Capabilities of my mqbile
            desired_capabilities = {
                "deviceName": "1",
                "platformName": platformname,
                "udid": udid,
                "platformVersion": platformversion,
                "appPackage": "com.bose.bosemusic",
                "appActivity": "com.bose.madrid.SplashScreenActivity"
            }
            global drivers
            drivers = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):

            return False

    # Function to open profile
    @log
    def test_open_profile(self):
        """
        This method is used to open user profile.
        """
        try:
            # Opening the profile
            drivers.find_element_by_id(profile).click()
            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):

            return False

    @log
    # Function for Signout
    def test_sign_out_btn(self):
        """
        This method is used for signing out.
        """
        try:
            # Scrolling to the end for signout
            touch = TouchAction(drivers)
            touch.press(x=484, y=1835).move_to(x=546, y=267).release().perform()
            drivers.find_element_by_id(sign_out).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):

            return False

    @log
    # Function to Allow permissions
    def test_allow_permissions(self):
        """
        This method is used to allow all permissions required by the application.
        """
        try:
            # Allow notificaton
            drivers.find_element_by_id(allow_notification).click()
            time.sleep(10)

            # Allow Location
            drivers.find_element_by_id(allow_location).click()
            time.sleep(3)

            # Allowing from popup
            drivers.find_element_by_id(location_pop_up).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):

            return False


class Sign_up:

    @log
    # Method for sign up
    def test_sign_up_btn(self):
        """
        This method is used to signup using email address.
        """
        try:
            time.sleep(2)
            # Click on Sign up button
            drivers.find_element_by_id(sign_up_btn_1).click()
            time.sleep(35)

            # Clicking on Sign in with email
            drivers.find_element_by_xpath(sign_in_email).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):

            return False

    @log
    # Method to fill details
    def test_fill_signup_details(self):
        """
        This method is used to fill signup details.
        """

        # Generate random email id
        email_id = string.ascii_lowercase[:20]
        email_id = ''.join(random.choice(email_id) for i in range(7))
        email_id = email_id + '@gmail.com'

        try:
            # Writing Email ID
            drivers.find_element_by_xpath(txt_email).send_keys(email_id)
            time.sleep(1)

            # Writing Password
            drivers.find_element_by_xpath(txt_password).send_keys("Test&mad")

            # Writing User Name
            drivers.find_element_by_xpath(txt_username).send_keys("Test")

            # Writing Last name
            drivers.find_element_by_xpath(txt_last_name).send_keys("Mad")

            # Opening Dropdown
            drivers.find_element_by_xpath(drop_down).click()
            time.sleep(3)

            touch = TouchAction(drivers)

            # Looping elements until India not shown into frame (15 times)
            for i in range(15):
                touch.press(x=475, y=1551).move_to(x=459, y=284).release().perform()
                time.sleep(2)

            # Selecting the India from Dropdown menu
            drivers.find_element_by_xpath(drp_dwn_india).click()

            # click on SignUp button
            drivers.find_element_by_xpath(sign_up_btn_2).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):

            return False

    @log
    # Method to Check all privacy radio button and click on I Agree
    def test_privacy_policy(self):
        """
        This method is used to accept privacy and policy required by the application.
        """
        try:
            # Terms of use
            drivers.find_element_by_xpath(terms_of_use).click()

            # Privacy Policy
            drivers.find_element_by_xpath(privacy_policy).click()

            # End User Licence Agreement
            drivers.find_element_by_xpath(licence_agreement).click()

            # I Agree
            drivers.find_element_by_xpath(i_agree).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):

            return False


# Class for Login contains all Login functions
class Login:

    @log
    # Method for signin
    def test_sign_in_btn(self):
        """
        This method is used for login using email address.
        """
        try:
            # Clicking on 'Sign in'
            drivers.find_element_by_id(sign_in_btn_1).click()
            time.sleep(30)

            # Clicking on 'Sign in with Email'
            drivers.find_element_by_xpath(sign_in_email_1).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):

            return False

    @log
    # Method to write Login details
    def test_fill_login_details(self):
        """
        This method is used to fill login details.
        """
        try:
            # Writing Login ID
            drivers.find_element_by_xpath(txt_email).send_keys("abcc@gmail.com")

            # Writing Password
            drivers.find_element_by_xpath(txt_password).send_keys("Prak@123")

            # Clicking on Sign in
            drivers.find_element_by_xpath(sign_in_btn_2).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):

            return False
