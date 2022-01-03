# Event Management System using Python and MySQL

## Requirements (Advised)

- Python v3.8+
- MySQL Community Server v8+

## Working

#### #1 Python Environment Setup
```bash
$ git clone https://github.com/debarchito/Event-Management-System.git
$ cd Event-Management-System
$ conda create -n EventManagementSystem python=3.8
$ conda activate EventManagementSystem
$ pip install -r requirements.txt
```

#### #2 MySQL Setup
You will find a `database.sql` file in `./src/database`. You need to run this file in MySQL console. Here is how you can do it (considering you are already in Event-Management-System folder in terminal)
```bash
$ cd src/database
$ mysql -u <USER> -p
Enter password: ********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.27 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> source database.sql
```
#### #3 Configuration
You will find a `config.json.example` file in `./src/database`. Rename it to `config.json` and update the contents of the file accordingly:
```json
{
    "host": "localhost",
    "user": "<YOUR MYSQL USERNAME GOES HERE>",
    "password": "<YOUR MYSQL PASSWORD GOES HERE>",
    "database": "EventManagementSystem"
}

```

#### #4 Start
You are all ready. Run this (while being inside Event-Management-System folder):
```bash
conda activate EventManagementSystem
cd src
python main.py
```

#### Enjoy!

## LICENSE

This repository is licensed under the MIT License.
