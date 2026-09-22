## Python and FastAPI

### Install python3 and pip3

```sh
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
pip3 --version
python3 -m venv .venv
source .venv/bin/activate
```

### Run application using FastAPI & Uvicorn server

```sh
pip install fastapi "uvicorn[standard]"
# fastapi is the framework itself.
# uvicorn is the server that will actually run your application.

uvicorn main:app --reload
# --reload: makes the server restart automatically whenever you make changes to your code. (Only use this while developing!)

# Open your web browser and go to: http://127.0.0.1:8000/

# Now, go to this URL in your browser: http://127.0.0.1:8000/docs
```
