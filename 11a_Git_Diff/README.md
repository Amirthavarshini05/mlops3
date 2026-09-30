# 11a - git diff

Scenario:
Arun has cloned the repository and adds:

def calculate_average(marks):
    return sum(marks) / len(marks)

Before committing, use:
git diff

Complete demo:
git clone https://github.com/USERNAME/college-management.git
cd college-management
git status
# edit student.py
git diff
git add student.py
git commit -m "Add average calculation"
git push origin main
