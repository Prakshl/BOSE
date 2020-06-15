import time
from Methods_py import *

# Calling Desired Caps function
desired_caps()
time.sleep(2)

# Creating Object of Sign_up Class
a = Sign_up()

# Calling method to click on signup and signup with email
a.sign_up_btn()
time.sleep(8)
# Calling method to fill required details
a.fill_signup_details()
time.sleep(20)
# Calling function to tick all privacy policy and click on I Agree
a.privacy_policy()
time.sleep(56)
# Calling function to Allow all required permission
allow_permissions()
time.sleep(5)
# Calling function to open profile
open_profile()
time.sleep(4)
# Signout Function
sign_out_btn()

