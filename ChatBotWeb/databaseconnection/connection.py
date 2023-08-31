import psycopg2
import pandas as pd

# Connect to the database
db_params = {
    'dbname': 'challenge',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}

connection = psycopg2.connect(**db_params)

cursor = connection.cursor()

cursor.execute('''SELECT v.modelo, VD.VEICULO_VENDIDO AS VENDAS
    FROM veiculos v
    JOIN vendas vd ON v.id_veiculo = vd.veiculos_id_veiculo
	ORDER BY 2 DESC''')

result = cursor.fetchall()

column_names = [desc[0] for desc in cursor.description]

df = pd.DataFrame(result, columns=column_names, index=None)

cursor.close()
connection.close()

print(df)