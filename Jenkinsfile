pipeline {
    agent any

    stages {
        stage('Preparar Ambiente') {
            steps {
                script {
                    echo '=== Preparando o ambiente ==='
                    sh '''
                    # Parar e remover containers existentes
                    docker ps -aq | xargs -r docker stop
                    docker ps -aq | xargs -r docker rm
                    docker-compose down || true

                    # Limpar recursos desnecessários
                    docker system prune -f || true
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                echo '=== Iniciando build ==='
                sh 'docker-compose build --no-cache' // Build das imagens sem cache
            }
        }

        stage('Testar Aplicação') {
            steps {
                echo '=== Executando testes ==='
                script {
                    // Subir os serviços necessários para os testes
                    sh '''
                    docker-compose up -d mariadb flask
                    echo "Aguardando inicialização dos serviços..."
                    sleep 15  # Aguarda a inicialização dos serviços
                    '''

                    // Verificar se os serviços estão rodando
                    sh '''
                    docker ps -qf "name=mariadb" || (echo "MariaDB não está rodando!" && exit 1)
                    docker ps -qf "name=flask-container" || (echo "Flask não está rodando!" && exit 1)
                    '''

                    // Executar os testes no contêiner Flask
                    sh '''
                    docker exec $(docker ps -qf "name=flask-container") \
                    pytest /app/tests --junitxml=/app/tests/report.xml
                    '''

                    // Derrubar os serviços após os testes
                    sh 'docker-compose down'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                echo '=== Realizando deploy da aplicação ==='
                sh 'docker-compose up --build -d'  // Subir os containers da aplicação em modo detach
            }
        }
    }

    post {
        always {
            echo '=== Pipeline executada ==='
            echo 'Acesse os serviços pelos links abaixo:'
            echo 'Grafana: http://localhost:3000'
            echo 'Prometheus: http://localhost:9090'
            echo 'Aplicação Flask: http://localhost:5000'
            echo 'Lista de alunos: http://localhost:5000/alunos'
        }
    }
}
