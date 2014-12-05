CREATE TABLE foo (n integer);

INSERT INTO foo VALUES (1), (2), (3);

SELECT * FROM foo
WHERE n > 1;
