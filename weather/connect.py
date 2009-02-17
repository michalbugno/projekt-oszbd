import cx_Oracle

dsn = cx_Oracle.makedsn('149.156.204.197', '1521', 'orcl')

conn = cx_Oracle.connect('st_msq', 'misiolek', dsn)

cur = conn.cursor()
