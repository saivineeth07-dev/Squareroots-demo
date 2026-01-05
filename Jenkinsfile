pipeline {
    agent any

    environment {
        CI = "true"
    }

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/saivineeth07-dev/Squareroots-demo.git'
            }
        }

        stage('Setup Virtualenv') {
            steps {
                bat '''
                if not exist venv (
                    "C:\\Users\\saivi\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv
                )
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\python -m pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def status = bat(script: 'venv\\Scripts\\pytest', returnStatus: true)
                    if (status == 5) {
                        echo 'No tests found. Continuing.'
                    } else if (status != 0) {
                        error "Tests failed"
                    }
                }
            }
        }

        stage('Run OpenCV') {
            steps {
                bat 'echo WORKSPACE=%WORKSPACE%'
                bat 'venv\\Scripts\\python -m app.main'
            }
        }

        stage('Verify Output') {
            steps {
                bat 'dir output'
            }
        }
    }

    post {
        success {
            echo 'Build Successful (CI-safe)'
            archiveArtifacts artifacts: 'output/*.jpg'
        }
        failure {
            echo 'Build Failed'
        }
    }
}
