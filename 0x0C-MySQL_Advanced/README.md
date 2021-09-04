# 0x0C. MySQL advanced

## Resources

Read or watch:

- [MySQL cheatsheet](https://intranet.hbtn.io/rltoken/LPHf_IaJaKHjk5eFPXB0cA)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://intranet.hbtn.io/rltoken/lLnaxz0ESQy3EHwuMMfvfg)
- [Stored Procedure](https://intranet.hbtn.io/rltoken/Sk9qc1Mg-1iLY2CPwRO-GQ)
- [Triggers](https://intranet.hbtn.io/rltoken/rpwsBdE-D0BvNGb_xp4e9g)
- [Views](https://intranet.hbtn.io/rltoken/_QXmgLWifMI5xBYcoU30-g)
- [Functions and Operators](https://intranet.hbtn.io/rltoken/o8FuG6wEKU7Czfshemkxiw)
- [Trigger Syntax and Examples](https://intranet.hbtn.io/rltoken/_GHvsp9VBoFvcF8e3vR8FA)
- [CREATE TABLE Statement](https://intranet.hbtn.io/rltoken/BZ9CZqpTzEz7iN_hUfrLQQ)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://intranet.hbtn.io/rltoken/JD1BbREw66Vg1j8b_G4kkQ)
- [CREATE INDEX Statement](https://intranet.hbtn.io/rltoken/MoxDptxm38J3IviBm2IMEw)
- [CREATE VIEW Statement](https://intranet.hbtn.io/rltoken/uDiqx_4DI7ZZ8A11C4g5CA)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General 0

- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Requirements

### General 1

- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
– All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## More Info

Comments for your SQL file:

```sh
cat my_script.sql
```

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

Use “container-on-demand” to run MySQL
Ask for container Ubuntu 18.04 - Python 3.7
Connect via SSH
Or via the WebTerminal
In the container, you should start MySQL before playing with it:

```sh
service mysql start
 * MySQL Community Server 5.7.30 is started

cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password:
Database
information_schema
mysql
performance_schema
sys
$
```

In the container, credentials are root/root

How to import a SQL dump

```sh
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
