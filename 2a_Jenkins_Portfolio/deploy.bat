@echo off
echo Deploying portfolio...
copy /Y "%WORKSPACE%\index.html" "C:\inetpub\wwwroot\index.html"
echo Deployment completed.
