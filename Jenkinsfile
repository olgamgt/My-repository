pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python --version'
                sh 'python ./gym-csv-loop.py assets/map1.csv 2 2 9 9 bfs'

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
