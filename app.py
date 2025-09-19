import streamlit as st
import pandas as pd
from functions import *
from untuk0100 import *
from variables_1 import *
from untuk0200 import *
from oop_module import *

st.title("MNC Insurance - Generator Laporan Bulanan OJK")

# --- Inisialisasi session_state ---
if "df1" not in st.session_state:
    st.session_state.df1 = None
if "df2" not in st.session_state:
    st.session_state.df2 = None
if "Object1" not in st.session_state:
    st.session_state.Object1 = None

# --- Form upload File 0100 ---
with st.form("form1"):
    file1 = st.file_uploader("Upload Excel File 0100", type=["xlsx", "xls"], key="file1")
    submit1 = st.form_submit_button("Submit File 0100")

    if submit1 and file1 is not None:
        st.session_state.df1 = pd.read_excel(file1, dtype = 'str')
        st.write("Preview File 0100:")
        st.dataframe(st.session_state.df1)

# --- Form upload File 0200 ---
with st.form("form2"):
    file2 = st.file_uploader("Upload Excel File 0200", type=["xlsx", "xls"], key="file2")
    submit2 = st.form_submit_button("Submit File 0200")

    if submit2 and file2 is not None:
        st.session_state.df2 = pd.read_excel(file2, dtype = 'str')
        st.write("Preview File 0200:")
        st.dataframe(st.session_state.df2)

# --- Input Periode Pelaporan ---
periode = st.date_input("Pilih Periode Pelaporan")
periode_str = periode.strftime("%Y%m%d")

# --- Tombol Proses Data ---
if st.button("Proses Data"):
    if st.session_state.df1 is not None and st.session_state.df2 is not None:
        # Buat object Apolo
        st.session_state.Object1 = Apolo(
            st.session_state.df1,
            st.session_state.df2,
            periode_lapor=periode_str
        )
        st.success(f"Object Apolo berhasil dibuat untuk periode {periode_str}")

    else:
        st.warning("Silakan upload kedua file sebelum memproses data.")

# --- Jika Object1 sudah ada, tampilkan tombol download ---
if st.session_state.Object1 is not None:
    Object1 = st.session_state.Object1

    # Generate file 0100
    data0100 = Object1.generate_0100()
    st.download_button(
        label="Download File 0100",
        data=data0100,
        file_name=f"PLSASRUK-0100-R-M-{int(periode.strftime("%Y%m%d"))}-2000003822-01.txt",
        mime="text/plain"
    )

    # Kalau nanti ada generate_0200, tinggal tambahkan di sini:
    if hasattr(Object1, "generate_0200"):
        data0200 = Object1.generate_0200()
        st.download_button(
            label="Download File 0200",
            data=data0200,
            file_name=f"PLSASRUK-0200-R-M-{int(periode.strftime("%Y%m%d"))}-2000003822-01.txt",
            mime="text/plain"
        )
