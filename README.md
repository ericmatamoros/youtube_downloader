# youtube_downloader

This repository contains the required functions & classes for the project: youtube_downloader

## Set up virtual environment & install dependencies

Download the project file.

```
# Install specific environments
make venv
```

## Run the streamlit app

Simply type: ./run_app.sh

The code of the bash file is:
· Source the conda environment
· Load the 'llm_nvs' already created environment
· Go to the scripts folder
· Run the app_streamlit.py file.

```
#!/bin/bash

# Activate the conda environment
source /Users/ericmatamoros/miniconda3/etc/profile.d/conda.sh
conda activate llm_nvs

# Run the Streamlit app
cd youtube_download/scripts/
streamlit run app_streamlit.py
```

NOTE: Any other user leveraging this code must change the conda env name and the file directory.

## Contributors

- [Eric Matamoros](ericmatamoros1999@gmail.com)