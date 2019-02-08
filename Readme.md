# Log Ticket Settlement WebApp

### Modules
The current modules included in this project are:
* database_setup.py

### Description:
This project is developed in Python 3.  It will be a Flask Application for Loggers and Forest Managers to track Logging Settlement Tickets.  Often these tickets are aggregated on paper receipts and must be hand entered into a spreadsheet for proper accounting of the hauled loads.  This application will help improve that system by making it more reliable, more flexible, and more accessible than a typical spreadsheet solution.

* The project sets up a SQLite database for a tracking tickets.  The Python script uses
SQLAlchemy as an ORM for the database and generates the database in the current working directory.


### Requirements
This application is in progress and will be a updated as new modules are completed.

### Running:
The code cannot be run without the associated database.
* Creating the database:
  The database is created by executing the Python script 'database_setup.py' from a shell prompt.
  The only dependency needed to create the database is:
  > sqlalchemy



### Author:
Jon Lunsford, March 18, 2018
