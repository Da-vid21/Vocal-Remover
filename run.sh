# sudo systemctl restart nginx
gunicorn app:app -t 300 --access-logfile ../access.log --error-logfile ../error.log