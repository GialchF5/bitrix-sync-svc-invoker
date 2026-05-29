# bitrix-sync-svc-invoker

## Краткое описание

Небольшая функция-запускатель для планового вызова сервиса синхронизации Bitrix24 по расписанию из Yandex Cloud.

## Назначение

Описание в Yandex Cloud не заполнено.

## Параметры функции

- ID функции: `d4e755q2ikdvok9hg9nm`
- Каталог Yandex Cloud: `sl`
- Статус: `ACTIVE`
- Runtime: `python311`
- Entry point: `index.handler`
- Версий в экспорте: `1`
- HTTP URL: `https://functions.yandexcloud.net/d4e755q2ikdvok9hg9nm`

## Триггеры

- `b24-sync-svc-fn` (`a1so4kcmn0vebvgorid6`), статус: `ACTIVE`, cron: `0 18 ? * * *`

## Переменные окружения

Значения не хранятся в sanitized-экспорте. Реальные значения находятся только в raw/, эту папку нельзя коммитить в GitHub.

- `CONTAINER_URL`
- `RUN_TOKEN`

Пример .env:

```dotenv
CONTAINER_URL=<set-value>
RUN_TOKEN=<set-value>
```

## Локальный запуск

```powershell
cd .\yc-export-author-gilach\sanitized\functions\bitrix-sync-svc-invoker
# Положи исходники функции в эту папку: index.py, requirements.txt и остальные файлы.
# Создай .env по примеру выше и event.json с тестовым событием.
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -c "import json, index; event=json.load(open('event.json', encoding='utf-8')); print(index.handler(event, None))"
```

Если локально нет версии Python, совпадающей с runtime `python311`, используй ближайшую совместимую версию только после проверки зависимостей.

Минимальный event.json для ручной проверки:

```json
{}
```

## Деплой новой версии

Перед деплоем проверь, что в папке лежат исходники функции и файл с зависимостями (`package.json` для Node.js или `requirements.txt` для Python).

```powershell
yc serverless function version create --function-id d4e755q2ikdvok9hg9nm --runtime python311 --entrypoint index.handler --source-path . --execution-timeout 60s
```

Если функции нужны переменные окружения, передавай их через `--environment` или настрой через консоль/секреты. Не коммить реальные токены, пароли, webhook URL и сертификаты в GitHub.

## Файлы экспорта

- `function.json` - описание функции.
- `versions.json` - версии функции с замаскированными значениями переменных окружения.