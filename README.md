# p4p-zivid-capture-helper

Helper script that allows to prompt user to do data capture using the zivid camera.

## Requirements

* [Zivid SDK](https://www.zivid.com/downloads) (v2.3.0) - Connect with Zivid camera.
* Zivid Camera - The camera used is Zivid One+ S.
* Python (v3.6+) - Interpreter to run script.
* Pip - Package manager for Python.
* Zivid Studio - GUI to open `.zdf` files for extracting required data.

Optional:
* [Python Virtual Environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) - Separate instance of Python installation.

## Setup

1.) Clone this repository.

2.) Open terminal in the project folder.

3.) OPTIONAL: If you installed the Virtual environment, you can setup the environment:
```bash
python3 -m venv venv --system-site-packages
source venv/bin/activate
```
Otherwise skip this step.

4.) Install required libraries.
```bash
pip install -r requirements.txt
```

5.) Connect the Zivid Camera and then run the script.
```bash
python3 main.py
```
