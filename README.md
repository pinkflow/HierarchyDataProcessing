# HierarchyDataProcessing

### Установка
Для установки требуется создать виртуальное окружение и установить пакет psycopg2 версии 2.9.3:  
pip install psycopg2==2.9.3

Далее необходимо запустить программу с помощью команды:  
python main.py {arg}  
Вместо {arg} подставить аргумент(идентификатор сотрудника)  

### Описание текущего решения
Решение использует стандартные библиотеки Python 3.10 и PostgreSQL 10.20.  
Для соединения с базой данных PostgreSQL используется сторонний пакет psycopg2 версии 2.9.3.  
Утилита принимает идентификатор строки и осуществляет поиск строк с таким же предком высшего уровня, как у входной строки.  
Утилита возвращает список строковых значений имен (Name во входном json) в строках, полученных способом выше.  

### SQL выборка
Для получения необходимых строк используется рекурсивный запрос, который сначала производит полное вычисление предка высшего порядка для каждой строки и только после этого выбирает из этого строки с предком, который равен предку входного значения.
В ходе выполнения запроса для каждого уровня осуществляется join с собственной таблицей по id и родителя.
Оптимизировать получение данных из таблицы помогло бы использование ltree меток, это позволило бы единожды получить предка высшего порядка и с его помощью получить все дочерние значения низшего порядка.
