# Fund Alloc 3.0 (back)

## Preparing Environment

### **Python 3.9**

Link for download: [Python 3.9](https://www.python.org/downloads/release/python-399/)

Instructions: [PhoenixNAP](https://phoenixnap.com/kb/how-to-install-python-3-windows)

### **Pip**

Link for download: [get-pip.py](https://bootstrap.pypa.io/get-pip.py)

Instructions: [PhoenixNAP](https://phoenixnap.com/kb/install-pip-windows)

### **GitHub Repository**

Run command: `git clone https://github.com/VitorMartin/fund_alloc_back.git`

Link: [VitorMartin/fund_alloc_back](https://github.com/VitorMartin/fund_alloc_back)

### **Pip Dependencies**

Run command: `"path/to/python3.9/python.exe" -m pip install -r requirements.txt`

This project was created with [FastAPI](https://fastapi.tiangolo.com/) version 0.67.0.

## Deploying App

### **Local**

To configure what interfaces to use, edit the file [src/config.json](src/config.json). For now, the only setup that is
currently working 100% is the original setup (using Access and FastAPI)

The server uses **port 8080** by default. To specify a custom port (and change other settings), edit the
file [src/controllers/fastapi/config.json](src/controllers/fastapi/config.json).

Run command: `"path/to/python3.9/python.exe" -m src.main`

## API Documentation

For information on this service's endpoints, deploy it and visit its [Documentation](http://127.0.0.1:8080/docs)
