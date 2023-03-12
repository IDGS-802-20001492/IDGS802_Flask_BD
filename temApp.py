from db import get_connection
try:
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute('call agregar_alumno(%s,%s,%s)',('Arturo','Alba','Alba@gmail.com'))

    connection.commit()
    connection.close()
    resultset = cursor.fetchall()
    for row in resultset:
        print(row)
except Exception as ex:
    print(ex)