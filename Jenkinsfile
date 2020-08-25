 pipeline{

    agent any

    stages{

        stage("Workspace"){
            steps{
                script{

                     def workspace_link = "<a href=http://localhost:8080/job/" + JOB_NAME + "/" + BUILD_NUMBER + "/execution/node/3/ws/'>Workspace</a>";
                     manager.createSummary("green.gif").appendText("<h1>" + workspace_link + "</h1>", false, false, false, "blue");

                }
            }
        }

        stage("run Login test file"){
            steps{

                bat """

                python --version

                pytest -vs Tests/test_login.py --platformname Android --udid 33766e229904 --platformversion 7.0

                """
               }
        }

        stage("run Signup test file"){
            steps{
                bat"""

                pytest -vs Tests/test_signup.py --platformname Android --udid 33766e229904 --platformversion 7.0

                """
            }
        }


        stage("run change name test file"){
            steps{
                bat"""

                pytest -vs Tests/test_change_name.py --platformname Android --udid 33766e229904 --platformversion 7.0

                """
            }
        }


        stage("run check application version test file"){
            steps{
                bat"""

                pytest -vs Tests/test_check_app_version.py --platformname Android --udid 33766e229904 --platformversion 7.0

                """
            }
        }


        stage("run inside manage product test file"){
            steps{
                bat"""

                pytest -vs Tests/test_inner_manage_product.py --platformname Android --udid 33766e229904 --platformversion 7.0

                """
            }
        }


        stage("run data preference test file"){
            steps{
                bat"""

                pytest -vs Tests/test_data_pref.py --platformname Android --udid 33766e229904 --platformversion 7.0

                """
            }
        }


        stage("run manage music test file"){
            steps{
                bat"""

                pytest -vs Tests/test_manage_music.py --platformname Android --udid 33766e229904 --platformversion 7.0

                """
            }
        }


        stage("run test notification test file"){
            steps{
                bat"""

                pytest -vs Tests/test_notification.py --platformname Android --udid 33766e229904 --platformversion 7.0
                
                """
            }
        }

   }
}
