# Src

## Project setup

```
yarn install
```

### Compiles and hot-reloads for development

```
yarn serve
```

### Compiles and minifies for production

```
yarn build
```

### Lints and fixes files

```
yarn lint
```

### Create dataset as fixture

```
python backend/operations/generate_users.py
```

### Load data into database

In virtualenv, run:

```
python manage.py loaddata fixture.json
```
