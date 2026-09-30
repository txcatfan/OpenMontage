# 1. Ensure you are on your main branch
git checkout main

# 2. Fetch the latest branches and commits from upstream
git fetch upstream

# 3. Merge the upstream changes into your local main branch
git merge upstream/main

# 4. Push the merged updates to your GitHub fork (origin)
git push origin main
