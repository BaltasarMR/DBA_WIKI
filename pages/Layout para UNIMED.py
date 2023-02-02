import streamlit as st
                
from PIL import Image 
                
st.markdown('''<b>
No dia 19/11 no chamado de número 0021889 a Droga Uchoas (0796-02345) solicitando um relatório personalizado com as seguintes informações (O nome da empresa, matricula, nome do funcionário e débitos. Ambos relatórios separados conforme cada crediário(empresa). As planilhas precisam também ser em Excel, para importação das respectivas empresas)


</b>''',unsafe_allow_html=True) 
                
image= Image.open(f'imagens/exportacaounimed.png')
                
st.image(image)
                
image1= Image.open(f'imagens/escolherdatainicialefinal.png')
                
st.image(image1)            
                
st.code('''
--------------------------------------------------------------------------------------------------------------------------------
Script
--------------------------------------------------------------------------------------------------------------------------------

SELECT 
 cast(crediario.nome as varchar) as empresa,
 cast(LTRIM(cliente.numerocartao)as varchar) AS matricula,
 cast(SUBSTRING(pessoa.nome,1,30)as varchar) AS funcionario,
 replace(cast(ROUND(SUM(crediarioReceber.valor),2)as varchar),'.', ',') AS debitos
FROM crediarioReceber
 JOIN cliente on cliente.id = crediarioReceber.clienteID
 JOIN crediario on crediario.id = cliente.crediarioID
 JOIN pessoa on pessoa.id = cliente.pessoaid
WHERE
 crediario.id = COLOCAR O ID DO CREDIÁRIO AQUI
 AND 
 crediarioReceber.status IN ('A', 'F')
 AND 
 datafechamento::date >= ${DATA_INICIAL_DDMMAAAA}
 AND
 datafechamento::date <=${DATA_FINAL_DDMMAAAA}
GROUP BY
     1,2,3
ORDER BY FUNCIONARIO,MATRICULA

--------------------------------------------------------------------------------------------------------------------------------
Cabeçalho
--------------------------------------------------------------------------------------------------------------------------------

SELECT 
 cast('empresa'as varchar)as empresa,
 cast('matricula'as varchar)as matricula,
 cast('funcionario'as varchar)as funcionario,
 cast('debitos'as varchar)as debitos

--------------------------------------------------------------------------------------------------------------------------------
Observações
--------------------------------------------------------------------------------------------------------------------------------

-  Foi colocado um  parâmetro nesse código para quando 
for realizar a exportação do arquivo, colocar a data de fechamento da fatura 
tanto no inicial quanto na final.

''',language='sql')