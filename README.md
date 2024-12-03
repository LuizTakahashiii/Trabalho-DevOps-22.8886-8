# Projeto DevOps: Pipeline CI/CD com Monitoramento

#Aluno : Luiz Sergio Takahashi

#RA: 22.8886-8

Este projeto implementa um ambiente DevOps completo com uma aplicação Flask, pipeline CI/CD usando Jenkins, monitoramento com Prometheus e Grafana, e containerização via Docker Compose.

# Trabalho-DevOps-22.8886-8

```plaintext
Trabalho-DevOps-22.8886-8/
├── docker-compose.yml
├── Jenkinsfile
├── prometheus.yml
├── grafana/
│   └── flask_dashboard.json
├── flask/
│   └── app.py
│   └── requirements.txt
│   └── tests/
│       └── test_cadastrar_aluno.py
Configuração do Projeto
1. Clonando o Repositório
Clone o repositório do projeto para sua máquina local:

bash

git clone <URL_DO_REPOSITORIO>
cd Trabalho-DevOps-22.8886-8

2. Configurando Chave SSH para o Git
Se ainda não configurou sua chave SSH, siga os passos abaixo:

Gere a chave SSH:
bash

ssh-keygen -t rsa -b 4096 -C "seu_email@example.com"
Adicione a chave ao SSH-Agent:
bash

eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
Adicione a chave pública ao GitHub ou outro provedor:
bash

cat ~/.ssh/id_rsa.pub
Copie e cole o conteúdo no campo de chaves SSH do seu repositório pessoal no provedor de Git (como GitHub).


3. Configurando Jenkins
Acesse o Jenkins pelo navegador:
arduino

http://localhost:8080
Crie um novo pipeline e vincule-o ao repositório Git do projeto.
Use o arquivo Jenkinsfile para configurar o pipeline.


4. Configurando e Executando o Projeto
Passo 1: Subir o Ambiente com Docker Compose
No diretório do projeto, execute:

bash

docker-compose up --build
Passo 2: Acessar os Serviços
Após a execução bem-sucedida, os serviços estarão disponíveis nos seguintes links:




Aplicação Flask: http://localhost:5000

Grafana: http://localhost:3000

Prometheus: http://localhost:9090

Jenkins: http://localhost:8080

Monitoramento com Grafana

Configuração do Dashboard

Acesse o Grafana em http://localhost:3000.

Faça login com as credenciais padrão:
Usuário: admin
Senha: admin

Importe o dashboard JSON localizado em grafana/flask_dashboard.json:
Navegue até Create > Import.

Cole o conteúdo do arquivo ou carregue diretamente.

Métricas Monitoradas

Taxa de requisições HTTP por método e status.

Taxa de consultas ao banco de dados MariaDB.

Testes da Aplicação

Suba os serviços Flask e MariaDB para execução dos testes
bash


docker-compose up -d mariadb flask
sleep 10

Execute o teste unitário:
bash

docker exec $(docker ps -qf "name=flask-container") python /app/tests/test_cadastrar_aluno.py
Verifique os resultados no terminal.

Personalização
Alteração de Configurações
Banco de Dados: Atualize SQLALCHEMY_DATABASE_URI no arquivo flask/app.py.
Intervalos de Coleta: Ajuste scrape_interval no arquivo prometheus.yml.
Adicionar Novas Métricas
Edite flask/app.py para expor novas métricas no endpoint /metrics.
Atualize o dashboard no Grafana para exibir as novas métricas.


Problemas Comuns
1. Containers Não Sobem
Verifique se as portas 5000, 3000, 9090 ou 8080 já estão em uso:
bash

lsof -i :PORTA
Mate o processo ocupando a porta:
bash

kill -9 PID
2. Falha na Conexão com o MariaDB
Certifique-se de que o container MariaDB está ativo:
bash

docker ps -qf "name=mariadb"


3. Grafana Não Carrega o Dashboard
Verifique se o JSON do dashboard está correto e os data sources estão configurados.
