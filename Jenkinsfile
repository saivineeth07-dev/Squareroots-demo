pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)   // 🔴 FIX #1: remove double checkout
    }

    environment {
        PYTHON = "C:\\Users\\saivi\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/saivineeth07-dev/Squareroots-demo.git'
                    ]],
                    extensions: [[
                        $class: 'CloneOption',
                        shallow: true,
                        depth: 1,
                        timeout: 5
                    ]]
                ])
            }
        }

        stage('Setup Virtualenv') {
            steps {
                bat '''
                if not exist %VENV% (
                    "%PYTHON%" -m venv %VENV%
                )
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                %VENV%\\Scripts\\python -m pip install --upgrade pip
                %VENV%\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def status = bat(
                        script: '%VENV%\\Scripts\\pytest',
                        returnStatus: true
                    )
                    if (status == 5) {
                        echo 'No tests found. Continuing.'
                    } else if (status != 0) {
                        error 'Tests failed'
                    }
                }
            }
        }

        stage('Run Application (SAFE)') {
            steps {
                // 🔴 FIX #2: Explicit python + timeout
                timeout(time: 30, unit: 'SECONDS') {
                    bat '''
                    %VENV%\\Scripts\\python Annotation.py
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Build Successful'
        }
        failure {
            echo 'Build Failed'
        }
    }
}
