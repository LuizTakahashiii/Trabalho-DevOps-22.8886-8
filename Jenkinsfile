#!/bin/bash

pipeline {
    agent any

    environment {
        // Define o nome do repositório para logging e configurações futuras
        REPO_URL = 'https://github.com/GuilhermeGaffuri/devOpsTrabalho'
    }

    stages {
        // Etapa 1: Clonar o código do Git
        stage('Checkout Code') {
            steps {
                echo 'Clonando o repositório do GitHub...'
                checkout scm
            }
        }

        // Etapa 2: Instalar dependências
        stage('Install Dependencies') {
            steps {
                echo 'Instalando dependências com pip...'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        // Etapa 3: Rodar os testes automatizados
        stage('Run Tests') {
            steps {
                echo 'Executando testes automatizados...'
                sh '''
                . venv/bin/activate
                python3 -m unittest discover -s tests
                '''
            }
        }

        // Etapa 4: Build e Deploy com Docker
        stage('Build and Deploy') {
            steps {
                echo 'Construindo imagens Docker e executando containers...'
                sh '''
                docker-compose down
                docker-compose build
                docker-compose up -d
                '''
            }
        }

        // Etapa 5: Verificar monitoramento
        stage('Verify Monitoring') {
            steps {
                echo 'Validando se o serviço está ativo...'
                sh '''
                curl -f http://localhost:5000/ || exit 1
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline concluída, limpando arquivos temporários...'
            sh '''
            docker-compose down
            rm -rf venv
            '''
        }
        success {
            echo 'Pipeline executada com sucesso!'
        }
        failure {
            echo 'Pipeline falhou. Verifique os logs no Console Output.'
        }
    }
}
