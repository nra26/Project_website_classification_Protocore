import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Klasifikasi Perbandingan Protocore", layout="centered")

# Memasukkan model
with open("Protocore_model.pkl", "rb") as file:
    model = pickle.load(file)

# Judul
st.title("Klasifikasi perbandingan protocore α sapphire level 0 untuk companion foreseer")

# Form
with st.form("classification_form"):
    col1, col2 = st.columns(2)

    # PROTOCORE 1
    with col1:
        st.subheader("Protocore 1")
        st.image("gambar_protocore.jpg", use_column_width=False, width=200)
        label_col, value_col = st.columns([2, 1])
        with label_col:
            st.text_input("Main Stat 1", value="HP", disabled=True)
        with value_col:
            st.number_input("label", value=1000.0, step=0.0, disabled=True, label_visibility="hidden")

        substat_protocore_1_1, isi_1_1 = st.columns([2,1])
        with substat_protocore_1_1:
            substat_protocore_1_1_val = st.selectbox("Substat", ("None","HP","DEF","ATK","HP Bonus","DEF Bonus","ATK Bonus","CRIT Damage","CRIT Rate","OATH Strength","DMG Boost to Weakened"), key="p1_1")
        with isi_1_1:
            isi_1_1_val = st.number_input("", value=0.0, key="v1_1")

        substat_protocore_1_2, isi_1_2 = st.columns([2,1])
        with substat_protocore_1_2:
            substat_protocore_1_2_val = st.selectbox("", ("None","HP","DEF","ATK","HP Bonus","DEF Bonus","ATK Bonus","CRIT Damage","CRIT Rate","OATH Strength","DMG Boost to Weakened"), key="p1_2")
        with isi_1_2:
            isi_1_2_val = st.number_input("", value=0.0, key="v1_2")

        substat_protocore_1_3, isi_1_3 = st.columns([2,1])
        with substat_protocore_1_3:
            substat_protocore_1_3_val = st.selectbox("", ("None","HP","DEF","ATK","HP Bonus","DEF Bonus","ATK Bonus","CRIT Damage","CRIT Rate","OATH Strength","DMG Boost to Weakened"), key="p1_3")
        with isi_1_3:
            isi_1_3_val = st.number_input("", value=0.0, key="v1_3")

        substat_protocore_1_4, isi_1_4 = st.columns([2,1])
        with substat_protocore_1_4:
            substat_protocore_1_4_val = st.selectbox("", ("None","HP","DEF","ATK","HP Bonus","DEF Bonus","ATK Bonus","CRIT Damage","CRIT Rate","OATH Strength","DMG Boost to Weakened"), key="p1_4")
        with isi_1_4:
            isi_1_4_val = st.number_input("", value=0.0, key="v1_4")

    # PROTOCORE 2
    with col2:
        st.subheader("Protocore 2")
        st.image("gambar_protocore.jpg", use_column_width=False, width=200)
        label_col, value_col = st.columns([2, 1])
        with label_col:
            st.text_input("Main Stat 2", value="HP", disabled=True)
        with value_col:
            st.number_input("sub stat 2", value=1000.0, step=0.0, disabled=True, label_visibility="hidden")

        substat_protocore_2_1, isi_2_1 = st.columns([2,1])
        with substat_protocore_2_1:
            substat_protocore_2_1_val = st.selectbox("Substat", ("None","HP","DEF","ATK","HP Bonus","DEF Bonus","ATK Bonus","CRIT Damage","CRIT Rate","OATH Strength","DMG Boost to Weakened"), key="p2_1")
        with isi_2_1:
            isi_2_1_val = st.number_input("", value=0.0, key="v2_1")

        substat_protocore_2_2, isi_2_2 = st.columns([2,1])
        with substat_protocore_2_2:
            substat_protocore_2_2_val = st.selectbox("", ("None","HP","DEF","ATK","HP Bonus","DEF Bonus","ATK Bonus","CRIT Damage","CRIT Rate","OATH Strength","DMG Boost to Weakened"), key="p2_2")
        with isi_2_2:
            isi_2_2_val = st.number_input("", value=0.0, key="v2_2")

        substat_protocore_2_3, isi_2_3 = st.columns([2,1])
        with substat_protocore_2_3:
            substat_protocore_2_3_val = st.selectbox("", ("None","HP","DEF","ATK","HP Bonus","DEF Bonus","ATK Bonus","CRIT Damage","CRIT Rate","OATH Strength","DMG Boost to Weakened"), key="p2_3")
        with isi_2_3:
            isi_2_3_val = st.number_input("", value=0.0, key="v2_3")

        substat_protocore_2_4, isi_2_4 = st.columns([2,1])
        with substat_protocore_2_4:
            substat_protocore_2_4_val = st.selectbox("", ("None","HP","DEF","ATK","HP Bonus","DEF Bonus","ATK Bonus","CRIT Damage","CRIT Rate","OATH Strength","DMG Boost to Weakened"), key="p2_4")
        with isi_2_4:
            isi_2_4_val = st.number_input("", value=0.0, key="v2_4")

    # Tombol BANDINGKAN
    _, col_btn, _ = st.columns([2, 1, 2])
    with col_btn:
        submitted = st.form_submit_button("BANDINGKAN")

# Proses prediksi
if submitted:
    stat_mapping = {
        "None": 0, "HP": 1, "ATK": 2, "DEF": 3,
        "HP Bonus": 4, "ATK Bonus": 5, "DEF Bonus": 6,
        "CRIT Rate": 7, "CRIT Damage": 8, "OATH Strength": 9,
        "DMG Boost to Weakened": 10
    }

    data = pd.DataFrame([[  
        stat_mapping[substat_protocore_1_1_val], isi_1_1_val,
        stat_mapping[substat_protocore_1_2_val], isi_1_2_val,
        stat_mapping[substat_protocore_1_3_val], isi_1_3_val,
        stat_mapping[substat_protocore_1_4_val], isi_1_4_val,
        stat_mapping[substat_protocore_2_1_val], isi_2_1_val,
        stat_mapping[substat_protocore_2_2_val], isi_2_2_val,
        stat_mapping[substat_protocore_2_3_val], isi_2_3_val,
        stat_mapping[substat_protocore_2_4_val], isi_2_4_val
    ]], columns=[
        'sub_stat_1_1', 'isi_1_1',
        'sub_stat_1_2', 'isi_1_2',
        'sub_stat_1_3', 'isi_1_3',
        'sub_stat_1_4', 'isi_1_4',
        'sub_stat_2_1', 'isi_2_1',
        'sub_stat_2_2', 'isi_2_2',
        'sub_stat_2_3', 'isi_2_3',
        'sub_stat_2_4', 'isi_2_4'
    ])
    if (data == 0).all(axis=None):
        st.warning("⚠️ Isi data terlebih dahulu sebelum melakukan perbandingan.")
    else:
        prediction = model.predict(data)[0]
        # Reset semua input ke default
        data = pd.DataFrame()
        if prediction == 0.0:
            st.markdown(f'<p class="prediction-text">Prediksi : Protocore 1 Unggul</p>', unsafe_allow_html=True)
        elif prediction == 1.0:
            st.markdown(f'<p class="prediction-text">Prediksi : Protocore 2 Unggul</p>', unsafe_allow_html=True) 
                
st.markdown("""
### Deskripsi
Form di atas digunakan untuk membandingkan **dua Protocore** berdasarkan substat yang ada.

Substat diisi berdasarkan isi 2 protocore α sapphire lvl. 0 yang ingin dibandingkan 
""")