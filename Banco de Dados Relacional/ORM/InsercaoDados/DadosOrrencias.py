import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CriacaoDasTabelas import CriacaoTabelasOcorrencias as oc

pastaBase = r"D:\0. Pessoal\0. Git\PUCRS\Banco de Dados Relacional\ORM\InsercaoDados\ArquivoDados"

csvDp = pastaBase + r"\OcorrenciaDP.csv"
csvMunicipio = pastaBase + r"\OcorrenciaMunicipio.csv"
excelResposavelDp = pastaBase + r"\OcorrenciaResponsavelDP.xlsx"
excelOcorrencias = pastaBase + r"\Ocorrencias.xlsx"

dp = pd.read_csv(csvDp, sep=";")
municipio = pd.read_csv(csvMunicipio, sep=",")
responsavelDp = pd.read_excel(excelResposavelDp)
ocorrencias = pd.read_excel(excelOcorrencias)

tbDpArquivo = pd.DataFrame(dp)
tbResposavelDPArquivo  = pd.DataFrame(responsavelDp)
tbMunicipioArquivo  = pd.DataFrame(municipio)
tbOcorrenciasArquivo  = pd.DataFrame(ocorrencias)

engine = sa.create_engine("sqlite:///BancoDados/ocorrencias.db")
sessao = orm.sessionmaker(bind=engine)
sessao = sessao()

conn = engine.connect()

metadados = sa.schema.MetaData()
metadados.reflect(bind=engine)

#Inserindo os dados do DP
DadosDp = tbDpArquivo.to_dict(orient="records")
tabela_DP = sa.Table(oc.Dp.__tablename__, metadados, autoload = True)

try:
    conn.execute(tabela_DP.insert(), DadosDp)
    sessao.commit()
except Exception as e:
    print(f"Erro ao inserir na tabela DP: {e}")


#Inserindo os dados do responsável dp
DadosResponsavelDp = tbResposavelDPArquivo.to_dict(orient="records")
tabela_ResponsavelDp = sa.Table(oc.ResponsavelDP.__tablename__, metadados, autoload = True)

try:
    conn.execute(tabela_ResponsavelDp.insert(), DadosResponsavelDp)
    conn.commit()
except Exception as e:
    print(f"Erro ao inserir na tabela responsável DP: {e}")
    
    
#Inserindo os dados do municipio
DadosMunicipio = tbMunicipioArquivo.to_dict(orient="records")
tabela_Municipio = sa.Table(oc.Municipio.__tablename__, metadados, autoload = True)

try:
    conn.execute(tabela_Municipio.insert(), DadosMunicipio)
    conn.commit()
except Exception as e:
    print(f"Erro ao inserir na tabela municipio: {e}")
    
#Inserindo os dados do municipio
DadosOcorrencia = tbOcorrenciasArquivo.to_dict(orient="records")
tabela_Ocorrencia = sa.Table(oc.Ocorrencias.__tablename__, metadados, autoload = True)

try:
    conn.execute(tabela_Ocorrencia.insert(), DadosOcorrencia)
    conn.commit()
except Exception as e:
    print(f"Erro ao inserir na tabela ocorrencia: {e}")
    
sessao.close_all()
