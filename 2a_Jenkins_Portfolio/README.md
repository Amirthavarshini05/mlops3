# 2a - Local Portfolio Jenkins Freestyle Deployment

Question requirements:
1. Local Git repository
2. Jenkins Freestyle job named `Local-Portfolio-Deploy`
3. Configure Git/local repository as SCM
4. Copy index.html to the local HTTP server root
5. Modify, commit and manually build again

Windows deployment command:
copy /Y "%WORKSPACE%\index.html" "C:\inetpub\wwwroot\index.html"

For IIS, enable Internet Information Services and use:
http://localhost
