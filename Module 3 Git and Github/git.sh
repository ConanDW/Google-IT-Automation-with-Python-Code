git config --global user.email "camday03@gmail.com"
git config --global user.name "Cameron Day"
ls -la #checks for dirs starting with . ex .git, .ssh
git add test.sh #stage the file
git status #check well status
git commit -m "commit message"
git log #show commits
git commit -a #use to skip stagging step
git log -p #paging
git show #show certain commites ex git show 6726e5e66d942cae339e301f831fc08e765877ed
git log --stat #gives stats 
git diff #same as diff -u
git add -p #show changes beeing added, and confs if you wanna change it. like -whatif in PowerShell
git diff --staged #show changes on staged files
git rm #rm 
echo .DS_STORE > .gitignore #add to git ignore
git checkout filename #use to revert before commit
git reset HEAD #to remove 

git add auto-update.py
git commit -m 'Add two new scripts'
git add gather-information.sh
git commit --amend #use admend to add to a comitt, using only in local

#BRANCHES BELOW

git branch #show branches
git branch new-feature # make a branch
git checkout new-feature
git checkout -b even-new # make a branch and switch to it
git branch -d #remove branch 
git log --graph --oneline # make logs more readable

git remote -v
git remote show origin
git fetch #sync data 

git pull #merges branches that are out of date locally to origin.

git rebase #fix three way merges