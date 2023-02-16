# Kosha Google Mail

Google Mail connector can be used to access Gmail mailboxes and send mail.

![Gmail](images/gmail.png)

This Connector API exposes REST API endpoints to perform any operations on Google Mail service in a simple, quick and intuitive fashion.

It describes various API operations, related request and response structures, and error codes. 

## Build

To start the virtualenv of the project, run
```
    pipenv shell
```

To install dependencies, run
```
    pipenv install
```

## Run

To run the project, simply provide env variables to supply your Google Cloud Application Client ID, Client Secret to connect to.


```bash
AWS_SERVER_PUBLIC_KEY=<PUBLIC_KEY> AWS_SERVER_SECRET_KEY=<SECRET_KEY>  uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8002
```

This will start a worker and expose the API on port `8002` on the host machine 

Swagger docs is available at `https://localhost:8002/docs`
