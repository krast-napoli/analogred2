# analogred2
#### Цель данного проекта - создание web-приложения - аналога БД Redis. Проект выполняется при помощи Flask и flask_restful, роль БД выполняет классичесий питоновский словарь

#### На данный момент реализована CRUD-функциональность и web-страница с текущей базой

### Запуск приложения
- pip install -r requirements.txt для установки зависимостей
+ запуск python3 analogred2.py
+ http запросы при помощи утилиты curl или библиотеки httpie. Например, POST запрос curl http://localhost:5000/year1987 -d "data=Australia" -X PUT выдаст результат 'year1987':'Australia'
+ результат также можно видеть на localhost:5000

### Запуск приложения (при помощи Docker)
- docker run -p 8888:5000 krast47/analogred2
