# -*- coding: utf-8 -*-
"""contabilidade.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QqR9NSlLHp_w07UOy5X_OiN8VkMsBVQg
"""

"""# Preparando df

"""

import pandas as pd


path = "/content/CC&Gerencial_Base de Dados (Atividade 2º Exercício).ods" #Adicionar path correto
df = pd.read_excel(path)


df['Data'] = pd.to_datetime(df['Data'])


df['Mes_Ano'] = df['Data'].dt.to_period('M')


# Remove rows where both 'Despesas' and 'Saida' are null

df.dropna(subset=['Entrada', 'Saida'], how='all', inplace=True)


df['Nome Natureza'].value_counts()

# Cria a condição booleana
condicao = df['Nome Natureza'].isin([
    "ADIANT. DE LUCRO - CARLOS HENR",
    "ADIANT. DE LUCRO - MATEUS MACI",
    "ADIANT. DE LUCRO - MANOEL VIRG"
])

# Usa loc para acessar e modificar as linhas que atendem à condição
df.loc[condicao, 'Nome Natureza'] = "ADIANT. DE LUCRO"


"""# Despesas"""

df_despesas = df[df['Saida'].notnull()].copy()

df_despesas.drop(df_despesas[df_despesas["Nome Natureza"] == "JUROS RECEBIDOS"].index, inplace=True)

df_despesas.dropna(subset=["Nome Natureza"], inplace=True)

df_despesas['Nome Natureza'].value_counts()

def categorizar(nome):
    categorias = {
        "Despesas Operacionais": ["SERVICOS DE PUBLICIDADE E PROP", "MARKETING DIRETO", "SERVICO DE DIVULGACAO",
                                   "CONSULTORIA", "LICENCA DE USO", "SERVICOS INFORMATICA", "SERVICOS LIMPEZA E CONSERVACAO",
                                   "CERTIFICADO DIGITAL"],
        "Despesas Administrativas": ["ALUGUEL DE IMOVEIS", "CONDOMINIO", "ENERGIA ELETRICA", "TELEFONIA MOVEL",
                                      "TELEFONIA FIXA", "MATERIAL DE EXPEDIENTE"],
        "Despesas Financeiras e Tributárias": ["TARIFAS BANCARIAS", "IOF", "JUROS PAGOS", "IRRF APLICACAO FINANCEIRA",
                                               "SIMPLES NACIONAL", "EMOLUMENTOS CARTORIOS", "TAXAS MUNICIPAIS",
                                               "CIM CADASTRO INSCRICAO MUNICIP"],
        "Despesas com Pessoal": ["PRO LABORE", "INSS SOBRE PRO LABORE", "CONFRATERNIZACAO", "CURSOS E TREINAMENTOS",
                                  "LANCHES E REFEICOES"],
        "Investimentos e Aplicações": ["APLICACAO ITAU AUTO MAIS", "RESGATE ITAU AUTO MAIS", "RESGATE INTER CDB MAIS",
                                        "APLICACAO INTER CDB MAIS", "AJUSTE DE RENDIMENTO APLICACAO",
                                        "RENDIMENTO DE APLICACOES FINAN", "CONSORCIO ITAU"],
        "Despesas Eventuais e Diversas": ["ADIANT. DE LUCRO", "ADIANTAMENTO DE CLIENTES", "ENTRADAS DE TRANSFERENCIAS",
                                           "PAGAMENTOS DIVERSOS", "OUTRAS DESPESAS", "SEGUROS PESSOAIS E EMPRESARIAI",
                                           "MULTAS PUNITIVAS", "DOACOES E CONTRIBUICOES", "CONDUCAO E TRANSPORTE",
                                           "IPTU IMP PREDIAL TERRIT URBANO"]
    }

    for categoria, itens in categorias.items():
        if nome in itens:
            return categoria
    return "Outros"

df_despesas.loc[:, "Categoria"] = df_despesas["Nome Natureza"].apply(categorizar)

df_despesas.head(10)

df_despesas.groupby(['Categoria'])['Saida'].sum().reset_index()

df_despesas['Categoria'].value_counts()

df_despesas[df_despesas['Categoria'] == 'Outros']['Nome Natureza'].value_counts()

df_despesas.loc[df_despesas["Categoria"] == "Outros", "Categoria"] = "Despesas Administrativas"

df_despesas['Categoria'].value_counts()

df_despesas.groupby('Categoria')['Saida'].sum().reset_index()

df_despesas[df_despesas["Mes_Ano"] == "2023-01"].groupby("Categoria")["Saida"].sum().reset_index()

df_despesas[df_despesas["Mes_Ano"] == "2023-02"].groupby("Categoria")["Saida"].sum().reset_index()

