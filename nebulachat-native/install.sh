#!/bin/bash
echo "Installing NebulaChat..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py