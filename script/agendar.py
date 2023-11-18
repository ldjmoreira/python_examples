import pymysql  # Você pode usar o pacote do banco de dados correspondente ao seu banco (e.g., psycopg2 para PostgreSQL)

    # Função para obter os horários do banco de dados
def obter_horarios_do_banco():
    # Estabelecer conexão com o banco de dados
    conexao = pymysql.connect(host='seu_host', user='seu_usuario', password='sua_senha', database='sua_base_de_dados')

    try:
        with conexao.cursor() as cursor:
            # Executar o SELECT para obter os horários
            cursor.execute('SELECT horario FROM horarios')
            resultados = cursor.fetchall()  # Obter os resultados do SELECT
            horarios = [resultado[0] for resultado in resultados]  # Extrair os horários

    finally:
        conexao.close()

    return horarios

# Função para chamar a API nos horários definidos
def chamar_api(horarios):
    # Implemente a lógica para chamar a API nos horários desejados
    # Por exemplo, você pode usar a biblioteca requests para fazer as requisições à API

    for horario in horarios:
        print()
        # Lógica para chamar a API no horário especificado
        # Exemplo usando requests:
        # requests.get('sua_url_da_api')

if __name__ == '__main__':
    # Obter os horários do banco de dados
    horarios = obter_horarios_do_banco()

    # Chamar a API nos horários obtidos
    chamar_api(horarios)
