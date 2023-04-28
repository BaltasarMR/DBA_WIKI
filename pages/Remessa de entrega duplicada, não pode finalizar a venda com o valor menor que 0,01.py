import streamlit as st
                    
from PIL import Image 
                    
st.caption("""
Ao finalizar uma venda o sistema não permite pois o valor deve ser maior que 0,01, mesmo a venda tendo o valor correto. O sistema duplica a remessa de entrega para a venda e considera a segunda com valor 0,00 no momento da finalização, sendo necessário excluí-la.
""")            
                    
st.code("""
----Remessa de entrega duplicada, não pode ser finalizada a venda com a forma de pagamento com o valor de 0,01----

-- 1) Pegar ID da Remessa de entrega duplicada na venda(Venda > Venda > Localizar e Selecionar a venda com COO, data e etc > Detalhes > Aba Entrega > Seção Remessas)

-- 2) Fazer select e backup dos dados da entrega duplicada da venda ex: 300000688566;"B";300000688125;300000688565
SELECT * FROM entregaremessa WHERE remessaid = xxxxx

-- 3) Feito backup, preencher o ID da entrega duplicada da venda no NQ
SELECT nq('delete from entregaremessa where id=xxxxx;');

-- 4) Conferir no Alpha7 se consta apenas uma remessa de entrega naquela venda""",language='sql')