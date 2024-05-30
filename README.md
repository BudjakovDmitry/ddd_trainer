# Domain Driven Design trainer

```shell
# Clone project
git clone git@github.com:BudjakovDmitry/ddd_trainer.git

# Up
docker-compose up --build -d

# Migrate
docker-compose exec app python manage.py migrate
 
# Stop
docker-compose down
```

Open in browser *http://127.0.0.1:8000/api/user/*
