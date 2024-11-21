pipeline {
    agent any

    environment {
        // Variáveis de ambiente, como nome da imagem Docker
        DOCKER_IMAGE = 'devopstrabalho:latest'
        DOCKER_REGISTRY = 'meu-registro.com'
    }

    stages {
        // Etapa 1: Baixar Código do Git
        stage('Baixar Código do Git') {
            steps {
                // Clonando o repositório Git
                git 'https://github.com/GuilhermeGaffuri/devOpsTrabalho.git'
            }
        }

        // Etapa 2: Rodar Testes
        stage('Rodar Testes') {
            steps {
                // Rodando testes (personalize conforme o seu projeto)
                script {
                    sh 'npm install'  // Se for uma aplicação Node.js, instale dependências
                    sh 'npm test'     // Execute os testes
                }
            }
        }

        // Etapa 3: Build e Deploy
        stage('Build e Deploy') {
            steps {
                script {
                    // Construindo a imagem Docker
                    sh 'docker build -t $DOCKER_IMAGE .'

                    // Subindo a aplicação (criação do container)
                    sh 'docker run -d -p 8080:80 $DOCKER_IMAGE'
                    
                    // Aqui você pode adicionar comandos para deploy em ambientes como Kubernetes, AWS, etc.
                    // Exemplo: 
                    // sh 'kubectl apply -f deployment.yaml'
                }
            }
        }

        // Etapa 4: Monitoramento
        stage('Verificar Monitoramento') {
            steps {
                script {
                    // Realizar verificação do monitoramento ou status da aplicação
                    def response = sh(script: 'curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/health', returnStdout: true).trim()
                    if (response != '200') {
                        error "Aplicação não está respondendo corretamente!"
                    } else {
                        echo "Monitoramento OK!"
                    }
                }
            }
        }
    }

    post {
        // Limpeza e mensagens pós-execução
        always {
            cleanWs()  // Limpa o workspace após execução
        }
        success {
            echo 'Pipeline executada com sucesso!'
        }
        failure {
            echo 'Pipeline falhou!'
        }
    }
}
