import os.path


def get_summary_rss(path_to_file):
    with open(path_to_file, 'r') as file:
        lines = file.readlines()[1:]
        result = 0
        for line in lines:
            result += int(line.split()[5])
    result_kb = round(result / 1024, 3)
    result_mb = round(result_kb / 1024, 3)
    result_gb = round(result_mb / 1024, 3)
    print('Потребляемая память:')
    print(f'{result} байт \n{result_kb} килобайт \n{result_mb} мегабайт\n{result_gb} гигабайт')


path_to_file = os.path.abspath('output_file.txt')

if __name__ == '__main__':
    get_summary_rss(path_to_file)
