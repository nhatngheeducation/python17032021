# Library
pip install fastapi
pip install uvicorn[standard]
pip install flake8  # Verify Code style
pip install python-multipart

# Export to requirement.txt
pip freeze > requirements.txt

# Restore from requirement.txt
pip install -r requirements.txt
