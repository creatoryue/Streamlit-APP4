import streamlit as st
import numpy as np
import os
from src.loadModel import CNN

classes = ['COPD-Mild', 'COPD-Severe', 'Interstitial Lung Disease', 'Normal']
