# mol-draw
Upload mol file and draw structure


https://s-yagyu-mol-draw-mol-upload-draw-cloud-x5cmef.streamlit.app/



### Stremlit Cloudにデプロイするのに苦労したこと

こちらの記事が参考になりました。感謝！

[hemoinfo のアプリをStreamlitを使ってDeployする #streamlit #RDKit #souyakuAC2020](https://iwatobipen.wordpress.com/2020/12/20/chemoinfo-%E3%81%AE%E3%82%A2%E3%83%97%E3%83%AA%E3%82%92streamlit%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6deploy%E3%81%99%E3%82%8B-streamlit-rdkit-souyakuac2020/)

[chem_streamlit　Github](https://github.com/iwatobipen/chem_streamlit)

- Conda のenvironment.ymlで最初トライ
  -> うまくいかなかった
- requirements.txtに変更
　 -> from rdkit.Chem import Draw　のインポートエラー
- packages.txtの追加
  　-> うまくいった

