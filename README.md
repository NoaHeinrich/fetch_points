# fetch_points
Back end developer assessment

To run this project, clone it to your machine.

From inside the directory, run `source venv/bin/activate` to enter the virtual environment. Then `pip install django djangorestframework`.

Then `cd fetch_points` to enter the project directory. Migrate the database by running `python manage.py migrate`, and then run `python manage.py runserver` to begin the developer server. The server should be running at http:localhost:8000.

To create a new user, send a POST request to http://localhost:8000/posts/users/new. If successful, a GET request to localhost:8000/posts/users/{user_id} will show that current user's data.

To create a new transaction, send a POST request to http://localhost:8000/points/users/{user_id}/add-points, along with form data with the name of the payer and the amount paid.

To deduct points from a user, send a POST request to http://localhost:8000/points/users/{user_id}/deduct-points, along with form data containing the amount of points you wish to deduct.
