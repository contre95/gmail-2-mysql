# Gmail-2-MySQL 

The aim of this small project is to process Gmail inbox messages and search for specific keywords, then save these on a MySQL database.

For the moment this project works exclusively with Gmail. Nevertheless, providers could be easily added in the `mail.py` file.

## Configuring the Gmail API

### Create the Service Account
In order to be able to access Google Services, go to [Google Developers Console](https://console.developers.google.com/) and create a new project.
On the left menu, select ***Credentials*** , then ***Create credentials***. Select ***Service account key*** from the type of credentials list. After this, choose ***New service account***, **JSON** as a private key type and hit **Create** button which will trigger the download of the JSON private key.

### Enable the Gmail API 
Once you have created the Service Account, you will need to enable the API which will be used to get the emails. To do that, select Library from the left menu and then search for “*Google Gmail API*” and press the **Enable** button

### Grant the Service Account access to the API
The access is granted by assigning permissions to the service account, using its email address. 

### Prerequisites
  * Python 3
  * MySQL

## Database Configuration

### Create the database
```
MariaDB [(none)]> create database <dbname>;
```
## Setup the Database
To setup the database in order to run the migrations please alter the `alembic.ini` file and set the `sqlalchemy.url` with your db parameters
```
sqlalchemy.url = mysql://user:password@127.0.0.1/dbname
```
The same applies to the ORM. Edit the `database.py` file located on the root directory of the project.
```
engine = create_engine('mysql+mysqldb://user:password@localhost:3306/dbname')
```

### Run the migrations
For the migration, we are going to use `Alembic`, since it's known that Alembic installation varies among different operative systems I strongly recommend to run Alembic in a container. To so, `cd` into the `db_migrations` directory and run the following command.
```
$ docker container run --rm --network=host -v $(pwd):/srv contre95/alembic upgrade head
```

### Set up the environment
Clone the repo and `cd` to the folder. Then run the following commands:
```
$ virtualenv -p python3 venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

### Run command

```
(venv) $ chmod 775 ./gmail_2_mysql.py
(venv) $ ./gmail_2_mysql.py
```
The expected output would be something like 
```
(venv) ➜ meli-challenge git:(master) ✗ ./gmail_2_mysql.py 
Subject --> Has Keywords {'devops', 'DEVOPS', 'DevOps'}

Security Engineer and 39 more Senior Cloud DevOps Engineer jobs in Tempe, AZ, US for you! --> Yes
Re: Want to work at Enterprise? --> No
Google Security alert --> No
Lucas, please add me to your LinkedIn network --> Yes
The Kemtah Group wants you! --> Yes
Lucas: 30+ new jobs for 'site reliability engineer' in Dallas-Fort Worth Metroplex --> No
27 Jobs : DevOps Engineer - Remote - Jr./Mid Arizona, United States --> Yes
See more jobs like OpenText - Software Engineer --> No
Re: Entrevista - Mercado Libre --> No
```
## Built With
* [SQLAlchemy](https://www.sqlalchemy.org/) - The ORM used
* [Google Gmail API](https://developers.google.com/gmail/)


## Authors

* **Lucas Contreras**  | Github [@contre95](https://github.com/contre95)


