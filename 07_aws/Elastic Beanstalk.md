## Elastic Beanstalk

> 반드시 django 2.1.1 로 진행



```bash
$ git checkout -b feature/deploy
```



```bash
$ mkdir .ebextensions
```

```bash
$ touch .ebextensions/django.config
```

```yaml
# django.config

option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: 프로젝트이름/wsgi.py
```



```bash
$ touch .ebextensions/db-migrate.config
```

```yaml
container_commands:
  01_migrate:
    command: "python manage.py migrate"
    leader_only: true
  02_chown_sqlitedb:
    command: "sudo chown wsgi db.sqlite3"
    leader_only: true
  03_seed: # Seeding 할 데이터가 있을 경우에만 추가
    command: "python manage.py loaddata seed.json"
    leader_only: true
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: 프로젝트이름.settings # settings 분리했을 경우 - 프로젝트이름.settings.production
```

- 주석은 실제로 작성하면 안된다.



```bash
$ touch .ebextensions/pip-upgrade.config
```

```yaml
commands:
  pip_upgrade:
    command: "sudo /opt/python/run/venv/bin/pip install --upgrade pip"
```



---



```python
# settings.py or base.py

STATIC_URL = '/static/'
STATIC_ROOT = 'static' # 추가
```



```yaml
# .ebextensions/db-migrate.config

container_commands:
  01_migrate:
    command: "python manage.py migrate"
    leader_only: true
  02_chown_sqlitedb:
    command: "sudo chown wsgi db.sqlite3"
    leader_only: true
  03_seed:
    command: "python manage.py loaddata seed.json"
    leader_only: true
	04_collectstatic: # 추가
    command: "python manage.py collectstatic"
		leader_only: true
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: 프로젝트이름.settings # settings 분리했을 경우 - 프로젝트이름.settings.production
```



```bash
# 관리자 계정 생성

$ python manage.py createsuperuser
사용자 이름: admin
이메일 주소: 
Password: 
Password (again): 
Superuser created successfully.
```



```bash
$ python manage.py dumpdata 어플리케이션(app).모델 --indent 4 > users.json # ex) accounts.User
```



```yaml
# .ebextensions/db-migrate.config

container_commands:
  01_migrate:
    command: "python manage.py migrate"
    leader_only: true
  02_chown_sqlitedb:
    command: "sudo chown wsgi db.sqlite3"
    leader_only: true
  03_seed:
    command: "python manage.py loaddata seed.json"
    leader_only: true
  04_collectstatic:
    command: "python manage.py collectstatic"
    leader_only: true
  05_superuser:
    command: "python manage.py loaddata users.json"
    leader_only: true
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: 프로젝트이름.settings
```



---



```bash
$ git add .
$ git commit -m "..."
```



```bash
$ pip install awsebcli
$ eb --version
EB CLI 3.16.0 (Python 3.7.3)
```



```bash
$ eb init
```

