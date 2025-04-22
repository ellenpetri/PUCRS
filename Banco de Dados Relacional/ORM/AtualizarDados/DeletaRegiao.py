import sqlalchemy as sa
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CriacaoDasTabelas import CriacaoTabelasOcorrencias as oc

engine = sa.create_engine("sqlite:///BancoDados/ocorrencias.db")

metadado = sa.MetaData()
metadado.reflect(bind=engine)

tbMunicipio = metadado.tables[oc.Municipio.__tablename__]

atualizaRegiao = sa.delete(tbMunicipio).where(tbMunicipio.c.regiao == "Capital")

try:
    with engine.connect() as conn:
        conn.execute(atualizaRegiao)
        conn.commit()
    print("Dados excluidos com sucesso!")
except Exception as e:
    print(f"Erro ao deletar dados da tabela municipio: {e}")