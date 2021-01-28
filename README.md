# multi-page-app

# Watch the tutorial video
[How to Make a Multi-Page Web App | Streamlit #16](https://youtu.be/nSw96qUbK9o)

<a href="https://youtu.be/nSw96qUbK9o"><img src="http://img.youtube.com/vi/nSw96qUbK9o/0.jpg" alt="How to Make a Multi-Page Web App | Streamlit #16" title="How to Make a Multi-Page Web App | Streamlit #16" width="400" /></a>

# Demo

Launch the web app:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/multi-page-app/main/app.py)

# Reproducing this web app
To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *multipage*
```
conda create -n multipage python=3.7.9
```
Secondly, we will login to the *multipage* environement
```
conda activate multipage
```
### Install prerequisite libraries

Download requirements.txt file

```
wget https://raw.githubusercontent.com/dataprofessor/ml-auto-app/main/requirements.txt

```

Pip install libraries
```
pip install -r requirements.txt
```

### Download and unzip this repo

Download [this repo](https://github.com/dataprofessor/multi-page-app/archive/main.zip) and unzip as your working directory.

###  Launch the app

```
streamlit run app.py
```
