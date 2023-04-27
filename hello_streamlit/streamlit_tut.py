import streamlit as st;


st.write("Hello, *World* Welcome! :sunglasses: SAO")

"Great";
st.header("App Title")
st.header("This is header!");

st.markdown("Hello **World**! my markdown");

import streamlit as st

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

st.divider()

st.metric("My Metric",42,2);

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd;

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart

df = pd.DataFrame(
    np.random.randn(50,20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(df)
"Done Outputing!";
