import requests


def put(token, pth, dest):
    # UPLOAD FILE
    header = {
        "Authorization": f"Bearer {token}",
        "Dropbox-API-Arg": f'{{"path": "{dest}", "mode": "add", "autorename": true, "mute": false, "strict_conflict": false}}',
        "Content-Type": "application/octet-stream"
    }

    data = open(fr'{pth}', 'rb')

    response = requests.post('https://content.dropboxapi.com/2/files/upload', headers=header, data=data)

    if response.status_code == 200:
        print(f'Файл успешно загружен в dropbox в папку {dest}')
    else:
        print(f'Ошибка {response.content}')


def get(token, pth, dest):
    # DOWNLOAD FILE
    header = {
        "Authorization": F"Bearer {token}",
        "Dropbox-API-Arg": f'{{ "path": "{pth}" }}',
    }

    response = requests.post('https://content.dropboxapi.com/2/files/download', headers=header)

    if response.status_code == 200:
        content = response.content
        with open(f'{dest}', 'wb+') as f:
            f.write(content)
        print(f'Файл успешно скачан на ваш компьютер в папку {dest}')
    else:
        print(f'Ошибка {response.content}')


if __name__ == '__main__':
    print('Добро пожаловать в dropbox loader')
    print('Используется команды PUT и GET для загрузки/скачивания файлов')
    print('Пример: put C:\\Users\\User\\Desktop\\dropbox.txt  /test_folder/dropbox.txt  <token>\
     данная команда загрузит файл')
    print(
        'Пример: get /test_folder/dropbox.txt C:\\Users\\User\\Desktop\\dropbox.txt <token>\
        данная команда скачает файл файл')

    command = input('Введите команду: ')
    command_list = command.split()
    try:
        if command_list[0] == 'put':
            put(command_list[3], command_list[1], command_list[2])
        elif command_list[0] == 'get':
            get(command_list[3], command_list[1], command_list[2])
        else:
            print('Ошибка ввода')
    except FileNotFoundError:
        print('Файл не найден.')
