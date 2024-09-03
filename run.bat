call %KONFIDANTEA_VENV%\Scripts\activate
waitress-serve --host 127.0.0.1 --port %KONFIDANTEA_PORT% konfidantea:app