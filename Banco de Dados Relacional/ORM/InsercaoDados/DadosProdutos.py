#Manipulação de dados
#De um arquivo CSV para o banco na tabela 'Vendas'

import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CriacaoDasTabelas import CriacaoTabelasVendas as tbVendas

engine = sa.create_engine("sqlite:///BancoDados/vendas.db")

sessao = orm.sessionmaker(bind=engine)
sessao = sessao()


#Inserindo informações na TBProduto em massa (utilizado se não precisar validar)
excelProdutos = r"D:\0. Pessoal\0. Git\PUCRS\Banco de Dados Relacional\ORM\InsercaoDados\ArquivoDados\Dados Produtos.xlsx"
produtos = pd.read_excel(excelProdutos)

tbProduto = pd.DataFrame(produtos)

connection = engine.connect()

metadados = sa.schema.MetaData()
metadados.reflect(bind=engine)

dadosProduto = tbProduto.to_dict(orient="records")

tabelaProduto = sa.Table(tbVendas.produto.__tablename__, metadados, autoload_with=engine)

print(tbProduto.columns)
print(tabelaProduto.columns.keys())


try:
    sessao.bulk_insert_mappings(tbVendas.produto, dadosProduto)
    sessao.commit()
except Exception as e:
    print(f"Erro ao inserir na tabela produto: {e}")
    
print("Dados inseridos na tabela produto")

sessao.close_all()