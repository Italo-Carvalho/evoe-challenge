
  

<h1  align="center">

<img  alt="evoe"  title="#evoe"  src="https://evoe.cc/static/images/evoe_logo_2020_fff.svg"  width="250px" />

</h1>

  

<h4  align="center">

🚀 Challenger Evoé - Django/Flask
</h4>
<p align="center">
  <a href="#-project">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#wrench-back-end-build-and-start">Back-end Build and Start</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-api-documentation-with-swagger">Api Documentation</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-front-end">Front-end</a>

</p>

<br>

  
  

## 💻 Project

  

Develop a Simple API using the Django and Django Rest API frameworks to register a ToDo.

  

## :wrench: Back-end Build and Start

  

```
$ cd back
$ sudo docker-compose up --build
```

  

## 📖 Api Documentation with Swagger

After starting the project, documentation will be available at:

```http://0.0.0.0:8000```

Create a user with the method ```POST``` in ```/user/```

![postuser](/.github/post_user.png)

Get your access token with method ```POST``` in ```/token/```

![accesstoken](/.github/get_token.png)

At the top of the page go to the button Authorize

![authorize](/.github/authorize.png)

And follow the example of the image

![token_login](/.github/token_login.png)

Access token in avaliable during 5 min and Refresh token in avaliable during 1 day, on access token expirate you can get new token with method ```POST``` and refresh key on ```/token/refresh/```, or login again in ```/token/```. 

## 🌐 Front-end

Front-end depend to back-end is running to work, for start follow the commands.

```
$ cd front
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python3 run.py 
```
### Login page

![login](/.github/login.png)
### Register page

![register](/.github/register.png)

### Notes page

![notes](/.github/notes.png)