import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

def create_server_socket():
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Позволяет повторно использовать адрес и порт
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Привязываем сокет к адресу и порту
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    # Слушаем входящие соединения (не более 1 одновременного соединения для простоты)
    server_socket.listen(1)
    return server_socket

def handle_client(client_socket):
    # Получаем фамилию от клиента
    request = client_socket.recv(1024).decode()
    message = request.strip().split('\n')[-1].strip()

    # Проверяем, принадлежит ли фамилия студенту вашей группы
    if message in groupmates.keys():
        response = f"Привет, {groupmates[message]}"
    else:
        response = "Такого пользователя нет в нашей группе!"

    # Отправляем ответ клиенту
    client_socket.sendall(str.encode(response))
    client_socket.close()

if __name__ == "__main__":
    # Информация о студентах вашей группы
    groupmates = {
        "Кувшинов": "Максим",
        "Коновалов": "Кирилл",
        "Шепталин": "Вадим"
    }

    # Создаем серверный сокет
    server_socket = create_server_socket()
    print(f"Сервер запущен на {SERVER_HOST}:{SERVER_PORT}")

    try:
        while True:
            # Ожидаем соединение
            print("Ожидание соединения...")
            client_connection, client_address = server_socket.accept()

            try:
                print(f"Подключен клиент {client_address}")
                # Обрабатываем запрос клиента
                handle_client(client_connection)
            except Exception as e:
                print(f"Ошибка при обработке клиента: {e}")
    except KeyboardInterrupt:
        print("Сервер завершил работу.")
    finally:
        # Закрываем серверный сокет при завершении
        server_socket.close()
