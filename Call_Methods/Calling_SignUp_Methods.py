import sys
sys.path.insert(0, r'C:\Users\Disha\PycharmProjects\Testing')
from Test_Methods.Testing_Methods import *

# Calling Desired Caps function
desired_caps()
time.sleep(2)

# Creating Object of Sign_up Class
signup_obj = Sign_up()

# Calling method to click on signup and signup with email
signup_obj.sign_up_btn()
time.sleep(8)

# Calling method to fill required details
signup_obj.fill_signup_details()
time.sleep(20)

# Calling function to tick all privacy policy and click on I Agree
signup_obj.privacy_policy()
time.sleep(56)

# Calling function to Allow all required permission
allow_permissions()
time.sleep(5)

# Calling function to open profile
open_profile()
time.sleep(4)

# Signout Function
sign_out_btn()
