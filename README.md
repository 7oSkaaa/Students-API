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

***You can use the following endpoints:***

- `swagger/` - for API documentation
- `admin/` - for admin dashboard
- `/student/` - for `GET` and `POST` requests
- `/student/<int>` - for `GET`, `PUT` and `DELETE` requests
- `/parent/` - for `GET` and `POST` requests
- `/parent/<int>` - for `GET`, `PUT` and `DELETE` requests
- `/subject/` - for `GET` and `POST` requests
- `/subject/<int>` - for `GET`, `PUT` and `DELETE` requests

***There are some relations between the apps:***

- `Student` has `ManyToMany` relation with `Subject`
- `Student` has `OneToOne` relation with `Parent`

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.
