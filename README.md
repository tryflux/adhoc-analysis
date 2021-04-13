# adhoc-analysis 📊

### Requirements
Currently the main requirements are python3 >= 3.8, and postgres. Both can installed using brew

$ brew install python
$ brew install postgresql
Jupyter
Note: All commands are assumed to be running at the root of the directory.

Most of our experiments include a Jupyter notebook. Jupyter is very simple to use and ships with it's own web-based GUI, to get started you should install the project dependencies inside your virtual environment:

(venv) $ pip3 install -r requirements.txt
And start Jupyter like so:

(venv) $ make jupyter
This will set up the PYTHONPATH and set PROJECTROOT which allow use of the utils module.

### Database
If you want Jupyter notebooks to connect to the DB you'll need to:

Copy the sample credentials file to .credentials and add your replica username and password to it.
$ cp credentials .credentials
Create an SSH tunnel
$ ssh -N -L 5432:replica.production.env.tryflux.com:5432 {username}@jumpbox.tryflux.com
You'll be prompted to tap your Yubikey and then nothing will appear to happen but the tunnel will be set up, and you can start querying the DB in your notebooks.

