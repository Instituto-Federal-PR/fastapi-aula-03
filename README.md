# Sistema Acadêmico — FastAPI com Arquitetura Limpa

API acadêmica com autenticação JWT, autorização por papel e CRUD de cursos, disciplinas, alunos e matrículas. A refatoração separa apresentação, aplicação, domínio e infraestrutura sem alterar os caminhos públicos, os contratos principais dos payloads nem as permissões existentes.

## Estrutura

```text
app/
├── core/                        # config.py e exceptions.py
├── domain/
│   ├── entities/                # curso, aluno, disciplina, matrícula e usuário
│   ├── repositories/            # Interfaces ABC separadas por recurso
│   └── services/                # auth_service.py
├── application/
│   ├── dtos/                    # DTOs de entrada separados por recurso
│   └── use_cases/               # Casos de uso separados por recurso
├── infrastructure/
│   ├── database/                # models.py e session.py
│   ├── repositories/            # Implementações concretas por recurso
│   └── security/                # backend JWT, hashing e UserManager
├── presentation/
│   ├── api/                     # Routers isolados por recurso
│   ├── dependencies/            # Injeção de dependências e papéis
│   └── schemas/                 # Schemas Pydantic isolados por recurso
├── alembic/                     # Migrações do banco
└── main.py                      # Ponto de composição FastAPI
tests/                           # Teste integrado de autenticação e CRUD
```

Os recursos `aluno` e `matricula` também aparecem nos repositórios, 
casos de uso, DTOs, schemas e routers para manter todo o CRUD original, 
além de `curso` e `disciplina`. As rotas convertem schemas Pydantic em DTOs 
de aplicação; os casos de uso dependem das interfaces do domínio; os adaptadores 
SQLAlchemy implementam essas interfaces.

## Executar com Docker Compose

```bash
docker compose up -d --build
docker compose exec web alembic upgrade head
```

A API fica em `http://localhost:17000`; a documentação interativa em `/docs`. 
O PostgreSQL usa as configurações locais definidas no `docker-compose.yml`.

## Executar localmente

É necessário um PostgreSQL e uma variável `DATABASE_URL` compatível com `postgresql+psycopg://...`.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL='postgresql+psycopg://usuario:senha@localhost:5432/fastapi_db'
alembic upgrade head
uvicorn app.main:app --reload
```

A chave JWT pode ser configurada em `JWT_SECRET`. Se não definida, é mantido o 
valor-padrão legado do projeto; esse valor deve ser substituído em ambientes reais.

## Autenticação e autorização

- Registro: `POST /auth/register` (papel padrão: `professor`)
- Login JWT: `POST /auth/jwt/login`
- Use o token como `Authorization: Bearer <token>`.
- Papéis: `professor` e `coordenador`.

| Operação | Permissão |
|---|---|
| Criar/alterar/excluir curso | Coordenador |
| Consultar cursos | Professor ou coordenador |
| Criar/alterar/excluir aluno | Professor |
| Consultar alunos | Professor ou coordenador |
| Criar/alterar/excluir disciplina | Professor |
| Consultar disciplinas | Professor ou coordenador |
| Criar/excluir matrícula | Coordenador |
| Consultar matrículas | Professor ou coordenador |

## Endpoints

- `/cursos`
- `/disciplinas`
- `/alunos`
- `/matriculas`

Os métodos e caminhos específicos permanecem documentados no Swagger em `/docs`.