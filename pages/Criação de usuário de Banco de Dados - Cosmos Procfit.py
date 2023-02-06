import streamlit as st
                    
from PIL import Image 
                    
st.caption("""
Criação usuário de Banco de Dados Cosmos Procfit
""") 
                    
image= Image.open(f'imagens/exemplo_do_SQL.odt')
                    
st.image(image)
                    
image1= Image.open(f'imagens/criação_usuario_leitura.odt')
                    
st.image(image1)            
                    
st.code("""


Acessar o servidor via NX ou X2GO;
Acessar o  pgAdmin III onde está a base que terá o acesso liberado;
Acessar a conexão Postgres (senha: supertux);
Localizar a base de dados em uso;
Clicar sobre o botão SQL (desenho de uma Lupa);
Copiar os comandos para criação do usuário, definindo um valor para as variáveis usuário e senha, e executar (Ctrl + E);


do $$                                                                                                
declare
  -- Defina o usuário e a senha aqui (não usar espaços, acentução etc. no usuário)
  usuario varchar := 'usuario';                                                                                          
  senha varchar := 'senha';
begin    
  /* Valida se as variáveis foram setadas */
  if (usuario = 'definir' or senha = 'definir') then
    raise exception 'As variáveis usuario e senha precisam ser definidas!';
  end if;

  /* Valida um tamanho mínimo para usuário e senha */
  if (length(usuario) < 5 or length(senha) < 4) then
    raise exception 'O usuário deve ter no mínimo 5 caracteres e a senha 4';
  end if;

  /* Valida o usuario */
  if (usuario !~ '^[0-9_a-zA-Z]+$') then
    raise exception 'Usuar apenas números, letras sem acentuação e _ para o nome do usuário';
  end if;  
  
  /* Exclui um possível usuário que já exista */
  execute format('drop role if exists %I', usuario);
 
  /* Cria o usuario */
  execute format('create role %I login password ''%s'' nosuperuser inherit nocreatedb nocreaterole connection limit 5', usuario, senha);
 
  /* Remove todos os privilégios que possam ter sido dados ao usuário */
  execute format('revoke all privileges on all tables in schema public from %I', usuario);
 
  /* Dá apenas os privilégios necessários.
  OBS: use o comando \dp no psql para ver todos os privilegios de todas as tabelas*/
  execute format('grant select on all tables in schema public to %I', usuario);

  /* Para que receba permissão de leitura em tabelas criadas posteriormente pelo chinchila*/
  execute format('alter default privileges for user chinchila in schema public grant select on tables to %I', usuario);

end; $$



Importante: Informar o usuário e senha que será criado nas linhas : 
  -- Defina o usuário e a senha aqui (não usar espaços, acentução etc. no usuário)
  usuario varchar := 'usuario';                                                                                          
  senha varchar := 'senha';

Conforme exemplo imagem 1 anexada.

Após isso deverá executar!

Abrir o terminal e logar como root;

Executar o comando para criar a variável de ambiente e verificar a versão do PostgreSQL:

PG_DATA=$(ps aux | grep -oP '^postgres .*postmaster.*-D *\K.*')
PG_VERSION=$(cat $PG_DATA/PG_VERSION)
echo "Versão PG: $PG_VERSION"


Executar o comando para editar o pg_hba.conf da versão em uso:
vim $PG_DATA/pg_hba.conf


Adicionar a linha com as informações de quem e como será permitido o acesso a base de dados:
Versões do PostgreSQL abaixo 14 vão utilizar host all USUARIO samenet md5 informando no lugar do USUÁRIO o usuário definido no passo 5 (alterar o all pelo IP de acordo com o endereçamento de IP da rede do cliente);
Versões posteriores ou igual a PostgreSQL14 utilizam outro método de autenticação o scram-sha-256. A Linha deverá ser salva host all USUARIO samenet scram-sha-256 informando no lugar do USUÁRIO o usuário definido no passo 5 (alterar o all pelo IP de acordo com o endereçamento de IP da rede do cliente);


Executar o comando para recarregar as liberações do PostgreSQL:
service postgresql-${PG_VERSION} reload

O arquivo pg_hba.conf exemplo conforme exemplo imagem 2 anexada.



Passar ao cliente o usuário e senha de acesso definidos.
""",language='sql')