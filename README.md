# KonfidanTea

1. git clone project
2. python -m venv .venv
3. ./.venv/Scripts/activate
4. pip install -r requirements.txt
5. flask run (database.db is created)
6. open http://localhost:5010
7. click "Initialize" (db entities are created)
8. obtain LK (local key) using the generator under Tools
10. obtainer eRK (encrypted remote key) using the generator and then the encryptor (with LK) under Tools
11. add env var KONFIDANTEA_LOCAL_KEY with the VALUE of LK
12. add env var KONFIDANTEA_REMOTE_KEYS with the LOCATIONS of eRK (comma separated)
13. add env var KONFIDANTEA_HOME with path to venv
14. add env var KONFIDANTEA_PORT with port 5010
15. run run.bat as service using NSSM (Non Sucking Service Manager)