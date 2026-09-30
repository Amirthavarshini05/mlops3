# 9a - Blue-Green Deployment with Nginx

This version uses Docker Compose:
- Blue: 8081
- Green: 8082
- Nginx: 80

Start:
docker compose up -d

Check:
curl http://localhost

Initially Nginx points to Blue.

Switch to Green:
1. Edit nginx/nginx.conf from `blue:80` to `green:80`.
2. Recreate/reload Nginx:
docker compose exec nginx nginx -t
docker compose exec nginx nginx -s reload

Then:
curl http://localhost

Expected before switch:
Version 1.0 (Blue)

Expected after switch:
Version 2.0 (Green)
