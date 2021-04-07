# InfoTech
### Утилита для закачки и скачки файлов в любом формате - dropbox
#### Запуск:
1. `pip install -r requirements.txt`
2. Запускаем скрипт

#### Используются команды PUT и GET для загрузки/скачивания файлов

Пример: ` put C:\Users\User\Desktop\dropbox.txt  /test_folder/dropbox.txt  <token>` - данная команда загрузит файл.

Пример: ` get /test_folder/dropbox.txt C:\Users\User\Desktop\dropbox.txt <token>`   - данная команда скачает файл.


##### Утилита умеет работать с некорректными данными: отрабатывать в случае ввода пути несуществующего файла и т.д.

##### В случае ошибки запроса - выводит тело ошибки.