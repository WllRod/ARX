from setuptools import setup

APP = ['ARX_Sistemas.py']
DATA_FILES  = ['assets.zip', 'config.json']
OPTIONS = { 'argv_emulation': True }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)