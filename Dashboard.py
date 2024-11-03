import streamlit as st
import pandas as pd
import altair as alt


st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)
col1.metric("Realisasi Anggaran", "35%")
col2.metric("Total Porsi", "89100", "-120")
col3.metric("Variasi Menu", "5", "-30")


# Membuat DataFrame
df = pd.read_csv("Book2.csv", sep=';')
c1, c2 = st.columns(2)
with c1:
    st.write('Variasi Menu tiap Minggu')
    #st.bar_chart(df, x='Hari', y='Persentase Menu', color= 'Menu', horizontal = True)

with c2:
    st.write('Hasil Evaluasi Computer Vision')
    source = pd.DataFrame({"Evaluasi": ['Porsi sedikit', 'Menu monoton', 'Bukan makanan bergizi', 'Sesuai'], "persentase": [10, 30, 10, 50]})
    #st.bar_chart(source, x='Evaluasi', y='persentase', color='Evaluasi')


st.subheader('Executive Summary')
with st.chat_message("AI"):
    st.write("Perlu adanya perbaikan dalam penggunaan anggaran dan pengawasan kualitas makanan. Penyajian menu yang kurang bervariasi serta porsi makanan yang tidak sesuai standar akan mengurangi efektivitas program. Diperlukan evaluasi pada sekolah sekolah yang terdeteksi melakukan penyimpangan atau ketidak sesuaian untuk dilakukan perbaikan proses pengadaan dan pendistribusian makanan, serta peningkatan kualitas pengawasan.")
