import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Зүрхэн сарнай", page_icon="🌹")

st.title("🌹 Зүрхэн сарнай найз охиндоо 🌹")
st.write("Өнөөдрийн цэцэг бол чи минь юм шүү 💖")

# Зүрхэн хэлбэрийн координатууд
t = np.linspace(0, 2 * np.pi, 100)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Зураг зурах
fig, ax = plt.subplots(figsize=(8, 6))
for i in range(len(x)):
    ax.text(x[i], y[i], "🌹", fontsize=14, ha='center', va='center')

# Мессеж
ax.text(0, -20, "Өнөөдрийн цэцэг бол чи минь юм шүү 💖",
        fontsize=16, ha='center', color='darkred', fontweight='bold')

ax.axis('off')
ax.set_title("Зүрхэн хэлбэртэй сарнайгаар чамдаа хайр илгээе!", fontsize=16, color='crimson')

# Streamlit дээр харуулах
st.pyplot(fig)
