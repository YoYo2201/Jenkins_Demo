pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/YoYo2201/Jenkins_Demo.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x DemoFile.py"
                sh "python3 DemoFile.py"
            }
        }
        stage('Test Code 1') {
            steps {
                sh "chmod u+x Testing_Pass.py"
                sh "python3 Testing_Pass.py"
            }
        }
        stage('Test Code 2') {
            steps {
                sh "chmod u+x Testing_Fail.py"
                sh "python3 Testing_Fail.py"
            }
        }
    } 
}