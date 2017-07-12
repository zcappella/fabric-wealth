# fabric-wealth
Widget coding challenge for Fabric Wealth

The goal for this project is to showcase my back end and front end skills as it relates to web development. My personal goal is to show a little of both sides of the house, while primarily focusing on the back end functionality. I want to put my own personal spin on this assignment and see what comes out of it. 



Moving Forward:
There are many things that I would change in future editions of the software:

-I would move the function based views to at least a class based view and clean up the 'if request.method' ugliness.<br />
-I would add a more robust filtering and searching mechanism than DataTables.<br />
-They are a nice resource, but not full featured.<br />
-I would spruce up the front end significantly by adding custom css, javascript, and more.<br />
-I would add user authentication to associate orders, thus making it easier to create a better order list/update page<br />
-I would clean up my static files significantly<br />
-I'm certain that there are files that are unnecessary, but I keep them to be safe<br />
-Django does a great deal of security for us with the csrf_token and XSS protection, but a more robust structure would be preferred.<br />
-Including a front end framework would be really helpful with the order create and edit functionality<br />



If building locally:<br />
There are just a few steps needed to be taken to build this project locally:<br />

-Create virtual environment<br />
-Have Python3<br />
-pip install -r requirements.txt<br />
-Make migrations<br />
-Create super user (python manage.py createsuperuser)<br />
-Collect the static files (python manage.py collectstatic)<br />
-Load the data in from the database (python manage.py loaddata db.json)<br />
-Then the application should be able to be run<br />
