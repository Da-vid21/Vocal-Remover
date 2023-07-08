# sudo systemctl restart nginx
#source venv/bin/activate
gunicorn app:app -t 600 --access-logfile ../access.log --error-logfile ../error.log