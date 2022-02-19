# NordCloud- NetworkSpeed


## Problem Statement
Problem is to find the best network station for given device coordinates that is within the reach, the reach and coordinated for all the network station are given.

If the distance between the device coordinate and station coordiante is greater then for all station reach. The output should be "No station for the device coordinate DEVICE_COORDINATES".

If the distance<reach, then the speed is calculated with the following formula:
(reach - distance)^2.

The station which have the highest speed will be the output with the following statement: "The best station for the device coordinates DEVICE_COORDINATES the best station is STATION_COORDINATES with the speed MAX_SPEED"




## Run the app

To run the code clone the repository by the following command on the command line terminal in the local machine:

```
git clone CLONE_URL
```

## Run the app locally

You need to have have docker installed on local machine to run the app.

```
docker build -t nord .
docker run -p 0.0.0.0:8080:8080 --name nord nord
```

The ouput can be seen on the url: http://127.0.0.1:8080



## Run the app in cloud 
The web application for the problem statement is served for the purpose of deployment on the cloud.

The web application is deployed on the Google Cloud Platform, it can be viewed by opening the following URL:  https://app-snyge32fia-lm.a.run.app.

## Cloud Deployment

The following steps are performed for the deployment of web application on the cloud.

- STEP 1:
There should be an account on the google cloud platform (gcp).
Create a new project in your gcp account.
Remeber the project should be linked with billing account then only it will allow to deploy the application.

- STEP 2:
There should be google cloud SDK shell in the local machine in order to deploy the application.
To install the google cloud CLI, follow the tutorial from the following link:https://cloud.google.com/sdk/docs/install

- STEP 3:
 Open the google cloud shell in hte folder and type the following commands:
```
gcloud config set project YOUR_PROJECT_ID(Get from gcp)
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/app:0.1
gcloud run deploy app --image gcr.io/YOUR_PROJECT_ID/app:0.1 --platform managed
```

After these commands the appication will be deployed and can url can be shared to be seen by other users.

## Run the test cases

For running the test cases.

```
python test.py -v
```



>Utkarsh Goyal


