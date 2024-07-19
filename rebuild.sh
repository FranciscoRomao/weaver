deactivate
rm -r .venv .pdm-python pdm.lock
python3 -m venv .venv
source .venv/bin/activate
pip install pdm
pdm install