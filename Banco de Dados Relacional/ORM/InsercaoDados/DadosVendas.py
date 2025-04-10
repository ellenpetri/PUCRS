#Manipulação de dados
#De um arquivo CSV para o banco na tabela 'Vendas'

import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CriacaoDasTabelas import CriacaoTabelasVendas as tbVendas


arquivo_vendedor_csv = r"D:\0. Pessoal\0. Git\PUCRS\Banco de Dados Relacional\ORM\InsercaoDados\ArquivoDados\Dados Vendedor.csv"

vendedor = pd.read_csv(arquivo_vendedor_csv, sep=";")

tbVendedor = pd.DataFrame(vendedor)

engine = sa.create_engine("sqlite:///BancoDados/vendas.db")

sessao = orm.sessionmaker(bind=engine)
sessao = sessao()

for i in range(len(tbVendedor)):
    dados_vendedor = tbVendas.vendedor(
        registro_vendedor = int(tbVendedor['Registro Vendedor'][i]),
        cpf = tbVendedor['CPF'][i],
        nome = tbVendedor['Nome'][i],
        genero = tbVendedor['Gênero'][i],
        email = tbVendedor['Email'][i]
    )
    
    try:
        sessao.add(dados_vendedor)
        sessao.commit()
    except Exception as e:
        print(f"Erro ao inserir os dados na tabela vendas: {e}")
        sessao.rollback()

print('Dados Inseridos na tabela vendas')
