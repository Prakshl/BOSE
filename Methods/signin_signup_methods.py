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


class common_methods:

    @log
    def desired_caps(self, platformname, udid, platformversion):
        """
        This method is used to create a mobile driver specific to the attached device.
        :param platformname: Mobile device platformname android/ios
        :param udid: UDID of mobile device
        :param platformversion: Mobile device platform verions
        """

        try:
            # Desired Capabilities of my mobile
            desired_capabilities = {
                "deviceName": "Samsung",
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
    def open_profile(self):
        """
        This method is used to open user profile.
        """

        try:

            # Opening the profile
            drivers.find_element_by_xpath(profile).click()
            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False

    @log
    # Function for Signout
    def sign_out_btn(self):
        """
        This method is used for signing out.
        """

        try:

            # Swipe to the end for signout
            for i in range(3):
                drivers.swipe(100, 700, 100, 150)

            # Click on signout button
            drivers.find_element_by_id(sign_out).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False

    @log
    # Function to Allow permissions
    def allow_permissions(self):
        """
        This method is used to allow all permissions required by the application.
        """

        try:

            # Allow notification
            drivers.find_element_by_id(allow_notification).click()
            time.sleep(10)

            # Allow Location
            drivers.find_element_by_id(allow_location).click()
            time.sleep(3)

            # Allowing from popup
            drivers.find_element_by_id(location_pop_up).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False

    def change_name(self):
        """
        This method is used to change first name and last name
        """

        try:

            # Open account info. activity
            drivers.find_element_by_id(account).click()
            time.sleep(10)

            # Change First name
            first_name = drivers.find_element_by_xpath(change_first_name)
            first_name.clear()
            first_name.send_keys('Jacob')

            # Change Last name
            last_name = drivers.find_element_by_xpath(change_last_name)
            last_name.clear()
            last_name.send_keys('Reddy')

            # Click on submit button
            drivers.find_element_by_xpath(submit).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False

    def manage_product(self):
        """
        This method is used to add new boss product or manage existing product.
        """

        try:

            # Click on manage product
            drivers.find_element_by_xpath(inside_manage_product).click()
            time.sleep(1)

            # Click on edit button
            drivers.find_element_by_id(inside_manage_product_edit).click()
            time.sleep(3)

            # Close editing
            drivers.find_element_by_accessibility_id('Close').click()

            # Click on add product
            drivers.find_element_by_id(inside_add_product).click()
            time.sleep(1)

            # Click on Headphones
            drivers.find_element_by_id(inside_headphone).click()
            time.sleep(2)

            # Allow Permission to turn on bluetooth
            drivers.find_element_by_id(inside_bluetooth).click()
            time.sleep(5)

            # Click on back element
            back()
            time.sleep(2)

            # Click on Speakers and soundbars
            drivers.find_element_by_id(inside_speaker).click()
            time.sleep(3)

            # Click on back element
            back()
            time.sleep(2)

            # Back to Home Activity
            drivers.find_element_by_accessibility_id('Back to My Products').click()
            time.sleep(2)

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False

    def manage_music(self):
        """
        This function is used to manage music services
        """

        try:

            # Click on manage music element
            drivers.find_element_by_xpath(manage_music).click()
            time.sleep(2)

            # Click on add new service
            drivers.find_element_by_xpath(add_new_service).click()
            time.sleep(2)

            # Swipe to find element
            drivers.swipe(100, 700, 100, 150)

            # Call back function to go back
            back()
            time.sleep(2)

            # Click on on learn more element
            drivers.find_element_by_xpath(learn_more).click()
            time.sleep(1)

            # Click on anonymous account
            drivers.find_element_by_xpath(tunein_account).click()
            time.sleep(2)

            # Call back function again to go back
            back()
            time.sleep(2)

            # Call back function again to go back
            back()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False

    def notification(self):

        """
        This function is used turn off or turn on notification
        """

        try:

            # Swipe till element is displayed on screen
            drivers.swipe(100, 700, 100, 150)
            time.sleep(2)

            # Click on notification switch button
            drivers.find_element_by_id(notification).click()
            time.sleep(2)

            # Click on dismiss button
            drivers.find_element_by_id(notification_dismiss).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False

    def data_preference(self):
        """
        This method is used to turn off or turn on data analysis from settings
        """

        try:

            # Swipe till element is displayed on screen
            for i in range(2):
                drivers.swipe(100, 700, 100, 150)

            # Click on data preference element
            drivers.find_element_by_xpath(data_preference).click()
            time.sleep(2)

            # Click to turn on or off app analysis
            drivers.find_element_by_id(app_analysis).click()
            back()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False

    def check_version(self):
        # cmd = "adb shell dumpsys package your.app.package.name.here |grep versionName"
        # Process process = null;

        try:

            app_version = drivers.find_element_by_xpath(application_version)
            version_text = app_version.text
            print(version_text)

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False


def back():
    """This method is used to click on go back element"""
    drivers.find_element_by_accessibility_id('Back').click()


def screenshot():
    # Make screenshot folder and save screenshot
    newpath = os.path.join(os.getcwd(), 'Screenshot')
    os.makedirs(newpath, exist_ok=True)
    ss_time = time.strftime('%d_%m_%Y_%H%M%S')
    activity_name = drivers.current_activity
    drivers.save_screenshot(newpath + '/' + activity_name + ss_time + '.png')


class Sign_up:

    @log
    # Method for sign up
    def sign_up_btn(self):
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
            screenshot()
            return False

    @log
    # Method to fill details
    def fill_signup_details(self):
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

            # Looping elements until India not shown into frame (23 times)
            for i in range(23):
                drivers.swipe(100, 700, 100, 150)
                time.sleep(2)

            # Selecting the India from Dropdown menu
            drivers.find_element_by_xpath(drp_dwn_india).click()

            # click on SignUp button
            drivers.find_element_by_xpath(sign_up_btn_2).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False

    @log
    # Method to Check all privacy radio button and click on I Agree
    def privacy_policy(self):
        """
        This method is used to accept privacy and policy required by the application.
        """

        try:
            # Terms of use
            drivers.find_element_by_xpath(terms_of_use).click()

            # Privacy Policy
            drivers.find_element_by_xpath(privacy_policy).click()

            # End User License Agreement
            drivers.find_element_by_xpath(licence_agreement).click()

            # I Agree
            drivers.find_element_by_id(i_agree).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False


# Class for Login contains all Login functions
class Login:

    @log
    # Method for signin
    def sign_in_btn(self):
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
            screenshot()
            return False

    @log
    # Method to write Login details
    def fill_login_details(self):
        """
        This method is used to fill login details.
        """

        try:
            # Writing Login ID
            drivers.find_element_by_xpath(txt_email).send_keys("abcc@gmail.com")

            # Writing Password
            drivers.find_element_by_xpath(txt_password).send_keys("Prak@123")

            # Hide keyboard
            drivers.hide_keyboard()

            # Clicking on Sign in
            drivers.find_element_by_xpath(sign_in_btn_2).click()

            return True

        except (NoSuchElementException, WebDriverException, RemoteDriverServerException):
            screenshot()
            return False
