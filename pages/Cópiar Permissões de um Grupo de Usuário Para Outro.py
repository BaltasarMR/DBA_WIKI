import streamlit as st
                    
from PIL import Image 
                    
st.caption("""
Precisa criar um novo grupo de usuário com as mesmas permissões de um grupo já existente.
""")            
                    
st.code("""
----Copiar permissões de um grupo de usuário para outro----

-- 1) Criar no Alpha7 um novo Grupo de Usuário com o nome que desejar (Cadastro Básico > Usuário > Grupo de Usuário > Incluir)

-- 2) Na base oficial, pegar os IDs dos grupos de usuário
SELECT * FROM GrupoUsuario;

Grupo de Destino xxxxx	ex: 3599759;"ATENDENTE 2"
Grupo de Origem yyyyy	ex: 363;"ATENDENTE"

-- 3) Substituir informações dos grupos de usuário no nq() e rodar uma vez
SELECT *, 
'select nq(''insert into PermissaoGrupoUsuario(id,chave,grupousuarioid,valor) values('||generate_id()||','''''||chave||''''',xxxxx,'||valor||')'');'
FROM PermissaoGrupoUsuario WHERE grupousuarioid = yyyyy;

/* Confirmar se o Grupo de Destino recebeu as permissões do Grupo de Origem
(CASO NÃO TRAGA NENHUMA LINHA, A CÓPIA FOI FEITA ERRADA)*/
SELECT * FROM PermissaoGrupoUsuario WHERE grupousuarioid = xxxxx""",language='sql')