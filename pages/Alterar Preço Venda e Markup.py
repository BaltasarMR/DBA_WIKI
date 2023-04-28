import streamlit as st
                    
from PIL import Image 
                    
st.caption("""
Precisa alterar o preço de venda e o markup de alguns produtos a partir de uma planilha CSV.
""")            
                    
st.code("""
----Alterar Preço Venda e Markup----

/* Verifica Preço venda, Preço rerefencial e Markup atual */
SELECT codigobarras, precovenda, precoreferencial, (((precovenda-precoreferencial)::numeric(15,2))/precoreferencial*100)::numeric(15,4) as Markup FROM embalagem; 


/* Deve-se ter uma planilha CSV contendo Nome, Codigo de barras e o Preço de venda já correto,
com o nome "precos.csv" salva na pasta /tmp e com todas as permissões de leitura e escrita */

--1) Criar tabela TMP para fazer o copy
CREATE TABLE tmp_preco(
nome varchar,
codigobarras varchar,
precovenda varchar
);

--2) Fazer o copy da planilha CSV para a tabela no banco
COPY tmp_preco FROM '/tmp/precos.csv' DELIMITER ';' CSV HEADER 

--3) Fazer o update do Preço venda atual pelo correto já importado na tabela tmp_preco no passo 2
SELECT 
'select nq(''update embalagem set precovenda = '||replace(replace(replace(tmp_preco.precovenda,'.','='),',','.'),'=','')::numeric(15,4)||' where id = '||embalagem.id||' '');',
FROM tmp_preco
JOIN embalagem ON embalagem.codigobarras = tmp_preco.codigobarras;

--4) Fazer o update do Markup com base no Preço venda importado no passo 3

/* IMPORTANTE: Sempre executar o script abaixo depois de realizar o passo 3 para atualizar o Markup com base nos novos preços importados,
caso contrário o Markup estará incorreto pois o sistema não recalculará o novo Markup quando os preços forem inseridos via banco */

SELECT 
'select nq(''update embalagem set markup = '||(((embalagem.precovenda-embalagem.precoreferencial)::numeric(15,2))/embalagem.precoreferencial*100)::numeric(15,4)||' where id = '||embalagem.id||' '');'
FROM tmp_preco
JOIN embalagem ON embalagem.codigobarras = tmp_preco.codigobarras;

--5) Após conferir/validar o sucesso do procedimento no sistema, excluir a tabela TMP para evitar erros na realização de um backup futuro da base
DROP TABLE tmp_preco;
""",language='sql')