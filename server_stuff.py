import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6996
flag = True
client_name = None
server_ip = '0.0.0.0'
server.bind(('', port))


#или Server = socket.create_server(('server_ip', port))



server.listen(1) #Указание количества допустимых для обработки клиентских соединений. Выше лимита – отказ в обслуживании
print('Сервер начал работу')
client_socket, address = server.accept() #Сбор данных клиента и его разбор на имя сокета и адрес клиента
print(f'Клиент {address} подключился')

while flag:
	data = str(input())
	client_socket.send(data).encode('utf-8')
	decode_data = client_socket.recv(1024).decode('utf-8')
	if decode_data == 'client_flag = False':
		client_socket.close()
		break
	print(decode_data)

