import streamlit as st
                    
from PIL import Image 
                    
st.caption("""
Gerar o arquivo de preços da Abcfarma 

""")            
                    
st.code("""
Gerar Arquivo de PREÇOS ABCFARMA - Guia de Medicamentos


- Deverá acessar um cliente pelo Hamaster
- Abrir o Pgadmin
- Acessar o banco de dados 


Script de Geração:
Salvar como: guiamedicamento.csv
SELECT lpad(codigobarras,13,'0')||rpad(nome,30,' ')||lpad('',10,'0')||lpad('',10,'0')
||rpad('',10,' ')||lpad(replace(pmf18::numeric(15,2)::varchar,'.',''),10,'0')||lpad(replace(pmc18::numeric(15,2)::varchar,'.',''),10,'0')
||lpad(replace(pmf17::numeric(15,2)::varchar,'.',''),10,'0')||lpad(replace(pmc17::numeric(15,2)::varchar,'.',''),10,'0')
||lpad(replace(pmf12::numeric(15,2)::varchar,'.',''),10,'0')||lpad(replace(pmc12::numeric(15,2)::varchar,'.',''),10,'0')
||(case when listapis='N' then '0' when listapis='P' then '1' else '2' end)
--||(case when categoria='G' then 'G' else ' ' end)
||(case when tipomedicamento='G' then 'G' else ' ' end)
||(case when tipopreco='M' then 'M' else 'L' end)
||to_char(datavigencia::date,'YYYYMMDD')::varchar
||'0'
 FROM 
  guiamedicamento

Gerar em .csv o arquivo 
""",language='sql')