import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CriacaoDasTabelas import CriacaoTabelasOcorrencias as oc

engine = sa.create_engine("sqlite:///BancoDados/ocorrencias.db")

Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()


#Apresentar um ranqueamento de todos os municipios pela quantidade de ocorrencias de roubo de veículos

RankMunicipio = pd.DataFrame(
    sessao.query(
        oc.Municipio.municipio.label("Município"),
        sa.func.sum(oc.Ocorrencias.qtde).label("Total")
    ).join(
        oc.Ocorrencias,
        oc.Ocorrencias.codDP == oc.Municipio.codIBGE
    ).where(
        oc.Ocorrencias.ocorrencia == "roubo_veiculo"
    ).group_by(
        oc.Municipio.municipio
    ).order_by(
        sa.func.sum(oc.Ocorrencias.qtde).desc()
    ).all()
)

print(RankMunicipio)