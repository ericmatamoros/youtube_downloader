#!/bin/bash

# Activate the conda environment
source /Users/ericmatamoros/miniconda3/etc/profile.d/conda.sh
conda activate llm_nvs

# Run the Streamlit app
cd youtube_download/scripts/
streamlit run app_streamlit.py
