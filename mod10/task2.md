1. Телефоны какого цвета чаще всего покупают? Ответ: Violet
```
cursor.execute('SELECT * FROM table_checkout ORDER BY sold_count DESC').fetchone()
```

2. Какие телефоны чаще покупают: красные или синие? Ответ: Red
```
cursor.execute('SELECT * FROM table_checkout WHERE phone_color IN ("Red","Blue") ORDER BY sold_count DESC').fetchall()
```

3. Какой самый непопулярный цвет телефона? Ответ: Goldenrod
```
cursor.execute('SELECT * FROM table_checkout ORDER BY sold_count').fetchone()
```