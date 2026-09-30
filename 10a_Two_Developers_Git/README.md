# 10a - Two Developers Working on One Python Project

Scenario: Student Management System.

Developer 1:
git clone https://github.com/USERNAME/student-management.git
cd student-management
git add student.py
git commit -m "Add student management feature"
git push origin main

Developer 2:
git clone https://github.com/USERNAME/student-management.git
cd student-management
git pull origin main
modify student.py
git add student.py
git commit -m "Add student search feature"
git push origin main

If both developers edit the same lines, resolve conflict markers and then:
git add student.py
git commit -m "Resolve merge conflict"
git push origin main
