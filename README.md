# Students API

It's a simple API to return `Students Data`

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
- Request Body

  - ```json
    {}
    ```

***Response***

```json
[
    {
        "id": 1,
        "name": "Ahmed Hossam",
        "age": 21,
        "birthdate": "2001-04-14",
        "class_number": 1
    },
    {
        "id": 2,
        "name": "Hashem Mohamed",
        "age": 25,
        "birthdate": "1997-02-18",
        "class_number": 4
    },
    {
        "id": 3,
        "name": "Mohamed Salah",
        "age": 25,
        "birthdate": "1997-12-12",
        "class_number": 2
    },
    {
        "id": 4,
        "name": "Wael Ahmed",
        "age": 24,
        "birthdate": "1999-05-21",
        "class_number": 6
    },
]
```

### POST

***Request***

- Request Header
  - ```localhost:8000/student```
- Request Body

  - ```json
    {
        "id": 5,
        "name": "Mina Magdy",
        "age": 20,
        "birthdate": "2001-11-18",
        "class_number": 3
    }
    ```

***Response**

```json
[
    {
        "id": 1,
        "name": "Ahmed Hossam",
        "age": 21,
        "birthdate": "2001-04-14",
        "class_number": 1
    },
    {
        "id": 2,
        "name": "Hashem Mohamed",
        "age": 25,
        "birthdate": "1997-02-18",
        "class_number": 4
    },
    {
        "id": 3,
        "name": "Mohamed Salah",
        "age": 25,
        "birthdate": "1997-12-12",
        "class_number": 2
    },
    {
        "id": 4,
        "name": "Wael Ahmed",
        "age": 24,
        "birthdate": "1999-05-21",
        "class_number": 6
    },
    {
        "id": 5,
        "name": "Mina Magdy",
        "age": 20,
        "birthdate": "2001-11-18",
        "class_number": 3
    }
]
```

### PUT

***Request***

- Request Header
  - ```localhost:8000/student/3/```
- Request Body

  - ```json
    {
        "id": 3,
        "name": "Mohamed Ibrahim",
        "age": 22,
        "birthdate": "2000-12-12",
        "class_number": 4
    }
    ```

***Response***

```json
[
    {
        "id": 1,
        "name": "Ahmed Hossam",
        "age": 21,
        "birthdate": "2001-04-14",
        "class_number": 1
    },
    {
        "id": 2,
        "name": "Hashem Mohamed",
        "age": 25,
        "birthdate": "1997-02-18",
        "class_number": 4
    },
    {
        "id": 3,
        "name": "Mohamed Ibrahim",
        "age": 22,
        "birthdate": "2000-12-12",
        "class_number": 4
    },
    {
        "id": 4,
        "name": "Wael Ahmed",
        "age": 24,
        "birthdate": "1999-05-21",
        "class_number": 6
    },
    {
        "id": 5,
        "name": "Mina Magdy",
        "age": 20,
        "birthdate": "2001-11-18",
        "class_number": 3
    }
]
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
[
    {
        "id": 1,
        "name": "Ahmed Hossam",
        "age": 21,
        "birthdate": "2001-04-14",
        "class_number": 1
    },
    {
        "id": 2,
        "name": "Hashem Mohamed",
        "age": 25,
        "birthdate": "1997-02-18",
        "class_number": 4
    },
    {
        "id": 4,
        "name": "Wael Ahmed",
        "age": 24,
        "birthdate": "1999-05-21",
        "class_number": 6
    },
    {
        "id": 5,
        "name": "Mina Magdy",
        "age": 20,
        "birthdate": "2001-11-18",
        "class_number": 3
    }
]
```

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.
