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
```

## migrate the database

```shell
python manage.py makemigrations
python manage.py migrate
```

## Run the project

```shell
python manage.py runserver
```

## Usage/Examples

***There are 4 allowed requests:***

- GET
- POST
- PUT
- DELETE

---

## Details

***There are 3 apps in the project:***

- student
- parent
- subject
- token
- account
- swagger

***You can use the following endpoints:***

- `swagger/` - for API documentation
- `admin/` - for admin dashboard
- `/student/` - for `GET` and `POST` requests
- `/student/<int>` - for `GET`, `PUT` and `DELETE` requests
- `/parent/` - for `GET` and `POST` requests (you must be logged in to use this endpoint and deal with only your data)
- `/parent/<int>` - for `GET`, `PUT` and `DELETE` requests (you must be logged in to use this endpoint and deal with only your data)
- `/subject/` - for `GET` and `POST` requests
- `/subject/<int>` - for `GET`, `PUT` and `DELETE` requests
- `/account/register/` - for `POST` requests (register new user not exist in database)
- `/account/login/` - for `POST` requests (login user exist in database and get token)

***There are some relations between the apps:***

- `Student` has `ManyToMany` relation with `Subject`
- `Student` has `OneToOne` relation with `Parent`
- `Parent` has `OneToOne` relation with `account`
- `Parent` has `oneToMany` relation with `token`

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.
