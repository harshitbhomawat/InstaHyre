API created using django.

**To populate the database use dump.json file. Run command 'python manage.py loaddata dump.json' in terminal.


Endpoints:-

1) http://127.0.0.1:8000/api/register: (POST)

**description:
endpoint to register a new user.

**required fields:
a)name
b)phone_number
c)password
d)confirm_password
e)email(optional)

2) http://127.0.0.1:8000/api/login: (POST)

**description:
endpoint to login and get authentication token, Returns the authentication token.

**required fields:
a)phone_number
b)password

3) http://127.0.0.1:8000/api/search_by_name: (POST)

**description:
endpoint to search for contacts by name. Returns a list of contacts with exactly and partially matching names

**required fields:
a)name

4) http://127.0.0.1:8000/api/search_by_number: (POST)

**description:
endpoint to search for contacts by number. Returns the details of user registered with this number,
else returns a list of contacts with exactly same number

**required fields:
a)phone_number

5) http://127.0.0.1:8000/api/view_contact: (POST)

**description:
endpoint to search for contacts by id. Returns the contact details with this id.

**required fields:
a)contact_id

6) http://127.0.0.1:8000/docs: (GET)

**description:
endpoint to see the documentation made with swagger

7) http://127.0.0.1:8000/openapi: (GET)

**description:
endpoint to get the Schema.



*** All endpoints except register and login requires the authentication token to be passed as header, hence no public access
    to anything***

->To get authentication token, send a valid request to "http://127.0.0.1:8000/api/login".
->To Check endpoints use postman.
->To pass token as a header in postman:
a)click on headers tab.
b)type 'Authorization' in key column and 'Token your_token' in value column, type the token you got from login in place of your_token in value column.
