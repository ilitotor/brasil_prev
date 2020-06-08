# BRASIL PREV - CHALLENGE PYTHON

#### API RESPONSES

Clone this repo:\
` git clone git@github.com:ilitotor/brasil_prev.git `

Go to the project directory and build project container:\
` docker-compose up  `


To access the endpoints: \
`http://0.0.0.0:8000/api/v1/product/` \
`http://0.0.0.0:8000/api/v1/clients/` \
`http://0.0.0.0:8000/api/v1/carts/` 

#### TESTS

Run:\
`docker ps`

Get the _Container ID_ then run:\
`docker exec -ti <container id> bash`

Then, inside the container execute:
`python manage.py test`
