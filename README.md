# bias-detection-backend
## overview

UROP project: Building a bias-aware news platform

Author (Bachelor in Computer Science): Xu Boran bxual@connect.ust.hk

Hong Kong University of Science and Technology

Professor: Ma Xiaojuan, Supervisor: Zheng Chengbo

This project aims to build a bias-aware news platform. The frontend of it is a web-application written with javascript and react. The backend is another web-application written with python and flask. This repository is its backend. The application features a database consisting of json files of the news items. When initialized, the application checks if there is new additions to the database, and use its NLP model to predict and save their political-bias. When it is running, the application can respond to requests and send the news content along with their bias to the frontend.

## instructions to run this application

follow these steps:
1. install necessary python packages, including flask
2. cd to the root directory
3. run command: flask run
4. the application will be running locally.

Please run this application along with the frontend to see the effect.
