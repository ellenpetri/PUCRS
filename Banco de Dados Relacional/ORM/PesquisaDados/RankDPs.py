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


#Apresentar um ranqueamento de todas as delegacias de polícia localizadas na capital pela quantidade de ocorrencias

RankDP = pd.DataFrame(
    sessao.query(
    oc.Dp.nome.label("DP"),
    sa.func.sum(oc.Ocorrencias.qtde).label("Total")
    ).join(
        oc.Ocorrencias,
        oc.Ocorrencias.codDP == oc.Dp.codDP
    ).join(
        oc.Municipio,
        oc.Municipio.codIBGE == oc.Municipio.codIBGE
    ).where(
        oc.Municipio.regiao == "Capital"
    ).group_by(
        oc.Dp.nome
    ).order_by(
        sa.func.sum(oc.Ocorrencias.qtde).label("Total").desc()
    ).all()
)

print(RankDP)