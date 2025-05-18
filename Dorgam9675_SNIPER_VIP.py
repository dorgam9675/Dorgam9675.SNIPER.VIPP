import streamlit as st
import yfinance as yf
import pandas as pd
import ta

st.set_page_config(page_title="Dorgam9675.SNIPER.VIP", layout="centered")

st.title("🔍 نظام Dorgam9675.SNIPER.VIP")
st.caption("مرحباً بك في النسخة التجريبية من النظام")

symbol = st.selectbox("اختر زوج العملات أو الذهب", ["XAUUSD=X", "EURUSD=X", "AAPL"])
interval = st.selectbox("الإطار الزمني", ["1h", "4h", "1d"])
period = st.selectbox("البيانات التاريخية", ["7d", "1mo", "3mo"])

if st.button("ابدأ التحليل"):
    try:
        df = yf.download(symbol, period=period, interval=interval)
        if df.empty:
            st.error("❌ لا توجد بيانات")
        else:
            df["RSI"] = ta.momentum.RSIIndicator(df["Close"]).rsi()
            df["EMA200"] = ta.trend.EMAIndicator(df["Close"], window=200).ema_indicator()

            st.success(f"✅ جاهز لتحليل {symbol} على الإطار {interval} بفترة {period}")
            st.line_chart(df[["Close", "EMA200"]])
            st.line_chart(df["RSI"])
    except Exception as e:
        st.error(f"حدث خطأ: {e}")