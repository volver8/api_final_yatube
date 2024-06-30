# Api YaTube

## Description
*This API implements a backend for a web application*

*API documentation:* [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

![](https://www.ibexa.co/var/site/storage/images/_aliases/ibexa_content_full/3/4/1/0/300143-1-eng-GB/d4255a27c1fa-AdobeStock_261705271_What-is-an-API.jpeg)

This API implements serialization and deserialization of data in models such as:
- Post
- Group
- Comment
- Follow

## Requests
There are some examples of requests:
  -  Model Post

      - GET request: /api/v1/posts/
          ```
          {
            "count": 123,
            "next": "http://api.example.org/accounts/?offset=400&limit=100",
            "previous": "http://api.example.org/accounts/?offset=200&limit=100",
            "results": [
              {
                "id": 0,
                "author": "string",
                "text": "string",
                "pub_date": "2021-10-14T20:41:29.648Z",
                "image": "string",
                "group": 0
              }
            ]
          }
          ```
      - POST request: /api/v1/posts/

        - Request samples
        ```
        {
        "text": "string",
        "image": "string",
        "group": 0
        }
        ```
        - Response samples
        ```
        {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2019-08-24T14:15:22Z",
        "image": "string",
        "group": 0
        }
        ```
       
  -  JWT token

      - POST request: /api/v1/jwt/create/

        - Request samples
        ```
        {
        "username": "string",
        "password": "string"
        }
        ```
        - Response samples
        ```
        {
        "refresh": "string",
        "access": "string"
        }
        ```

## My contacts:

- *email:* rvs@yandex.ru
- *telegram:* underover_one
