## Установка зависимостей и запуск проекта
```zsh
# Серверная часть

pip install -r requirements.txt
fastapi dev main.py


# Клиентская часть

cd front-end
npm install
npm run dev
```


## Предупреждение
git update-index --assume-unchanged credentials.json

What’s more, Sheets API v4 introduced Usage Limits (as of this writing, 300 requests per 60 seconds per project, and 60 requests per 60 seconds per user). When your application hits that limit, you get an APIError 429 RESOURCE_EXHAUSTED.


## Как создать ключ для Google sheets API в GoogleCloudConsole
https://www.youtube.com/watch?v=zCEJurLGFRk


## Google-Sheets-API-Python
### Doc : gspread : https://docs.gspread.org/en/v6.1.4/index.html


## Структура проекта

```zsh



```