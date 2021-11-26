from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import os
import os.path as path
import datetime


def pb_show_clicked():
    text = ''
    form.textEdit_main.clear()
    for item in os.listdir():
        text += f'{item}\n'

    form.textEdit_main.insertPlainText(text)


def pb_properties_clicked():
    form.textEdit_main.clear()
    text = ''
    text += (f'Время последнего доступа: {datetime.datetime.fromtimestamp(path.getatime(os.getcwd()))}\n')
    text += (f'Время последнего изменения:  {datetime.datetime.fromtimestamp(path.getatime(os.getcwd()))}\n')
    text += (f'Время создания:  {datetime.datetime.fromtimestamp(path.getatime(os.getcwd()))}\n')
    form.textEdit_main.insertPlainText(text)


def pb_delete_file_clicked():
    try:
        os.remove(form.textEdit_path.toPlainText())
        form.textEdit_main.clear()
        form.textEdit_main.insertPlainText('Файл удален')
    except Exception as e:
        form.textEdit_main.clear()
        form.textEdit_main.insertPlainText(e.__str__())

def pb_read_file_clicked():
    try:
        os.system(f'notepad.exe {form.textEdit_path.toPlainText()}')
    except Exception as e:
        form.textEdit_main.clear()
        form.textEdit_main.insertPlainText(e.__str__())

def pb_new_file_clicked():
    file = open(form.textEdit_path.toPlainText(), 'w+')
    file.write('Hello world!')
    file.close()
    form.textEdit_main.clear()
    form.textEdit_main.insertPlainText('Файл успешно создан!')


def pb_new_dir_clicked():
    os.mkdir(form.textEdit_path.toPlainText())
    form.textEdit_main.clear()
    form.textEdit_main.insertPlainText('Каталог успешно создан!')

if __name__ == '__main__':
    Form, Window = uic.loadUiType("design.ui")
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()

    form.textEdit_main.insertPlainText('При нажатии на клавиши здесь будет выводиться информация')
    form.textEdit_path.insertPlainText(os.getcwd())
    form.pb_show.clicked.connect(pb_show_clicked)
    form.pb_properties.clicked.connect(pb_properties_clicked)
    form.pb_delete_file.clicked.connect(pb_delete_file_clicked)
    form.pb_read_file.clicked.connect(pb_read_file_clicked)
    form.pb_new_file.clicked.connect(pb_new_file_clicked)
    form.pb_new_dir.clicked.connect(pb_new_dir_clicked)

    app.exec_()
