## Flask Auto Test Application

This is a Test Application for project Auto Test.

### Requirements

1. The python module requirements are mentioned in requirements.txt inside the root folder.
2. The deployment will require active internet connection
   in order to download the static libraries for frontend. (e.g. Bootstrap)

### To Run the Server

1. Dockerfile resides in `docker` directory.
2. Change to `docker` directory.
3. Run `docker build . -t autop`
4. Run `docker run -p "5000:5000"  -tdi autop`

### Accessing and Using the Server

1. Access the endpoint [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
2. Click "Populate Database" in order to fetch data from the remote web source.
3. In case of issue, click "Teardown Table" to drop the table and start fresh.
4. Home page lists the paginated view of All the Trucks from the local database.
5. [Sport](http://127.0.0.1:5000/Sport?car_type=Sport) link lists all the Sports cars from the local database. 
6. In order to fetch the price of a vehicle, click on "Get Price"

### Nodejs (expressjs) version of this app

1. https://github.com/ashayshub/express-autop
