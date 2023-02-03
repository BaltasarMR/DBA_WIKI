import streamlit as st
                    
from PIL import Image 
                    
st.caption("""
- Acessar a base do ESC com usuário chinchila .
- Pegar o ID correspondente as loja.
- Copiar e executar a consulta em outra instância F5 - Executar.
""")            
                    
st.code("""
select * from unidadenegocio;
ID Destino = xxxxxx
ID Origem = yyyyyy

 select 
   'select execute_native_query(''insert into historicovenda(id,unidadenegocioid,embalagemid,data,quantidade) values('||generate_id()||',xxxxxx,'||embalagemid||','''''||data||''''','||quantidade||')'',''ESC'',''admin'');'
from historicovenda
where unidadenegocioid = yyyyyy 
 and data >= now() - interval '3' month""",language='sql')