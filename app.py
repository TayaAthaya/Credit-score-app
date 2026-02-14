import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model_pinjaman.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

st.title("Aplikasi Prediksi Kelayakan Pinjaman 🏦")
st.write("Silakan masukkan data nasabah di bawah ini:")


col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    married = st.selectbox("Status Pernikahan", ["Yes", "No"])
    dependents = st.selectbox("Jumlah Tanggungan", ["0", "1", "2", "3+"])
    education = st.selectbox("Pendidikan", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Wiraswasta?", ["Yes", "No"])

with col2:
    applicant_income = st.number_input("Pendapatan Bulanan (USD)", min_value=0)
    coapplicant_income = st.number_input("Pendapatan Pendamping (USD)", min_value=0)
    loan_amount = st.number_input("Jumlah Pinjaman (Ribuan USD)", min_value=0)
    loan_term = st.number_input("Durasi Pinjaman (Hari)", min_value=0)
    credit_history_label = st.selectbox("Apakah Memiliki Riwayat Kredit yang Baik?", ["Ya", "Tidak"])
    if credit_history_label == "Ya":
        credit_history = 1.0
    else:
        credit_history = 0.0
    property_area = st.selectbox("Area Properti", ["Rural", "Semiurban", "Urban"])

if st.button("Cek Kelayakan Pinjaman"):
    input_data = {
        "Gender": 1 if gender == "Male" else 0,
        "Married": 1 if married == "Yes" else 0,
        "Dependents": int(dependents.replace('3+', '3')),
        "Education": 1 if education == "Graduate" else 0,
        "Self_Employed": 1 if self_employed == "Yes" else 0,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": {"Rural": 0, "Semiurban": 1, "Urban": 2}[property_area]
    }

    df_input = pd.DataFrame([input_data])

    prediction = model.predict(df_input)

    if prediction[0] == 1:
        st.success("Selamat! Pinjaman Anda kemungkinan DISETUJUI. 🎉")
    else:
        st.error("Mohon maaf, Pinjaman Anda kemungkinan DITOLAK. ❌")