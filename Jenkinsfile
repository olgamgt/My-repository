pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python -c "import sys; print sys.path"'
                sh 'python gym-csv-loop.py assets/map1.csv 2 2 9 9 bfs'
                sh 'python prueba.py'

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
