import streamlit as st
import pickle

# 加载模型
# 将模型文件路径改为相对路径，假设模型文件和 app.py 位于同一目录
model_path = 'random_forest_model.pkl'
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Model file not found: {model_path}. Please ensure it is uploaded.")

# 网页标题
st.title("Random Forest Model Predictor")

# 手动设置特征范围
feature_ranges = {
    "Income Variability": (0, 1000),
    "Annual Income": (0, 500000),
    "Total Savings": (0, 200000),
    "Loan Defaults": (0, 10),
    "Existing Loans": (0, 10),
    "Daily Income * Risk Tolerance": (0, 1000),
    "Annual Income * Family Support": (0, 1000000),
}

# 输入框（基于范围）
st.header("Input Features")
income_variability = st.number_input(
    "Income Variability",
    value=feature_ranges["Income Variability"][0],
    min_value=feature_ranges["Income Variability"][0],
    max_value=feature_ranges["Income Variability"][1],
)

annual_income = st.number_input(
    "Annual Income",
    value=feature_ranges["Annual Income"][0],
    min_value=feature_ranges["Annual Income"][0],
    max_value=feature_ranges["Annual Income"][1],
)

total_savings = st.number_input(
    "Total Savings",
    value=feature_ranges["Total Savings"][0],
    min_value=feature_ranges["Total Savings"][0],
    max_value=feature_ranges["Total Savings"][1],
)

loan_defaults = st.number_input(
    "Loan Defaults",
    value=feature_ranges["Loan Defaults"][0],
    min_value=feature_ranges["Loan Defaults"][0],
    max_value=feature_ranges["Loan Defaults"][1],
)

existing_loans = st.number_input(
    "Existing Loans",
    value=feature_ranges["Existing Loans"][0],
    min_value=feature_ranges["Existing Loans"][0],
    max_value=feature_ranges["Existing Loans"][1],
)

daily_income_risk_tolerance = st.number_input(
    "Daily Income * Risk Tolerance",
    value=feature_ranges["Daily Income * Risk Tolerance"][0],
    min_value=feature_ranges["Daily Income * Risk Tolerance"][0],
    max_value=feature_ranges["Daily Income * Risk Tolerance"][1],
)

annual_income_family_support = st.number_input(
    "Annual Income * Family Support",
    value=feature_ranges["Annual Income * Family Support"][0],
    min_value=feature_ranges["Annual Income * Family Support"][0],
    max_value=feature_ranges["Annual Income * Family Support"][1],
)

# 预测按钮
if st.button("Predict"):
    try:
        # 构建输入数据
        input_data = [[
            income_variability,
            annual_income,
            total_savings,
            loan_defaults,
            existing_loans,
            daily_income_risk_tolerance,
            annual_income_family_support
        ]]
        # 执行预测
        prediction = model.predict(input_data)
        st.success(f"Predicted Credit Score: {prediction[0]}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
