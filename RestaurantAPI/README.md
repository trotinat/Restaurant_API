
# Restaurant BackEnd

This repository contains the backend codebase for a restaurant app developed using Django, a powerful and popular Python web framework. The backend provides a solid foundation for building a feature-rich restaurant application, enabling efficient management of restaurant operations, menu updates, order processing, and customer engagement.


## Tech Stack

**BackEnd** : Django,MySql

## Related

Here are some related projects

[Scrapping](https://github.com/AdilCHBALY/Restaurant-Scrapping)
[FrontEnd](https://github.com/AdilCHBALY/Restaurant_frontend)

## Run Locally

Clone the project

```bash
  git clone https://github.com/AdilCHBALY/Restaurant_API.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Configure the database settings in the settings.py file to connect to your desired database server.

Run database migrations 

```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```


## API Reference

#### Get all Restaurants

```http
  GET /restaurant
```

#### Get Restaurant Details

```http
  GET /restaurant/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of Restaurant to fetch |

#### Get all the Cities

```http
  GET /city
```

#### Get Restuarants of a City

```http
  GET /city/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of City to fetch |


