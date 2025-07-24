#!/bin/bash
echo "🚀 Installing NebulaChat..."

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt

echo "✅ Installation complete. Run with: python main.py"
