# Flask Product API with React frontend

## Create .env file for Frontend API Calls

To bind backend API calls, create a `.env` file from the example file:

```bash
cp ./frontend/.env.example ./frontend/.env
```

## How to run
```bash
  docker compose up -d

```

## How to test api with curl commands
```bash
  chmod +x curl-tests.sh
  ./curl-tests.sh
```

## How to test api with frontend
Frontend runs at: http://localhost:3000