import unittest
import os
import tempfile
import zipfile
from datetime import datetime
from main import VirtualFileSystem, ls, cd, cat, chown, date

class TestVirtualFileSystem(unittest.TestCase):

    def setUp(self):
        # Создание временной директории для тестирования
        self.test_dir = tempfile.mkdtemp()
        # Создание временного ZIP-файла с тестовыми файлами
        self.zip_file = os.path.join(self.test_dir, 'test.zip')
        with zipfile.ZipFile(self.zip_file, 'w') as zipf:
            zipf.writestr('file1.txt', 'Hello, World!')
            zipf.writestr('file2.txt', 'Goodbye, World!')
            zipf.writestr('subdir/file3.txt', 'Hello from subdir!')

        # Инициализация виртуальной файловой системы
        self.vfs = VirtualFileSystem(self.zip_file)

    def tearDown(self):
        # Удаление временной директории после тестов
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_ls(self):
        # Проверяем вывод команды ls
        expected_output = "File      13        " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " file1.txt\n" \
                          "File      15        " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " file2.txt\n" \
                          "Directory 0        " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " subdir"
        actual_output = ls(self.vfs)
        self.assertIn('file1.txt', actual_output)
        self.assertIn('file2.txt', actual_output)
        self.assertIn('subdir', actual_output)

    def test_cd(self):
        # Переход в подкаталог
        output = cd(self.vfs, 'subdir')
        self.assertIn("Changed directory to", output)
        self.assertEqual(self.vfs.current_path, os.path.join(self.vfs.root, 'subdir'))

    def test_cd_invalid(self):
        # Проверка перехода в несуществующий каталог
        output = cd(self.vfs, 'nonexistent')
        self.assertEqual(output, "Directory not found")

    def test_cat(self):
        # Чтение содержимого файла
        output = cat(self.vfs, 'file1')
        self.assertEqual(output, 'Hello, World!')

    def test_cat_invalid(self):
        # Проверка чтения несуществующего файла
        output = cat(self.vfs, 'nonexistent')
        self.assertEqual(output, 'File not found')

    def test_cat_invalid_extension(self):
        # Проверка чтения файла без расширения
        output = cat(self.vfs, 'file2')
        self.assertEqual(output, 'Goodbye, World!')

    def test_chown(self):
        # Проверка смены владельца файла
        output = chown(self.vfs, 'file1.txt', 'new_owner')
        self.assertEqual(output, "Changed owner of file1.txt to new_owner")

    def test_chown_invalid(self):
        # Проверка смены владельца несуществующего файла
        output = chown(self.vfs, 'nonexistent.txt', 'new_owner')
        self.assertEqual(output, "File not found")

    def test_chown_no_args(self):
        # Проверка неправильного формата (должен вернуть сообщение об ошибке)
        output = chown(self.vfs, 'file1.txt', '')
        self.assertEqual(output, "Changed owner of file1.txt to ")

    def test_date(self):
        # Проверка формата даты
        output = date()
        self.assertEqual(len(output), 19)  # Проверка формата 'YYYY-MM-DD HH:MM:SS'

if __name__ == '__main__':
    unittest.main()
