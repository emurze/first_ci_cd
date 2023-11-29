
# Django Template

## How run project?

Run dev server

```
docker compose up --build
```

Run prod server

```
docker compose -f docker-compose.prod.yml up --build
```

## How run tests?

Coverage
```
docker exec -it todo bash -c "cd src && poetry run coverage run --rcfile ../setup.cfg --data-file logs/.coverage manage.py test && poetry run coverage report --rcfile ../setup.cfg --data-file logs/.coverage"
```

Unittests
```
docker exec -it todo bash -c "cd src && poetry run python3 manage.py test apps"
```

End-To-End
```
docker exec -it todo bash -c "poetry run python3 src/manage.py test tests"
```

Utils Unittests
```
docker exec -it todo poetry run python3 -m unittest discover src/utils/
```

