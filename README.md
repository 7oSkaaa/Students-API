# Students API

It's a simple API to deal with `Students Data`

## Installation

Install my-project with poetry

```shell
# clone the repo
git clone https://github.com/7oSkaaa/Students-API.git
```

```shell
# get the directory of the repo
cd Students-API
```

```shell
# start the project
poetry shell
poetry install
python manage.py runserver
```

## Usage/Examples

There are 4 allowed requests:

- GET
- POST
- PUT
- DELETE

---

### GET

***Request***

- Request Header
  - `localhost:8000/student`
  - `localhost:8000/student/1`
- Request Body

  - ```json
    {}
    ```

***Response***

- ```json
    {
        "students": [
            {
                "id": 1,
                "first_name": "Ahmed",
                "last_name": "Hossam",
                "email": "ahmed.7oskaa@gmail.com",
                "age": 21,
                "class_number": 1
            },
            {
                "id": 3,
                "first_name": "Wael",
                "last_name": "Ahmed",
                "email": "wael.ahmed99@gmail.com",
                "age": 24,
                "class_number": 5
            }
        ]
    }
    ```

- ```json
    {
        "student": [
            {
                "id": 1,
                "first_name": "Ahmed",
                "last_name": "Hossam",
                "email": "ahmed.7oskaa@gmail.com",
                "age": 21,
                "class_number": 1
            }
        ]
    }
    ```

### POST

***Request***

- Request Header
  - ```localhost:8000/student```
- Request Body

  - ```json
    {
        "id": 2,
        "first_name": "Mina",
        "last_name": "Magdy",
        "email": "minamagdy@gmail.com",
        "age": 20,
        "class_number": 3
    }
    ```

***Response**

```json
{
    "students": [
        {
            "id": 1,
            "first_name": "Ahmed",
            "last_name": "Hossam",
            "email": "ahmed.7oskaa@gmail.com",
            "age": 21,
            "class_number": 1
        },
        {
            "id": 2,
            "first_name": "Mina",
            "last_name": "Magdy",
            "email": "minamagdy@gmail.com",
            "age": 20,
            "class_number": 3
        },
        {
            "id": 3,
            "first_name": "Wael",
            "last_name": "Ahmed",
            "email": "wael.ahmed99@gmail.com",
            "age": 24,
            "class_number": 5
        }
    ]
}
```

### PUT

***Request***

- Request Header
  - ```localhost:8000/student/3/```
- Request Body

  - ```json
    {
        "id": 3,
        "first_name": "Mohamed",
        "last_name": "Ibrahim",
        "email": "mo_Ibrahim@gmail.com",
        "age": 20,
        "class_number": 5
    }
    ```

***Response***

```json
{
    "students": [
        {
            "id": 1,
            "first_name": "Ahmed",
            "last_name": "Hossam",
            "email": "ahmed.7oskaa@gmail.com",
            "age": 21,
            "class_number": 1
        },
        {
            "id": 2,
            "first_name": "Mina",
            "last_name": "Magdy",
            "email": "minamagdy@gmail.com",
            "age": 20,
            "class_number": 3
        },
        {
            "id": 3,
            "first_name": "Mohamed",
            "last_name": "Ibrahim",
            "email": "mo_Ibrahim@gmail.com",
            "age": 20,
            "class_number": 5
        }
    ]
}
```

### DELETE

***Request***

- Request Header
  - ```localhost:8000/student/3/```
- Request Body

  - ```json
    {}
    ```

***Response***

```json
{
    "students": [
        {
            "id": 1,
            "first_name": "Ahmed",
            "last_name": "Hossam",
            "email": "ahmed.7oskaa@gmail.com",
            "age": 21,
            "class_number": 1
        },
        {
            "id": 2,
            "first_name": "Mina",
            "last_name": "Magdy",
            "email": "minamagdy@gmail.com",
            "age": 20,
            "class_number": 3
        }
    ]
}
```

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.
