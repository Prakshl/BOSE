# How to run

1. You can Sign up or Login using two different Py File
   There User need to write appropriate PlatformName and UDID at run time.
   
   Ex. pytest -v test_login.py --platformname PlatformName --udid UDID platformversion PlatformVersion  (Using -v we know that which method is currently executing and that method is passed or not.)
         
         ytest -v test_login.py --platformname Android --udid 5132 platformversion 7.0
         
          pytest -v test_login.py::test_desired_capabilities --platformname Android --udid 5132 platformversion 7.0 (By using '::' only desired capabilities method will run)
         
2. To SignUP:   Run test_signup.py file
3. To Login:    Run test_login.py file
   These both files are in Call_Methods
   
4. You can see locators (Paths of different android view elements) Open Locators.py file to view all locators used in the `project.
5. You can see all methods which are used to set desired capabilities and also used for Login and SignUp.  Open test_all_methods.py to view.
