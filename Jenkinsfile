pipeline{
    agent any
    stages{
        
        stage('run_py'){
            steps{
                bat"""cd Tests
                      pytest -v test_signup.py --platformname Android --udid 33766e229904 --platformversion 7.0
                """
                
               
                
            }
        }
        
      
    }
}
