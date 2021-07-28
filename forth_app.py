import streamlit as st

import numpy as np
import os

classes = ['COPD-Mild', 'COPD-Severe', 'Interstitial Lung Disease', 'Normal']

load_state = st.text("loading...")