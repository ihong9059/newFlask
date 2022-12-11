. runProject.sh

gunicorn  --bind unix:/tmp/myproject.sock 'pybo:create_app()' &

sudo systemctl restart nginx &






