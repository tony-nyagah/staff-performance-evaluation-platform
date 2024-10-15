# Staff performance Evaluation Platform
This is a platform used to evaluate staff performance. 
The goal is to reduce the use of Excel sheets and have a central place for evaluations.

## Setting up for development
Most of the important commands have been placed in the `makefile` in the project root.    
The commands can be viewed by running the `make` or `make help` command.    
A command can be run by running `make <command>`, replace `<command>` with the name of the command.

## Running the app locally
First migrate the database: `make migrate`.    
Next, create a superuser: `make createsuperuser`.  
Finally, run the app: `make runserver`.

Locally, it will run on [http://localhost:8030/](http://localhost:8030/).    
First thing you will see is a login screen. Login and look around.    
To access the admin console, go to [http://localhost:8030/admin/](http://localhost:8030/admin/).   