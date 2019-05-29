from fabric import Connection

c = Connection('smart-stag')
with open('dbdump', 'wb') as f:
    result = c.run('pg_dump -h localhost -p 5432 -U taxbot taxbot_ml -w')
    result.handle_stdout(hide=True, output=f)
