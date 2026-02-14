# IA Jurídica Modular (Versão Avançada)

Este projeto implementa uma Inteligência Artificial Jurídica modular, baseada em um "Prompt Mestre" e arquitetura escalável.

## Estrutura do Projeto

- `backend/`: Código fonte do servidor backend (FastAPI, Chains, LLM).
- `data/`: Dados brutos e processados.
- `vector_db/`: Banco de dados vetorial para RAG.
- `logs/`: Logs de execução.
- `docker/`: Arquivos de configuração Docker.
- `openwebui/`: Integração com OpenWebUI.
- `tests/`: Testes automatizados.

## Módulos

O sistema é dividido em módulos por área do direito:
- Civil
- Trabalhista
- Empresarial
- Tributário
- Penal
- Administrativo
- Consumidor
- Previdenciário
- Contratual

## Pré-requisitos

1.  **Python 3.10+** instalado.
2.  **Ollama** instalado e em execução.
    -   Certifique-se de ter baixado o modelo padrão (llama3):
        ```bash
        ollama pull llama3
        ```

## Instalação

1.  Clone o repositório e navegue até a pasta do projeto:
    ```bash
    cd ia-juridica
    ```

2.  Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    # venv\Scripts\activate   # Windows
    ```

3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Execução

1.  Certifique-se de que o Ollama está rodando (geralmente em `http://localhost:11434`).

2.  Inicie o servidor backend:
    ```bash
    export PYTHONPATH=$PWD
    uvicorn backend.main:app --reload
    ```

    O servidor estará disponível em `http://localhost:8000`.

## Testando a API

Você pode testar a API enviando uma requisição POST para `/chat`:

### Exemplo (Curl):

**Caso Trabalhista:**
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "Fui demitido sem justa causa e não recebi minhas verbas rescisórias."}'
```

**Caso Civil:**
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "Meu vizinho construiu um muro que invadiu meu terreno."}'
```

## Executando Testes

Para rodar os testes unitários:

```bash
export PYTHONPATH=$PWD
python -m unittest discover tests
```
