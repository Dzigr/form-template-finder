### Form template finder
Fasapi project: form template finder

**Stack:**
* Python
* FastAPI
* MongoDB
* Docker
* Docker-compose

----

### Start project with Docker ###

----

###### Note: Required Python & Poetry ######
1. Clone the repository
    ```comandline
    git clone git@github.com:Dzigr/form-template-finder && cd form-template-finder
    ```

2. Initiate configuration with Makefile command
    ```commandline
    make prepare
    ```
   This will create .env file with necessary variables, requirements file and build docker containers

3. Run application by
    ```commandline
    make start
    ```

<details><summary>
Without poetry
</summary>

---

1. Create virtual environment
    ```commandline
    python3 -m venv venv
    ```
2. Activate virtual environment
    ```commandline 
    source venv/bin/activate
    ```
3. Install requirements via pip
    ```commandline 
    pip install -r requirements.txt
    ```
4. Run docker-compose
    ```bash
    docker-compose up --build
    ```
---
</details>

### Testing:

1. Run tests by
    ```commandline
    make test
    ```

---

### Usage:

[View endpoints if needed][docs]

*GET /api/ping/* - ping api service

*POST /api/get_form/* - receive the query with data 

<details><summary>Request example</summary>

```json lines
  f_name1=value1&f_name2=value2
```

</details>

<details><summary>Response example</summary>

If form found in database return form template name:
```json lines
  "FormName"
```

Otherwise return initial data with serialized fields:
```json lines
{
  "f_name1": FIELD_TYPE,
  "f_name2": FIELD_TYPE
}
```

</details>

### Finally:

1. Clear docker containers
    ```commandline
    make clear
    ```

<!-- links -->

[docs]: http://127.0.0.1:8888/api/docs