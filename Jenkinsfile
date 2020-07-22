pipeline{
    agent any
    stages{
        stage('build'){
            steps{
                sh 'pip install pytest'
            }
        }
          
        
        stage('change_folder'){
            steps{
               dir('Test') {
                sh"pwd"
              }
            }
        }
        
        stage('run_pytest'){
            steps{
                sh"pwd"
                sh 'pytest -v -s test_login.py --platformname Android --udid 33766e229904 --platformversion 7.0'
            }
        }
    }
}
