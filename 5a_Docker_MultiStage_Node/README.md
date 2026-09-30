# 5a - Docker Multi-Stage Node.js Optimization

Build baseline:
docker build -f Dockerfile.large -t app-large:latest .

Build optimized:
docker build -f Dockerfile.optimized -t app-optimized:latest .

Compare:
docker images app-large app-optimized

Run:
docker run -d --name node-large -p 3001:3000 app-large:latest
docker run -d --name node-optimized -p 3002:3000 app-optimized:latest

Test:
curl http://localhost:3001/health
curl http://localhost:3002/health
