import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
#element.send_keys(file_path)
print('1.os.path.abspath(__file__))=',os.path.abspath(__file__))	#путь до исполняемого файла
print('2.file_path =', file_path)	#путь до заданного файла
print('3???',os.path.abspath(os.path.dirname(__file__)))	#текущий каталог