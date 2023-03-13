## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Docker

### Lancement de l'application en local via l'image Docker
- Télécharger et installer [Docker](https://docs.docker.com/get-docker/)
- Rejoindre le repository Docker : https://hub.docker.com/r/antoinemx/lettings-python/tags
- Choisissez le tag le plus récent
- Utiliser la commande `docker run --rm -p 8000:8000 antoinemx/lettings-python:<tag>`

Vous pouvez accéder à l'application dans votre navigateur via l'url http://localhost:8000

## Déploiement

### Prérequis
Afin de déployer l'application via le pipeleine CircleCI et Heroku, vous devez créer des comptes pour tous les outils suivants:

- [GitHub](https://github.com/)
- [CircleCI](https://circleci.com) (via le compte GitHub)
- [Docker](https://www.docker.com)
- [Heroku](https://www.heroku.com)

### Configuration

#### CircleCI

Initialiser un projet sur CircleCI via *"Set Up Project"*. 
Sélectionner la branche *master* comme source pour le fichier *.circleci/config.yml*.

Pour faire fonctionner le pipeline CircleCI, il est nécessaire de préciser des variables d'environnement (*Project Settings* > *Environment Variables*) :

| Variable CircleCI | Description                                                                                                                                                                                                               |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CIRCLE_PROJECT    | Nom du projet CircleCI                                                                                                                                                                                                    |
| DOCKER_TOKEN      | Mot de passe Docker                                                                                                                                                			    |
| DOCKER_USER       | Nom d'utilisateur Docker                                                                                                                                                                                  |
| HEROKU_API_KEY    | Clé API de l'application créée via Heroku                                                                                                                                                |
| HEROKU_APP_NAME   | Nom de l'application Heroku : l'application déployée sera accessible via `https://<HEROKU_APP_NAME>.herokuapp.com/`                                                                                                       |

#### Docker

Créer un repository sur DockerHub. Le nom du repository doit correspondre à la variable *CIRCLE_PROJECT* créée pour CircleCI

#### Heroku

Pour créer une application avec votre compte Heroku:

Créer manuellement l'application sur le site. Le nom de l'application doit correspondre à la variable *HEROKU_APP_NAME* créée pour CircleCI
