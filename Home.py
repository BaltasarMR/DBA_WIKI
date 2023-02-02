import streamlit as st
from pathlib import Path
import shutil
import os
import pandas as pd

directory = Path('pages')

st.title('Documentação DBA')

CriarDocumentacao = st.checkbox('Criar?',value=True)

if CriarDocumentacao == True:
    
    NomePagina = st.text_input('Nome da Pagina')

    DescricaoProblema = st.text_area('Descrição do Problema')

    Imagem1 = st.file_uploader(label = "Primeira Imagem")

    ComandoSQL = st.text_area('Coloque o comando SQL utilizado')

    Imagem2 = st.file_uploader(label = "Segunda Imagem")

    BotaoCriarDOC = st.button('Criar o DOC')
    
    def CriarDOC():
        if DescricaoProblema == '':
            st.error('**Você esqueceu de colocar o problema!!**')
        elif ComandoSQL == '':
            st.error('**Você esqueceu de colocar o comando para a solução!!**')
        elif Imagem1 == None:
            st.error('**Você esqueceu de anexar uma evidência!!**')
        elif Imagem2 == None:
            st.error('**Você esqueceu de anexar uma evidência!!**')
        
        else:
            save_folder = 'imagens/'
            save_path1 = Path(save_folder, Imagem1.name)
            with open(save_path1, mode='wb') as w:
                w.write(Imagem1.getvalue())
        
            save_path2 = Path(save_folder, Imagem2.name)
            with open(save_path2, mode='wb') as w:
                w.write(Imagem2.getvalue())        
            if directory.exists():
                file = open(f'pages/{NomePagina}.py',"w",encoding='utf-8')
                file.write(f"""import streamlit as st
                \nfrom PIL import Image 
                \nst.markdown('''<b>\n{DescricaoProblema}\n</b>''',unsafe_allow_html=True) 
                \nimage= Image.open(f'imagens/{Imagem1.name}')
                \nst.image(image)
                \nimage1= Image.open(f'imagens/{Imagem2.name}')
                \nst.image(image1)            
                \nst.code('''\n{ComandoSQL}''',language='sql')""")
                file.close()

    if BotaoCriarDOC:
        CriarDOC()

else:
    
    for diretorio,subpastas,arquivos in os.walk('./pages'):
        NomeArquivos = st.selectbox('',(arquivos))
        TirandoPY = NomeArquivos.replace('.py','')
        ArquivoURL = TirandoPY.replace(' ','_')
        st.markdown(f'<b><a href="{ArquivoURL}">{TirandoPY}</a></b>',unsafe_allow_html=True)