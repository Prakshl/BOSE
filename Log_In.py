import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap = {
    "deviceName": "1",
    "platformName": "Android",
    "udid": "33766e229904",
    "platformVersion": "7.0",
    "appPackage": "com.bose.bosemusic",
    "appActivity": "com.bose.madrid.SplashScreenActivity"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# Clicking on 'Sign in'
driver.find_element_by_id("com.bose.bosemusic:id/login_button").click()
time.sleep(10)

# Clicking on 'Sign in with Email'
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[2]").click()
time.sleep(3)

# Writing Login ID
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[2]/android.widget.EditText"). \
    send_keys("abcc@gmail.com")

# Writing Password
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[3]/android.widget.EditText"). \
    send_keys("Prak@123")

# Clicking on Sign in
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[5]/android.widget.Button").click()
time.sleep(3)
"""
# These three Policies displayed only once

# Check on Terms of use
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[4]").click()
# check on Privacy Policy
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[5]").click()

# Check on End User License Agreement
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[6]").click()

# Clicking I Agree
# driver.find_element_by_id("gigya-privacy-accept").click()
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit"
                             ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                             "/android.view.View/android.view.View[7]/android.widget.Button").click()
"""
time.sleep(8)
driver.find_element_by_id("com.bose.bosemusic:id/primary_button").click()

time.sleep(10)
# Allow Location
driver.find_element_by_id("com.bose.bosemusic:id/round_button").click()
time.sleep(3)

# Allowing from popup
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(5)

# Open Account Setting
driver.find_element_by_id("com.bose.bosemusic:id/item_account_settings").click()
time.sleep(2)

touch = TouchAction(driver)
# Scrolling to the end for signout
touch.press(x=442, y=1872).move_to(x=559, y=142).release().perform()

# signout
driver.find_element_by_id("com.bose.bosemusic:id/button").click()
