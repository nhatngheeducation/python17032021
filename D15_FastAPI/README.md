# Library
pip install fastapi

pip install uvicorn[standard]

pip install python-multipart

pip install mysql-connector-python

# Verify Code style
pip install flake8

# Export to requirement.txt
pip freeze > requirements.txt

# Restore from requirement.txt
pip install -r requirements.txt

# OCR Service

pip install tesseract

pip install pytesseract

pip install jinja2

pip install opencv-python

# Restore project

1. Create a virtual environment:
(Windows):
+ python -m venv <myenv>
+ cd myenv/Scripts
+ activate

(Linux)
+ venv <myenv>
+ source myenv/bin/activate

2. Install packages
pip install -r requirements.txt