
# Stepik course 575

Special repo for this task

[link to course](https://stepik.org/course/575/syllabus)

## Lesson 3 step 6 - review task


**Prerequisites::**
You need python3 on you host (PATH also must be set up)

_for linux_:
```bash
~ $ git clone "https://github.com/ChehST/stepik_575"
~ $ cd stepik_575
~ $ python -m venv .venv
~ $ source .venv/bin/acivate
~ $ pip3 install -r requirments.txt
~ $ pytest --language=es core/test_items.py
```

steps:
- [x] Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
- [x] Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
- [x] Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
- [x] В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
- [x] Тест должен запускаться с параметром language следующей командой:        ```pytest --language=es test_items.py```
- и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
- [x] Отправить ссылку на данный репозиторий в качестве ответа на данное задание.
- Отправить решение на рецензирование другим учащимся. Не забудьте, что решение на рецензирование можно отправить только один раз.
- [ ] Проверьте решения минимум трех других учащихся, чтобы получить баллы за задание.
