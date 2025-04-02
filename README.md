# Projeto Contabilidade

Este projeto é uma aplicação para processamento e análise de planilhas financeiras. Ele utiliza bibliotecas como **Pandas**, **Matplotlib** e **Seaborn** para manipulação e visualização de dados.

## 📌 Pré-requisitos

Certifique-se de ter os seguintes itens instalados:

- **Python 3.12** ou superior
- **Pip** (gerenciador de pacotes do Python)
- **Node.js** _(opcional, caso queira configurar o frontend)_

## 🚀 Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/Projeto-Contabilidade-PubliFin.git
   cd Projeto-Contabilidade-PubliFin
   ```

2. **Instale as dependências do backend:**

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

   _Ou, se estiver usando o pyproject.toml:_

   ```bash
   pip install .
   ```

3. **Adicione a planilha de entrada:**
   Certifique-se de que o arquivo `planilha.xlsx` está localizado no diretório `backend/`.

## 📊 Processamento de Dados

O arquivo `process_excel.py` executa as seguintes operações:

- **Receita Bruta Mensal**: Calcula a receita total por mês.
- **Despesas por Categoria**: Agrupa as despesas em categorias predefinidas.
- **Lucro/Prejuízo Mensal**: Calcula o resultado financeiro mensal.
- **Visualização de Dados**: Gera gráficos interativos para análise.

## ▶️ Uso

Para executar o processamento dos dados, utilize o seguinte comando:

```bash
python app/services/process_excel.py
```

## 🛠 Tecnologias Utilizadas

- **Python** (Pandas, Matplotlib, Seaborn)
- **Node.js** _(se aplicável para o frontend)_

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para contribuir! ✨
