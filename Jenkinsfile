pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/saivineeth07-dev/Squareroots-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Run Application') {
            steps {
                sh 'Annotation.py'
            }
        }
    }

    post {
        success {
            echo 'Build & Deployment Successful!'
        }
        failure {
            echo 'Build Failed!'
        }
    }
}
