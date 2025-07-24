#!/bin/bash
set -e

# 🚀 Nebula GitHub Push + Release Script

# Make sure you're in the nebula/ root directory
if [ ! -d ".git" ]; then
    echo "❌ Not a git repo. Run scaffold.sh first."
    exit 1
fi

# Check for required env variable
if [ -z "$GITHUB_PAT" ]; then
  echo "❌ Please set your GitHub PAT in the environment:"
  echo "export GITHUB_PAT=your_pat_here"
  exit 1
fi

# Git remote setup (adjust as needed)
REPO_URL="https://evaderbot:${GITHUB_PAT}@github.com/evader/umn.git"
git remote remove origin || true
git remote add origin "$REPO_URL"

# Push to GitHub
git push origin main
git push origin v1.0.0-rc1

echo "✅ Pushed to GitHub!"

# Create GitHub Release via API
echo "📦 Creating GitHub Release..."
curl -s -X POST https://api.github.com/repos/evader/umn/releases \
  -H "Authorization: token $GITHUB_PAT" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "tag_name": "v1.0.0-rc1",
  "target_commitish": "main",
  "name": "Nebula v1.0.0-rc1",
  "body": "$(cat RELEASE.md)",
  "draft": false,
  "prerelease": false
}
EOF

echo "🎉 GitHub Release created!"