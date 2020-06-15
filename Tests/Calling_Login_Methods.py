import time
from Methods import *

# Calling Desired Caps function
desired_caps()
time.sleep(2)

# Creating Object of Class Login class
login_obj=Login()

# Calling method to click on signin and sign with email
login_obj.sign_in_btn()
time.sleep(3)

# Calling method to fil login details
login_obj.fill_login_details()
time.sleep(18)

# Calling function to Allow all required permission
allow_permissions()
time.sleep(5)

# Calling function to open profile
open_profile()
time.sleep(3)

#Signout Function
sign_out_btn()