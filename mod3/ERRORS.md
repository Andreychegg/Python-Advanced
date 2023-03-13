Метод `get_age()` неправильно вычислял возраст, вычисляя текущий год из года рождения

```    
def get_age(self):
        now = datetime.now()
        return now.year - self.yob
```

Метод `set_name()` неверно присваивал имя человека, потому что он использовал не переданное имя, а текущее имя объекта

```
def set_name(self, name):
    self.name = name
```

Метод `set_address` использовал оператор сравнивания `==` вместо оператора присваивания `=`

```
def set_address(self, address):
    self.address = address
```

Метод `is_homeless()` неверно возвращал значение, если адрес не установлен. Он проверял, что переменная address является None, в то время как адрес может быть пустой строкой. Необходимо проверять, что переменная address равна пустой строке

```
def is_homeless(self):
    return self.address == ''
```
