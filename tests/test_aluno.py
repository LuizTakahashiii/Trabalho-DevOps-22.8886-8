import pytest
from app import app, db, Aluno

@pytest.fixture
def client():
    # Configuração para testes
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco em memória
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Criação do app e banco
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Cria as tabelas
        yield client  # Retorna o cliente de teste

        # Limpeza do banco após os testes
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_index(client):
    """Teste para a rota principal"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bem-vindo à aplicação Flask!' in response.data

def test_listar_alunos_vazio(client):
    """Teste para listar alunos quando não há nenhum cadastrado"""
    response = client.get('/alunos')
    assert response.status_code == 200
    assert response.json == []

def test_adicionar_aluno(client):
    """Teste para adicionar um aluno"""
    data = {'nome': 'João Silva', 'ra': '12345'}
    response = client.post('/alunos', json=data)
    assert response.status_code == 201
    assert response.json['message'] == 'Aluno adicionado com sucesso!'

    # Verifica se o aluno foi adicionado
    response = client.get('/alunos')
    assert response.status_code == 200
    alunos = response.json
    assert len(alunos) == 1
    assert alunos[0]['nome'] == 'João Silva'
    assert alunos[0]['ra'] == '12345'

def test_adicionar_aluno_duplicado(client):
    """Teste para evitar adicionar um aluno com RA duplicado"""
    data = {'nome': 'João Silva', 'ra': '12345'}
    client.post('/alunos', json=data)

    # Tenta adicionar o mesmo RA
    response = client.post('/alunos', json=data)
    assert response.status_code == 500  # Erro esperado por duplicação
    assert b'UNIQUE constraint failed' in response.data  # Mensagem do SQLite
