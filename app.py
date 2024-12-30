import streamlit as st
import pickle
import pandas as pd

# 加载模型
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# 应用标题
st.title("灵活就业者信用风险预测 (Gig Worker Credit Risk Prediction)")

# 简介
st.write("""
    通过输入用户特征，预测信用风险评分。适用于灵活就业者的信用风险评估。
""")

# 用户输入
st.header("输入用户信息 (Enter User Information)")

# 输入基础特征
income_volatility = st.slider("收入波动 (Income Variability, 1-10)", min_value=1, max_value=10)
annual_income = st.number_input("年收入 (Annual Income)", min_value=0.0, step=0.1)
total_savings = st.number_input("总储蓄 (Total Savings)", min_value=0.0, step=0.1)
loan_defaults = st.slider("贷款违约次数 (Loan Defaults)", min_value=0, max_value=10, step=1)
existing_loans = st.slider("存量贷款数 (Existing Loans)", min_value=0, max_value=10, step=1)
daily_income = st.number_input("日收入 (Daily Income)", min_value=0.0, step=0.1)
risk_tolerance = st.slider("风险容忍度 (Risk Tolerance, 1-10)", min_value=1, max_value=10)
family_support = st.slider("家庭支持水平 (Family Support, 1-10)", min_value=1, max_value=10)

# 派生特征
daily_income_risk_tolerance = daily_income * risk_tolerance
annual_income_family_support = annual_income * family_support

# 生成数据
input_data = pd.DataFrame({
    'Income Variability': [income_volatility],
    'Annual Income': [annual_income],
    'Total Savings': [total_savings],
    'Loan Defaults': [loan_defaults],
    'Existing Loans': [existing_loans],
    'Daily Income * Risk Tolerance': [daily_income_risk_tolerance],
    'Annual Income * Family Support': [annual_income_family_support]
})

# 显示输入数据
st.subheader("输入数据 (Input Data)")
st.write(input_data)

# 预测按钮
if st.button("预测信用风险评分 (Predict Credit Risk Score)"):
    # 确保输入数据与模型特征一致
    try:
        prediction = model.predict(input_data)
        st.subheader("预测结果 (Prediction)")
        st.write(f"信用风险评分预测值 (Predicted Credit Risk Score): {prediction[0]}")
    except Exception as e:
        st.error(f"预测失败，请检查输入数据或模型兼容性！\n错误信息: {e}")
