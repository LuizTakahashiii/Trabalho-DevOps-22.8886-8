pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'devopstrabalho:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YourRepo/devops_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r flask/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Build and Deploy') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
