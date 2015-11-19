# gym-server

## POSTGRESQL SETUP

createdb gym
createuser -P gymuser
[.. enter password in settings.py ..]

GRANT ALL PRIVILEGES ON DATABASE gym TO gymuser;



## DJANGO MIGRATIONS

NON USARE `migrate` ma:

```
python manage.py migrate_schemas --shared
```


## django dev server

per sviluppo in locale usare hexxie.com come dominio (... punta a localhost ma permette di usare sottodomini ...)

```
python manage.py runserver hexxie.com:8000
```

