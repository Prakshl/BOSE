pipeline{
    
    agent any
        
    stages{
        stage('run_py'){
            steps{
                bat """
                   cd Tests
                   pytest -v -s test_login.py --platformname Android --udid 988a90363239513753 --platformversion 8.0.0
                  
                """  
            }
        }
      
    }
        
}
