echo "Switching to main"
git checkout main

echo "Deploying to server..."
scp -i C:/Users/lee_h/Documents/General_Assembly/coding_projects/HaoFang.pem -r * ubuntu@13.229.106.234:/var/www/backend-server/
scp -i C:/Users/lee_h/Documents/General_Assembly/coding_projects/HaoFang.pem -r .env ubuntu@13.229.106.234:/var/www/backend-server/

echo "Done"