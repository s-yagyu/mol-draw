# ref https://cafe-mickey.com/python/streamlit-6/
# ref https://github.com/hurutoriya/streamlist-file-uploader-example/blob/main/streamlit_pdf_uploader/main.py

from pathlib import Path
from tempfile import NamedTemporaryFile

import streamlit as st
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import inchi
from rdkit.Chem import Draw

st.title('Mol Drawing')

# Fileの拡張子をチェックしてくる
uploaded_file = st.file_uploader("Mol file upload", type='mol')


if uploaded_file is not None:
    file_name = uploaded_file.name

    
    with NamedTemporaryFile(delete=False) as f:
        fp = Path(f.name)
        fp.write_bytes(uploaded_file.getvalue())
    
        m_ = Chem.MolFromMolFile(f'{f.name}')
        m_img = Draw.MolToImage(m_,)
        m_smiles = Chem.MolToSmiles(m_)
        m_inchi = inchi.MolToInchi(m_, options='', logLevel=None, treatWarningAsError=False)
        m_inchikey = Chem.MolToInchiKey(m_)
    
    # ファイルを削除  
    fp.unlink()
    
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    ax.set_title(f"InchiKey : {m_inchikey}")
    ax.imshow(m_img)
    ax.set_xticks([])
    ax.set_yticks([])    
    fig.suptitle(f'{file_name}')
    plt.tight_layout()

    st.pyplot(fig)
        
