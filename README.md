# KonfidanTea

Prerequisites:
- Python
- pipx
- Poetry
- nssm

1. git clone project
2. open project folder
3. add env var KONFIDANTEA_HOME
4. add env var KONFIDANTEA_PORT
5. poetry install
6. add env var KONFIDANTEA_VENV with the location of poetry venv
7. poetry run flask run (database.db is created)
8. open http://localhost:<port>
9. click "Initialize" (db entities are created)
10. obtain LK (local key) using the generator under Tools
11. add env var KONFIDANTEA_LOCAL_KEY
12. obtainer eRK (encrypted remote key) using the generator and then the encryptor (with LK) under Tools
13. add env var KONFIDANTEA_REMOTE_KEYS with the LOCATIONS of eRK (comma separated)
14. run run.bat as service using NSSM (Non Sucking Service Manager)
15. decrypt using POST API call: http://127.0.0.1:<port>/decrypt (param "id" -> db entry id/ref)