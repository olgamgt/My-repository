pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python --version'
                sh 'python busqueda.py'

            }
        }
        stage('Test') { 
            steps {
                echo 'Testing..' 
            }
        }
        stage('Deploy') { 
            steps {
                echo 'Deploying..'
            }
        }
    }
}
