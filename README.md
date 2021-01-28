# multi-page-app

# Demo

[Demo of this web app](#).

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
