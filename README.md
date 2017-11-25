## Flask Auto Test Application

This is a Test Application for project Auto Test.

### Requirements

1. The python module requirements are mentioned in requirements.txt inside the root folder.
2. The deployment will require active internet connection
   in order to download the static libraries for frontend. (e.g. Bootstrap)

### ToDo
1. Add relative paths to the static and templates folders.
2. Add `get price` functionality to the "Get Price" button.  

### To Run the Server

1. Dockerfile resides in `docker` directory.
2. Change to `docker` directory.
3. Run `docker build . -t autop`
4. Run `docker run -p "5000:5000"  -tdi autop`
5. Access the endpoint [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
