# Запуск
Вручную можно запустить сервер установив все зависимости:
```bash
pip install -r requirements.txt
```
И запустив `src/server.py`

Иначе можно воспользоваться **docker** образом `eternl334/pari_lab1`, доступным онлайн на [dockerhub](https://hub.docker.com/repository/docker/eternl334/pari_lab1/general). Для этого необходимо воспользоваться следующей командой:

```bash
docker run -p 5000:5000 eternl334/pari_lab1
```

После запуска сервер будет доступен по адресу `http://localhost:5000/`
