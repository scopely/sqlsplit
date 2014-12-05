# sqlsplit

SQL-splitting server! Uses [sqlparse](https://github.com/andialbrecht/sqlparse)
under the hood.

## Usage

```
$ pip install sqlsplit
$ PROD=1 python sqlsplit
```

Then, say ya gots a sql file like dis:

```sql
CREATE TABLE foo (n integer);

INSERT INTO foo VALUES (1), (2), (3);

SELECT * FROM foo
WHERE n > 1;
```

Call it `myawesomesql.sql`. Now, using
[httpie](https://github.com/jakubroztocil/httpie), we can test it out:

```
$ http -f POST http://localhost:5000/split sql=@example.sql
```
