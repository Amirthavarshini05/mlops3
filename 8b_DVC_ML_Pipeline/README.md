# 8b - DVC 3-stage Pipeline

Install:
pip install -r requirements.txt
git init
dvc init

Track data:
dvc add data/books.csv
git add .
git commit -m "Dataset version 1"

Run:
dvc repro
type metrics.txt

Create version 2 by adding rows to data/books.csv:
dvc add data/books.csv
dvc repro
dvc metrics diff
git add .
git commit -m "Dataset version 2"

Exact metric values depend on the data and environment.
