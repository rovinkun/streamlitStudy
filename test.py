import streamlit as st

st.title("hello")
st.header("ヘッダー")
st.text("test")
st.markdown("マークダウン")

st.button('ボタン')
st.selectbox('コンボボックス',('選択1','選択2'))
st.checkbox('チェックボックス')
st.radio('ラジオボタン',('ラジオボタン1','ラジオボタン2'))
st.date_input('日付インプット')
st.text_input('インプットボックス')
st.text_area('テキストエリア')
st.selectbox("メニューリスト", ("選択肢1", "選択肢2", "選択肢3")) 
st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3")) 