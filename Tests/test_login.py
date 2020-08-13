from Methods.signin_signup_methods import *

# Object of Login class
login_obj = Login()
# Object of Common methods class
common_obj = test_common_methods()


# Calling Desired Caps method
def test_desired_capabilities(platformname, udid, platformversion):
    assert common_obj.test_desired_caps(platformname, udid, platformversion)


# Calling method to click on signin and sign with email
def test_login_btn():
    assert login_obj.test_sign_in_btn()
    time.sleep(3)

# Calling method to write Login details

def test_login_fill():
    assert login_obj.test_fill_login_details()
    time.sleep(25)


# Calling method to Allow all required permission
def test_allow_all_permission():
    assert common_obj.test_allow_permissions()
    time.sleep(5)

# Calling method to open profile
def test_open_my_profile():
    assert common_obj.test_open_profile()
    time.sleep(4)

# Signout method
def test_sign_out():
    assert common_obj.test_sign_out_btn()
