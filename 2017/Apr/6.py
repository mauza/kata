query = '''
SELECT
    *
FROM(
SELECT
    u."id",
    sum(e.total) as total
FROM
    users u
    INNER JOIN expenses e on e.userid = u."id"
WHERE
    u.created > '2016-1-1' AND
    u.created < '2016-12-31'
GROUP BY
    u."id"
) O
WHERE
    O.total > 20 AND
    O.total < 10000000
'''
