import pytest
from app import app, db, Aluno

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco em memória para testes
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_adicionar_aluno(client):
    # Dados do aluno para teste
    aluno_data = {
        "nome": "João",
        "sobrenome": "Silva",
        "turma": "3A",
        "disciplinas": "Matemática, Física",
        "ra": "123456"
    }

    # Envia requisição POST para adicionar aluno
    response = client.post('/alunos', json=aluno_data)
    assert response.status_code == 201

    # Verifica se o aluno foi adicionado no banco
    aluno = Aluno.query.filter_by(ra="123456").first()
    assert aluno is not None
    assert aluno.nome == "João"
    assert aluno.sobrenome == "Silva"
    assert aluno.turma == "3A"
