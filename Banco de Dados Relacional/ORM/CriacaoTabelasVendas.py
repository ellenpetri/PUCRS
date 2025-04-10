import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///BancoDados/vendas.db")

base = orm.declarative_base()

#Primeiro as tabelas que não possuem chave estrangeira

#Tabela cliente
class cliente(base):
    __tablename__ = "cliente"
    
    cpf = sa.Column(sa.CHAR(14), primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email = sa.Column(sa.VARCHAR(50), nullable=False)
    genero = sa.Column(sa.CHAR(1))
    salario = sa.Column(sa.DECIMAL(10, 2))
    dia_mes_aniversario = sa.Column(sa.CHAR(5))
    bairro = sa.Column(sa.VARCHAR(50))
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))
    
#Tabela Fornecedor
class fornecedor(base):
    __tablename__ = "fornecedor"
    
    registro_fornecedor = sa.Column(sa.INTEGER, primary_key=True,  index=True)
    nome_fantasia = sa.Column(sa.VARCHAR(50), nullable=False)
    razao_social = sa.Column(sa.VARCHAR(100), nullable=False)
    cidade = sa.Column(sa.VARCHAR(50), nullable=False)
    uf = sa.Column(sa.CHAR(2), nullable=False)


#Tabela Vendedor
class vendedor(base):
    __tablename__ = "vendedor"
    
    registro_vendedor = sa.Column(sa.INTEGER, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), nullable=False)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email = sa.Column(sa.VARCHAR(50), nullable=False)
    genero = sa.Column(sa.CHAR(1))

#Agora as tabelas que possuem chave estrangeira de tabelas que já criamos

#Tabela Produto
class produto(base):
    __tablename__ = "produto"
    
    cod_Barras = sa.Column(sa.INTEGER, primary_key=True, index=True)
    registro_fornecedor = sa.Column(sa.INTEGER, sa.ForeignKey("fornecedor.registro_fornecedor", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
    dsc_produto = sa.Column(sa.VARCHAR(100), nullable=False)
    genero = sa.Column(sa.CHAR(1), nullable=False)

#Tabela Vendas
class vendas(base):
    __tablename__ = "vendas"
    
    id_Transacao = sa.Column(sa.INTEGER, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), sa.ForeignKey("cliente.cpf", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
    registro_vendedor = sa.Column(sa.INTEGER, sa.ForeignKey("vendedor.registro_vendedor", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
    cod_Barras = sa.Column(sa.INTEGER, sa.ForeignKey("produto.cod_Barras", ondelete="NO ACTION", onupdate="CASCADE"), index=True)



try:
    #criar as tabelas
    base.metadata.create_all(engine)
    print("Tabelas criadas")
except ValueError:
    ValueError()















