# 4b - GitFlow Branching

Required branches:
main
develop
feature/user-auth
release/1.0
hotfix/login-bug

Typical commands:
git switch main
git switch -c develop
git switch develop
git switch -c feature/user-auth
git add .
git commit -m "Add user authentication"
git push -u origin feature/user-auth
git switch develop
git merge feature/user-auth
git switch -c release/1.0
git switch main
git merge release/1.0
git tag -a v1.0 -m "Release version 1.0"
git push origin --all
git push origin v1.0

To demonstrate a conflict, make different changes to app.py on release/1.0 and develop,
merge and manually remove <<<<<<< ======= >>>>>>> markers.
