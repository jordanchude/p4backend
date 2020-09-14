# Project Overview

## Project Link
- [Link](https://cinefavorites.netlify.app/#/)

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Incomplete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Incomplete
|Day 2| Working RestAPI | Incomplete
|Day 3| Core Application Structure (HTML, CSS, etc.) | Incomplete
|Day 4| MVP & Bug Fixes | Incomplete
|Day 5| Final Touches and Present | Incomplete

## Project Description

My final project is a movie database called 'Cinefavorites'. Users will be able to create a login and subsequently login, where they'll be able to add one of their favorite movies to a list of films. The user will be able to add a title, director, description, and image to each film. After adding the film, the dashboard will display the image and title of the film. Once the user clicks on the film, they'll see the image, title, and description of the film on a separate page. On the separate page, they'll be able to add the platforms that they can stream and/or download the film on. 

## Google Sheet

- [Link](https://docs.google.com/spreadsheets/d/1MiYUM5Rr0hr_9kbYVNgYzxu88jngsMA9udl1Ox-z7Vw/edit?usp=sharing)

## Wireframes

- [Backend Wireframe](https://res.cloudinary.com/dpjdvsigb/image/upload/v1600013611/project-4-assets/backend-wireframe_m9z8wp.jpg)


## Time/Priority Matrix 

- [MVP](https://res.cloudinary.com/dpjdvsigb/image/upload/v1600049665/project-4-assets/backend-mvp_tdx4ae.jpg)
- [Post MVP](https://res.cloudinary.com/dpjdvsigb/image/upload/v1600049665/project-4-assets/backend-post-mvp_zgrhcu.jpg)

### MVP/PostMVP
#### MVP

- Create and Login with JWT User Authentication
- Create, Read, Update, and Delete Movies
- Create, Read, and Delete Links
- One-to-many relationship between Users and Movies
- One to many relationship between Movies and Links

#### PostMVP 

- Add score to Movies model
- Rank Movies in database by score

## Functional Components
#### MVP
| Letter | Component | Priority | Estimated Time | Time Invested |
| --- | --- | :---: |  :---: | :---: |
| A | Project Setup | H | 1hr | -hr |
| B | Heroku Deployment| H | 1hr | -hr |
| C | API Models | H | 3hr | -hr |
| D | API Serializers | H | 2hr | -hr |
| E | API Views | H | 4hr | -hr |
| E | API URLs | H | 1hr | -hr |
| F | Authentication Models | H | 2hr | -hr |
| G | Authentication Serializers | H | 2hr | -hr |
| H | Authentication Views | H | 4hr | -hr |
| I | Authentication URLs | H | 1hr | -hr |
| J | API Testing and Debugging | H | 4hr | -hr |
| K | Authentication Testing and Debugging | H | 4hr | -hr |
| - | Total | - | 29hr | -hr |


#### PostMVP
| Letter | Component | Priority | Estimated Time | Time Invested |
| --- | --- | :---: |  :---: | :---: |
| A | Reviews Model | M | 1hr | -hr |
| B | Reviews Serializers | M | 1hr | -hr |
| C | Reviews Views | M | 1hr | -hr |
| D | Reviews URLs | L | 1hr | -hr |
| E | API (Reviews) Testing and Debugging | H | 2hr | -hr |
| - | Total | - | 6hr | -hr |

## Additional Libraries
- asgiref (3.2.10)
- dj-database-url (0.5.0)
- Django (3.1.1)
- django-heroku (0.3.1)
- gunicorn (20.0.4)
- psycopg2 (2.8.6)
- pytz (2020.1)
- sqlparse (0.3.1)
- whitenoise (5.2.0)

## Code Snippet


## Issues and Resolutions

#### SAMPLE
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier                  
**RESOLUTION**: Missing comma after first object in sources {} object
