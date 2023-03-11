import sys


def get_mean_size(lines):
    files_size = 0
    count = 0
    for line in lines:
        count += 1
        files_size += int(line.split()[4])
    if count > 0:
        average_size = round((files_size / count), 2)
        return f'Средний размер файла в каталоге: {average_size} байт'
    else:
        return f'В каталоге нет файлов'


if __name__ == '__main__':
    lines = sys.stdin.readlines()[1:]
    print(get_mean_size(lines))
