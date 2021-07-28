import streamlit as st
from src import loadModel, sound
import numpy as np
import os

classes = ['COPD-Mild', 'COPD-Severe', 'Interstitial Lung Disease', 'Normal']