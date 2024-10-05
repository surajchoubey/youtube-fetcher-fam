# YOUTUBE FETCHER APPLICATION

![Screenshot 2024-10-05 at 11 54 13](https://github.com/user-attachments/assets/0fc1e3b3-d00c-4a71-a826-83690fb7d7d5)

## (1/4) BASIC VIEW 

The cron job keeps running every 10 seconds in the background and makes sure it saves only unique videos in the database so no videos are repeated.

<img width="425" alt="Screenshot 2024-10-05 at 11 59 07" src="https://github.com/user-attachments/assets/a8840c00-f1ec-4e11-a80b-db47f83b03d9">


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
| Search           | ![Screenshot 2024-10-05 at 11 55 41](https://github.com/user-attachments/assets/faed003e-2fda-43ad-bad1-9ca3597e9617) | Optimized search that filters all the keywords you type in the search query.                                                                                                                      |
| Before           | ![Screenshot 2024-10-05 at 11 56 25](https://github.com/user-attachments/assets/2eb9dc0c-521e-4b08-bfbe-2651bff7b3d3) | Select a particular publishing date to fetch videos published **before** that date.                                                                                                              |
| After            | ![Screenshot 2024-10-05 at 11 56 44](https://github.com/user-attachments/assets/72bf2d01-60d1-4dd8-a20c-98ea7f6aceed) | Select a particular publishing date to fetch videos published **after** that date.                                                                                                               |
| SortBy           | ![Screenshot 2024-10-05 at 11 56 56](https://github.com/user-attachments/assets/8a834061-7a2e-48b5-9fd1-95ea74a7f673) | Click on the button to set the results in ascending or descending order of publishing date.                                                                                                      |
| Pagination       | ![Screenshot 2024-10-05 at 11 57 15](https://github.com/user-attachments/assets/06cc9262-1e8c-435e-aa54-682121b88fb9) | Select a particular page of results. Each page returns 10 results by default.                                                                                                                    |




