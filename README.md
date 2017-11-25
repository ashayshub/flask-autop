## Flask Auto Test Application

This is a Test Application for project Auto Test.

### Requirements

1. The python module requirements are mentioned in requirements.txt inside the root folder.
2. The deployment will require active internet connection
   in order to download the static libraries for frontend. (e.g. Bootstrap)

### ToDo
1. Add `get price` functionality to the "Get Price" button.  

### To Run the Server

1. Dockerfile resides in `docker` directory.
2. Change to `docker` directory.
3. Run `docker build . -t autop`
4. Run `docker run -p "5000:5000"  -tdi autop`
5. Access the endpoint [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Accessing and Using the Server

1. Click "Populate Database" in order to fetch data from the remote web source.
2. In case of issue, click "Teardown Table" to drop the table and start fresh.
3. Home page lists the paginated view of All the Trucks from the local database.
4. `/Sport` page lists all the Sports cars from the local database. 
