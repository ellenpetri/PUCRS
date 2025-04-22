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

dp = pd.read_csv(csvDp, sep=",")
municipio = pd.read_csv(csvMunicipio, sep=",")
responsavelDp = pd.read_excel(excelResposavelDp)
ocorrencias = pd.read_excel(excelOcorrencias)

tbDpArquivo = pd.DataFrame(dp)
tbResposavelDPArquivo  = pd.DataFrame(responsavelDp)
tbMunicipioArquivo  = pd.DataFrame(municipio)
tbOcorrenciasArquivo  = pd.DataFrame(ocorrencias)

engine = sa.create_engine("sqlite:///BancoDados/ocorrencias.db")

conn = engine.connect()
metadata = sa.schema.MetaData(bind=engine)
Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

#Inserindo os dados do DP
DadosDp = tbDpArquivo.tp_dict(orient="records")
tabela_DP = sa.Table(oc.dp.__tablename__, metadata, autoload = True)

try:
    conn.execute(tabela_DP.insert(), DadosDp)
    sessao.commit()
except Exception as e:
    print(f"Erro ao inserir na tabela DP: {e}")


#Inserindo os dados do responsável dp
DadosResponsavelDp = tbResposavelDPArquivo.tp_dict(orient="records")
tabela_ResponsavelDp = sa.Table(oc.ResponsavelDP.__tablename__, metadata, autoload = True)

try:
    conn.execute(tabela_ResponsavelDp.insert(), DadosResponsavelDp)
    sessao.commit()
except Exception as e:
    print(f"Erro ao inserir na tabela responsável DP: {e}")
    
    
#Inserindo os dados do municipio
DadosMunicipio = tbMunicipioArquivo.tp_dict(orient="records")
tabela_Municipio = sa.Table(oc.Municipio.__tablename__, metadata, autoload = True)

try:
    conn.execute(tabela_Municipio.insert(), DadosMunicipio)
    sessao.commit()
except Exception as e:
    print(f"Erro ao inserir na tabela municipio: {e}")