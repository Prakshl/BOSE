from Methods.signin_signup_methods import *

# Object of signup class
signup_obj = Sign_up()
# Object of Common methods class
common_obj = test_common_methods()


# Calling Desired Caps method
def test_desired_capabilities(platformname, udid, platformversion):
    assert common_obj.test_desired_caps(platformname, udid, platformversion)
    time.sleep(2)


# Calling method to click on signup and signup with email
def test_signup_btn():
    assert signup_obj.test_sign_up_btn()
    time.sleep(8)


# Calling method to fill required details
def test_signup_fill():
    assert signup_obj.test_fill_signup_details()
    time.sleep(20)

# Calling function to tick all privacy policy and click on I Agree
def test_privacy_policies():
    assert signup_obj.test_privacy_policy()
    time.sleep(56)


# Calling function to Allow all required permission
def test_allow_allpermissions():
    assert common_obj.test_allow_permissions()
    time.sleep(5)


# Calling function to open profile
def test_open_my_profile():
    assert common_obj.test_open_profile()
    time.sleep(3)


# Signout Function
def test_signout():
    assert common_obj.test_sign_out_btn()
