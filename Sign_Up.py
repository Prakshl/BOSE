from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

# Desired Capabilities of my mobile
desired_cap = {
    "deviceName": "1",
    "platformName": "Android",
    "udid": "33766e229904",
    "platformVersion": "7.0",
    "appPackage": "com.bose.bosemusic",
    "appActivity": "com.bose.madrid.SplashScreenActivity"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
time.sleep(4)

# Click on Sign up button
driver.find_element_by_id("com.bose.bosemusic:id/register_button").click()
time.sleep(28)

# Click on Sign up with Email
driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
    ".LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
    ".view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]").click()
time.sleep(12)

# Writing Email ID
driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
    ".LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
    ".view.View/android.view.View/android.view.View/android.view.View/android.view.View["
    "2]/android.widget.EditText").send_keys(
    "abcc@gmail.com")

# Writing Password
driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
    ".LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
    ".view.View/android.view.View/android.view.View/android.view.View/android.view.View["
    "3]/android.widget.EditText").send_keys(
    "Prak@123")

# Writing User Name
driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
    ".LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
    ".view.View/android.view.View/android.view.View/android.view.View/android.view.View["
    "4]/android.widget.EditText").send_keys(
    "Prakshal")

# Writing Last name
driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
    ".LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
    ".view.View/android.view.View/android.view.View/android.view.View/android.view.View["
    "5]/android.widget.EditText").send_keys(
    "Shah")

# Opening Dropdown
driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
    ".LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
    ".view.View/android.view.View/android.view.View/android.view.View/android.view.View["
    "6]/android.widget.Spinner").click()
time.sleep(3)

touch = TouchAction(driver)

# Looping elements until India not shown into frame (15 times)
for i in range(15):
    touch.press(x=475, y=1551).move_to(x=459, y=284).release().perform()
    time.sleep(2)

# Selecting the India from Dropdown menu
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]").click()

# click on SignUp button
driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
    ".LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android"
    ".view.View/android.view.View/android.view.View/android.view.View/android.view.View["
    "8]/android.widget.Button").click()

time.sleep(15)

# Terms of use
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[4]/android.view.View/android.view.View").click()

# Privacy Policy
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[5]/android.view.View/android.view.View").click()

# End User Licence Agreement
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[6]/android.view.View/android.view.View").click()
time.sleep(1)

# I Agree
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[7]/android.widget.Button").click()
time.sleep(55)

# Allow Notifications window (Clicking on 'GOT IT')
driver.find_element_by_id("com.bose.bosemusic:id/primary_button").click()
time.sleep(2)

# Allowing Location Access
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                             ".FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup["
                             "1]/android.widget.FrameLayout/android.widget.TextView").click()
time.sleep(2)

# Allowing Location Access which shown by mobile
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(3)

# Opening the profile
driver.find_element_by_id("com.bose.bosemusic:id/item_account_settings").click()
time.sleep(6)

# Scrolling to the end for signout
touch.press(x=484, y=1835).move_to(x=546, y=267).release().perform()
time.sleep(1)

# Sign out
driver.find_element_by_id("com.bose.bosemusic:id/button").click()

