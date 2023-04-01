import json
import subprocess


with open('skillbox_json_messages.log', 'r') as file:
    logs = file.readlines()
logs = [json.loads(log) for log in logs]


def get_count_messages(logs):
    levels_count = {
        'DEBUG': 0,
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0,
        'CRITICAL': 0
    }
    for line in logs:
        levels_count[line['level']] += 1
    for level, count in levels_count.items():
        print(f"{level}: {count}")


def get_hour_max_count_logs(logs):
    hour_count = dict()
    for line in logs:
        hour = line['time'].split(':')[0]
        if hour in hour_count:
            hour_count[hour] += 1
        else:
            hour_count[hour] = 1
    max_count = max(hour_count, key=hour_count.get)
    return max_count


def get_count_logs_in_period():
    command = ['grep', '-c', '05:[0-1][0-9]:[0-5][0-9].*level.*CRITICAL', 'skillbox_json_messages.log']
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()


def get_count_messages_with_dog():
    command = ['grep', '-c', 'dog', 'skillbox_json_messages.log']
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()


def get_most_frequently_word_in_warning(logs):
    word_freq = dict()
    for line in logs:
        if line['level'] == 'WARNING':
            message = line['message']
            words = message.split()
            for word in words:
                if word in words:
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1
    most_freq_word = max(word_freq, key=word_freq.get)
    return most_freq_word


if __name__ == '__main__':
    print('Сколько было сообщений каждого уровня за сутки')
    get_count_messages(logs)

    print(f'\nБольше всего логов было в {get_hour_max_count_logs(logs)} часов')

    print(f'\n{get_count_logs_in_period()} логов уровня CRITICAL было в период с 05:00:00 по 05:20:00')

    print(f'\n{get_count_messages_with_dog()} сообщений содержат слово dog')

    print(f'\nСлово {get_most_frequently_word_in_warning(logs)} чаще всего встречалось в сообщениях уровня WARNING')
