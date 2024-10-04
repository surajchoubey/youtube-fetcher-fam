# YOUTUBE FETCHER APPLICATION

## (1/4) BASIC VIEW 

The cron job keeps running every 10 seconds in the background and makes sure it saves only unique videos in the database so no videos are repeated.

![Screenshot 2024-10-04 at 18 11 01](https://github.com/user-attachments/assets/004d58cc-8eb7-40d9-84b5-bb1986591f8e)

## (2/4) HOW TO USE THIS PROJECT WITHOUT DOCKER ?

Run the following commands which includes cloning the github repo installing python packages for flask backend and node modules for frontend application.
After that index.html created from `npm run build` will be used by python backend flask server.

1. Clone the github repo and `cd` into it
```
git clone https://github.com/surajchoubey/youtube-fetcher-fam
cd youtube-fetcher-fam
```

2. Install node modules for frontend and build frontend
```
npm install
npm run build
```
3. Create virtual environment for python packages and install python packages
```
python -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt # use pip/pip3 accordingly
```
4. Run server
```
python3 index.py # use python/python3 accordingly
```

5. Deactivate the environment using:

```
deactivate
```

## (3/4) HOW TO USE THIS PROJECT USING DOCKER ?

If you wish to go through the docker steps, please have docker installed command line for this


1. Clone the github repo and `cd` into it
```
git clone https://github.com/surajchoubey/youtube-fetcher-fam
cd youtube-fetcher-fam
```

2. Build docker image
```
sudo docker build -t fampay-app .
```

3. Now you can see list of docker images using
```
docker images
```

4. Build a container using the command. Enjoy your server running on http://127.0.0.1:5001
```
docker run -d -p 5001:5001 --name fampay-container fampay-app
```

5. Stop the docker container using
```
sudo docker container stop fampay-container
```

## (4/4) FUNCTIONAL FRONTEND OPTIONS

| **Feature**      | **Image** | **Description**                                                                                                                                                                                  |
|------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger Button   | ![Screenshot 2024-10-04 at 19 01 59](https://github.com/user-attachments/assets/6c5ff114-85b3-48a9-9410-0a418ec087fb) | This button triggers the backend to get videos from the last 5 days, runs every 10 seconds, and takes 55-60 seconds to completely execute the operation. It also saves the data into the database. Every time you click, it saves 50 videos (10 videos per day for 5 days). |
| Search           | ![Screenshot 2024-10-04 at 19 03 52](https://github.com/user-attachments/assets/42b0c114-cf05-4dd3-b502-ce5aab7a870f) | Optimized search that filters all the keywords you type in the search query.                                                                                                                      |
| Before           | ![Screenshot 2024-10-04 at 19 04 42](https://github.com/user-attachments/assets/c5858b81-00aa-453a-94db-2c6b0d514b88) | Select a particular publishing date to fetch videos published **before** that date.                                                                                                              |
| After            | ![Screenshot 2024-10-04 at 19 05 03](https://github.com/user-attachments/assets/f3fa5dd9-9da7-44e3-803a-2622a9c10c05) | Select a particular publishing date to fetch videos published **after** that date.                                                                                                               |
| SortBy           | ![Screenshot 2024-10-04 at 19 06 03](https://github.com/user-attachments/assets/0fbed62e-0a11-4cd3-afee-c3bc64f7c5cd)| Click on the button to set the results in ascending or descending order of publishing date.                                                                                                      |
| Pagination       | ![Screenshot 2024-10-04 at 19 08 00](https://github.com/user-attachments/assets/79a1a958-1d96-40fb-a97e-b485e9eeac2f)| Select a particular page of results. Each page returns 10 results by default.                                                                                                                    |




