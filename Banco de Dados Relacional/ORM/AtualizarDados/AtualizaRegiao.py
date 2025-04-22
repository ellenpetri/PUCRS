import sqlalchemy as sa
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CriacaoDasTabelas import CriacaoTabelasOcorrencias as oc

engine = sa.create_engine("sqlite:///BancoDados/ocorrencias.db")

metadado = sa.MetaData()
metadado.reflect(bind=engine)

tbMunicipio = metadado.tables[oc.Municipio.__tablename__]

atualizaRegiao = sa.update(tbMunicipio).values(
    {
        "regiao" : "Capital"
    }
).where(
    tbMunicipio.c.municipio == "Rio de Janeiro"
)

try:
    with engine.connect() as conn:
        conn.execute(atualizaRegiao)
        conn.commit()
    print("Dados atualizados com sucesso!")
except Exception as e:
    print(f"Erro ao atualizar a tabela municipio: {e}")