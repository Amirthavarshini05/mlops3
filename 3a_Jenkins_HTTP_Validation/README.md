# 3a - Automated HTTP Validation Jenkins Pipeline

Prerequisite on Windows:
Enable IIS and make sure http://localhost works.

The pipeline:
Deploy -> Validate.

To demonstrate failure, stop IIS:
net stop W3SVC

Run Jenkins and observe failure. Then:
net start W3SVC

Run Jenkins again and observe SUCCESS.
