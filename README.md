Вариант №24<br/>
Задание №1<br/>
Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу<br/>
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.<br/>
Эмулятор должен запускаться из реальной командной строки, а файл с<br/>
виртуальной файловой системой не нужно распаковывать у пользователя.<br/>
Эмулятор принимает образ виртуальной файловой системы в виде файла формата<br/>
zip. Эмулятор должен работать в режиме GUI.
***
Конфигурационный файл имеет формат ini и содержит:<br/>
• Имя компьютера для показа в приглашении к вводу.
• Путь к архиву виртуальной файловой системы.
• Путь к лог-файлу.
Лог-файл имеет формат xml и содержит все действия во время последнего<br/>
сеанса работы с эмулятором. Для каждого действия указаны дата и время.<br/>
Необходимо поддержать в эмуляторе команды ls, cd и exit, а также<br/>
следующие команды:<br/>
1. chown.<br/>
2. cat.<br/>
3. date.<br/>
Все функции эмулятора должны быть покрыты тестами, а для каждой из<br/>
поддерживаемых команд необходимо написать 3 теста.
***
Описание функций<br/>
1. read_config(config_path)<br/>
Назначение:<br/>
Читает конфигурационный файл для извлечения имени хоста, пути к виртуальной файловой системе и пути к журналу.<br/>

Параметры:  <br/>
config_path (str): Путь к конфигурационному файлу (например, config.ini).<br/>

Возвращает: <br/>
Кортеж, содержащий имя хоста, путь к VFS и путь к журналу.<br/>

3. log_action(log_path, action)<br/>
Назначение: Логирует действие в XML-файл.<br/>
Параметры:  log_path (str): Путь к XML-файлу журнала.<br/>
action (str): Описание действия, которое нужно залогировать.<br/>
Возвращает: None.<br/>

4. VirtualFileSystem<br/>
Класс для работы с виртуальной файловой системой.<br/>
Методы:
* __init__(self, zip_path):<br/>
Назначение: Инициализирует VFS, извлекая содержимое ZIP-файла.<br/>
Параметры:  zip_path (str): Путь к ZIP-файлу.<br/>

* extract_zip(self, zip_path):<br/>
Назначение: Извлекает файлы из ZIP-архива в корневую директорию VFS.<br/>
Параметры: zip_path (str): Путь к ZIP-файлу.<br/>
Возвращает: None.<br/>

* list_directory(self):<br/>
Назначение: Возвращает список содержимого текущей директории с информацией о типе (файл или директория), размере и времени последнего изменения.<br/>
Возвращает: Строку с перечислением элементов директории.<br/>

* change_directory(self, path):<br/>
Назначение: Меняет текущую директорию.<br/>
Параметры:path (str): Новый путь к директории.<br/>
Возвращает: None.<br/>

* get_relative_path(self):<br/>
Назначение: Возвращает относительный путь к текущей директории.<br/>
Возвращает: Строку с относительным путем.<br/>

* read_file(self, file_name):<br/>
Назначение: Читает содержимое файла.<br/>
Параметры:  file_name (str): Имя файла для чтения.<br/>
Возвращает: Содержимое файла или сообщение об ошибке, если файл не найден.<br/>

4. Основные команды

* ls(vfs):
Назначение: Возвращает список файлов и директорий в текущей директории.
Параметры:  vfs (VirtualFileSystem): Объект виртуальной файловой системы.
Возвращает: Строку с содержимым директории.

* cd(vfs, path):
Назначение: Изменяет текущую директорию.
Параметры:  vfs (VirtualFileSystem): Объект виртуальной файловой системы.
            path (str): Путь к новой директории.
Возвращает: Сообщение об успешном изменении директории или ошибку.

* cat(vfs, file_name):
Назначение: Читает содержимое файла.
Параметры:  vfs (VirtualFileSystem): Объект виртуальной файловой системы.
            file_name (str): Имя файла для чтения.
Возвращает: Содержимое файла или сообщение об ошибке, если файл не найден.

* date():
Назначение: Возвращает текущую дату и время.
Возвращает: Строку с текущими датой и временем.

* chown(vfs, file_name, new_owner):
Назначение: Изменяет владельца файла (только имитация, реальная реализация не выполнена).
Параметры:  vfs (VirtualFileSystem): Объект виртуальной файловой системы.
            file_name (str): Имя файла.
            new_owner (str): Новый владелец.
Возвращает: Сообщение об успешном изменении владельца или ошибку.

5. run_shell(hostname, vfs_path, log_path)
Назначение: Запускает основной цикл работы эмулятора оболочки с GUI на tkinter.
Параметры:  hostname (str): Имя хоста.
            vfs_path (str): Путь к виртуальной файловой системе.
            log_path (str): Путь к журналу.
Возвращает: None
***
НАСТРОЙКИ
config.ini
Файл конфигурации должен содержать следующие параметры в секции [DEFAULT]:
[DEFAULT]
    hostname = MyVirtualMachine
    vfs_path = путь_к_zip_файлу
    log_path = путь_к_xml_журналу
hostname: Имя вашего хоста (например, MyVirtualMachine).
vfs_path: Путь к ZIP-файлу, содержащему вашу виртуальную файловую систему.
log_path: Путь к XML-файлу для записи журнала действий.
***
КОМАНДЫ ДЛЯ СБОРКИ ПРОЕКТА
Скрипт использует стандартные библиотеки, поэтому дополнительных зависимостей не требуется.
ZIP-файл, содержащий нужные файлы и директории для виртуальной файловой системы.
Файл config.ini с необходимыми параметрами.
***
ПРИМЕРЫ
![image](https://github.com/user-attachments/assets/110e0053-04b5-49de-83db-0d68c58632f2)
***
РЕЗУЛЬТАТЫ ПРОГОНА ТЕСТОВ
C:\Users\Andre\PycharmProjects\dz_config_Podshivalov_A_M\.venv\bin\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2023.3/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py" --path C:\Users\Andre\PycharmProjects\dz_config_Podshivalov_A_M\TestVirtualFileSystem.py 
Testing started at 21:36 ...
Launching unittests with arguments python -m unittest C:\Users\Andre\PycharmProjects\dz_config_Podshivalov_A_M\TestVirtualFileSystem.py in C:\Users\Andre\PycharmProjects\dz_config_Podshivalov_A_M

Ran 10 tests in 0.095s
OK
Process finished with exit code 0
![image](https://github.com/user-attachments/assets/61f04c77-e20f-422b-a810-d5668ea975c7)

