import mysql.connector
from gerador_codigo import gerar_codigo

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="seu_banco"
    )

def mostrar_tabela(cursor, titulo):
    print(f"\n📊 {titulo}")
    cursor.execute("SELECT * FROM alimentos")
    resultados = cursor.fetchall()

    if not resultados:
        print("Tabela vazia")
    else:
        for linha in resultados:
            print(linha)

def main():
    conn = conectar()
    cursor = conn.cursor()

    mostrar_tabela(cursor, "ANTES")

    codigo, sec = gerar_codigo("A", "B", "BR")
    print(f"\nNovo código gerado: {codigo} | Sec: {sec}")

    mostrar_tabela(cursor, "DEPOIS")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
