## GitHub Plagarism Detector
  [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fssp4all%2FGitHub-Plagiarism-Detector&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

This is an automation tool for detecting plagarism in the code assignments. 

Note: This project uses MOSS software by Standford Univerity
### Demo 
![demo](./media/GPD.gif)

![demo](./media/GPD2.gif)

![Stats](./media/stats.png)
### Tech Stack 
- Flask
- React 
- Postgresql


### Execution
- cd to root dir ie. GPD
- `npm run start`

- cd to GPD/server
- `flask run`

- Start postgresql server using `pg_ctl -D /usr/local/var/postgres start`

### Installation 

<b> > Back End </b>

`pip install Flask`

`cd server`

`pip install -r requirements.txt`

Create a .env file in the server directory and add the following:
```
DB_SERVER = localhost:5432
DB_USER = username
DB_PASSWORD = admin
DB_NAME = gpd_dev
MOSS_USER_ID = moss_id
SENDER_EMAIL = email
RECEIVER_EMAIL = email
APP_PASSWORD = email_password 
MAXIMUM_JUMP_PERCENTAGE = 50 
```
Make the necessary changes based on your system configurations.

Create directories `app/files` in the project directory.

<b> > Front End </b>

Install Npm, React 

<b> > Postgres</b> 

For Mac, postgresql DB installation

Get homebrew

`brew update then brew  doctor `

`brew install postgresql`

start server using `pg_ctl -D /usr/local/var/postgres start`

Enter  `psql postgres` to get started

Some handy command for Postgres

- `CREATE DATABASE gpd_dev;`
- Dump .pgsql into DB `psql gpd_dev < /Users/spawar2/Desktop/GitHub-Plagiarism-Detector/server/db.pgsql`


Useful commands in psql command line 
- to use DB `\c gpd_dev `
- To list all DBS `\list`
- To list all Tables use  `\dt`
- To Empty table  `truncate [table_name] cascade; #if foreign keys are there`
