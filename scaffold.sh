#!/bin/bash
set -e

echo "🌌 Nebula Git Scaffold Starting..."

# No cd into 'nebula' — you're already in the right folder
rm -rf .git

git init
git add .
git commit -m "🚀 Final release v1.0.0-rc1 - full product suite"
git tag v1.0.0-rc1

echo "✅ Git repo ready. Run github_push_and_release.sh next!"
