import pandas as pd 
from time import sleep

class CalculosFinanceiros:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_excel(file_path)

    def filtrar_entradas(self):
        # Filtra as entradas
        entradas = self.df[self.df['Natureza'].astype(str).str.startswith('1')]
        return entradas

    def transformar_data(self):
        # Converte a coluna 'Data' para o formato dia/mês/ano
        if 'Data' in self.df.columns:
            self.df['Data'] = pd.to_datetime(self.df['Data'], format='%m/%d/%Y', errors='coerce')
            self.df['Data'] = self.df['Data'].dt.strftime('%m/%Y')
        else:
            raise ValueError("A coluna 'Data' não existe no arquivo Excel.")
        return self.df

    def separar_meses(self):
        # Separa os meses
        lista_meses = []

        datas_unicas = self.df['Data'].unique().tolist()
        
        for data in datas_unicas:
            planilha_filtrada = self.df[self.df['Data'] == data]
            total_saida = round(float(planilha_filtrada['Entrada'].sum()), 2)
            
            lista_meses.append({'Mes/Ano': data, 'Receita Bruta': total_saida})
            
            # Remove índices onde a Receita Bruta seja 0
            lista_meses = [mes for mes in lista_meses if mes['Receita Bruta'] != 0]
            # Transforma lista_meses em um DataFrame
        
        lista_meses = pd.DataFrame(lista_meses)
        
        return lista_meses



calculo = CalculosFinanceiros('planilha.xlsx')
filtro = calculo.transformar_data()
filtro = calculo.filtrar_entradas()
filtro = calculo.separar_meses()
print(filtro)
