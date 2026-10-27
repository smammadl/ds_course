import streamlit as st
from pathlib import Path

MAIN_DIR = Path(__file__).parent
ADAMLAR_FAYLI = MAIN_DIR / 'adamlar.txt'

st.title('Kanalima xosh geldiniz')

st.text('Amsterdamdan haminiza salamlar')

ad = st.text_input('adinizi yazin')
yash = st.number_input(
    'yashinizi yazin', 
    min_value=0, 
    max_value=100,
)
sheher = st.selectbox("doguldugunuz sheher?", 
    ['Baki', 'Sumqayit', 'Gəncə']
)

def adami_save_et(*args):
    adamin_melumatlari = "-".join(args)
    with open(ADAMLAR_FAYLI, mode='a') as f:
        f.writelines(f"{adamin_melumatlari}\n")

if st.button('Yadda Saxla'):
    adami_save_et(ad, str(yash), sheher)
