# VigilyteAgents

The Django backend serves the dashboard and its API from the same origin. From
the `backend` directory, run migrations and start the development server:

```sh
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. The dashboard loads wallet records from
`/api/wallets/` and mandate records from `/api/mandates/`; use **Refresh** to
reload them. Wallet signing seeds are not included in API responses.