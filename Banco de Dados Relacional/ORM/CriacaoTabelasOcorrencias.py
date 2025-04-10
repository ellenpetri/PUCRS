import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///BancoDados/ocorrencias.db")

base = orm.declarative_base()

#Primeiro as tabelas que não possuem chave estrangeira

#Tabela tbDp
class Dp(base):
    __tablename__ = "tbDp"
    
    codDP = sa.Column(sa.INTEGER, primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    endereco = sa.Column(sa.VARCHAR(255), nullable=False)
    
#Tabela tbResponsavelDP
class ResponsavelDP(base):
    __tablename__ = "tbResponsavelDP"
    
    codDP = sa.Column(sa.INTEGER, primary_key=True, index=True)
    delegado = sa.Column(sa.VARCHAR(100), nullable=False)
    

#Tabela Municipio
class Municipio(base):
    __tablename__ = "tbMunicipio"
    
    codIBGE = sa.Column(sa.INTEGER, primary_key=True, index=True) 
    municipio = sa.column(sa.VARCHAR(100), nullable=False)
    regiao = sa.column(sa.VARCHAR(25), nullable=False)  

#Agora as tabelas que possuem chave estrangeira de tabelas que já criamos

#Tabela Ocorrencias
class Ocorrencias(base):
    __tablename__ = "tbOcorencias"
    
    indRegistro = sa.column(sa.INTEGER, primary_key=True, index=True)
    codDP = sa.column(sa.INTEGER, sa.ForeignKey("tbDp.codDP", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
    codIBGE = sa.column(sa.INTEGER, sa.ForeignKey("tbMunicipio.codIBGE", ondelete="NO ACTION", onupdate="CASCADE", index=True))
    ano = sa.column(sa.CHAR(4), nullable=False)
    mes = sa.Column(sa.VARCHAR(2), nullable=False)
    ocorrencia = sa.Column(sa.VARCHAR(100), nullable=False)
    qtde = sa.Column(sa.INTEGER, nullable=False)
    
try:
    #criar as tabelas
    base.metadata.create_all(engine) 
    print("Tabelas criadas")
except ValueError:
    ValueError()

    