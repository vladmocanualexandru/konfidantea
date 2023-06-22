call %KONFIDANTEA_HOME%\.venv\scripts\activate
call waitress-serve --host 127.0.0.1 --port %KONFIDANTEA_PORT% konfidantea:app