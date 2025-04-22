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

#Apresentar um ranqueamento de todos as DPs pela quatidade de roubo e furtos de veículos, no interior
RankDP = pd.DataFrame( sessao.query(
                oc.Dp.nome.label("DP"), 
                sa.func.sum(oc.Ocorrencias.qtde).label("Total")
            ).join(
                oc.Ocorrencias,
                oc.Ocorrencias.codDP == oc.Dp.codDP
            ).join(
                oc.Municipio,
                oc.Municipio.codIBGE == oc.Ocorrencias.codIBGE
            ).where(
                oc.Municipio.regiao == "Interior",
                sa.or_(oc.Ocorrencias.ocorrencia == "roubo_veiculo", oc.Ocorrencias.ocorrencia == "furto_veiculo")
            ).group_by(
                oc.Dp.nome
            ).order_by(
                sa.func.sum(oc.Ocorrencias.qtde).desc()
            ).all()
        )

print(RankDP)

