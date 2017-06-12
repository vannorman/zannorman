python manage.py makemigrations
python manage.py migrate
git pull
git add -A
git commit -m "$1"
ssh -i ~/.ssh/zannorman.pem ubuntu@ec2-52-53-162-113.us-west-1.compute.amazonaws.com
cd zannorman.com
git pull
python manage.py makemigrations
python manage.py migrate
sudo service apache2 restart
