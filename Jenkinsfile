pipeline{
    agent any
    stages{
        
        stage('change_folder'){
            steps{
               dir('Tests') {
                   sh"pytest -v -s test_login.py --platformname Android --udid 33766e229904 --platformversion 7.0"
         
              }
            }
        }
        
      
    }
}
