sudo apt update -y && sudo apt upgrade -y
sudo apt install python3-venv -y

python -m venv .tempvenv

source .tempvenv/bin/activate && pip install rpi-lcd && deactivate

