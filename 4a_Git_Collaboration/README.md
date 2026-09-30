# 4a - College Management Git Collaboration

Repository: college-management
Branches:
main
develop
feature/student
feature/faculty
feature/attendance

Commands:
git clone https://github.com/USERNAME/college-management.git
cd college-management
git switch develop
git pull origin develop
git switch -c feature/student
git status
git diff
git add student.py
git commit -m "Add student management feature"
git push -u origin feature/student

Then create a Pull Request:
feature/student -> develop
