import streamlit as st
                    
from PIL import Image 
                    
st.caption('''
- Acessar a base do ESC com usuário chinchila.
- Pegar o ID correspondente as loja.
- Copiar e executar a consulta em outra instância F5 - Executar.

''')            
                    
st.code('''
select * from unidadenegocio;
ID Destino = xxxxxx
ID Origem = yyyyyy

select
  'select nq(''insert into custoproduto (id,produtoid,unidadenegocioid,custo,customedio) values ('||generate_id()||','||produtoid||',xxxxxx,'||custo||','||customedio||')'');'
from custoproduto  where unidadenegocioid = yyyyyy;  --lojaorigem''',language='sql')