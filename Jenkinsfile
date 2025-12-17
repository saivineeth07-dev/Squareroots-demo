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
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def status = bat(script: 'pytest', returnStatus: true)
                    if (status == 5) {
                        echo 'No tests found. Continuing pipeline.'
                    } else if (status != 0) {
                        error 'Tests failed'
                    }
                }
            }
        }

        stage('Run Application') {
            steps {
                bat 'Annotation.py'
            }
        }
        stage('Verify Python') {
           steps {
                bat 'where python'
                bat 'python --version'
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
