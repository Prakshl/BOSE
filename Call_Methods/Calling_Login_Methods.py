import sys
sys.path.insert(0, r'C:\Users\Disha\PycharmProjects\Testing')
from Test_Methods import Testing_Methods

# Calling Desired Caps function
Testing_Methods.desired_caps()
Testing_Methods.time.sleep(2)

# Creating Object of Class Login class
login_obj = Testing_Methods.Login()

# Calling method to click on signin and sign with email
login_obj.sign_in_btn()
Testing_Methods.time.sleep(3)

# Calling method to fil login details
login_obj.fill_login_details()
Testing_Methods.time.sleep(18)

# Calling function to Allow all required permission
Testing_Methods.allow_permissions()
Testing_Methods.time.sleep(5)

# Calling function to open profile
Testing_Methods.open_profile()
Testing_Methods.time.sleep(3)

# Signout Function
Testing_Methods.sign_out_btn()
