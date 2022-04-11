# React + Django Full-Stack App

**Week 10: April 2022. Project #4 for General Assembly.**

_This project is a continuation of my previous MERN full-stack app, utilizing React and Django instead of React and Node/Express._

PlantPet - A full-stack web application for the plant obsessed, plant newbies, and aspiring plant parents. Track individual plant watering, add photos, and personalized plant care!


## Deployed Website

Hosted via Heroku: https://plantpet.herokuapp.com/


## Repositories
- PlantPet 2.0 React+Django full-stack app:
    - Front-end: https://github.com/angelafrancisco/plantpet-react-fe
    - Back-End: https://github.com/angelafrancisco/plantpet-django-be

- PlantPet 1.0 MERN full-stack app:
    - Front-End: https://github.com/angelafrancisco/plant-front-end
    - Back-End: https://github.com/angelafrancisco/plant-back-end


## Technology

- React
- HTML/CSS/SASS
- Django/Python


## User Stories

- Homepage shows app features and links to login or register an account.
    - _(Note: Currently user register/login not in production. Register/Login buttons will take you to the user dashboard.)_
- User can create a new account and login.
- User can add plants to their "My Plants" section, creating a name, adding plant type, image url, room name, window direction, and notes about plant.
- Once a plant is added, user can edit or delete plant.
- User can complete watering tasks in their "My Tasks" section, as they are auto-generated after creating a new plant.


## GA Project Requirements (MVP)

- A full-stack application (React and Django)
- MVC file structure: Models, Views, Controllers (Note: React is views)
- At least one model with full CRUD
- At least three react components, besides App.js
- Deployed online and accessible to the public via Heroku
- Two git repositories, one for backend and one for frontend
- A `README.md` file with explanations of the technologies used, the approach taken, unsolved problems, user stories, and notes
- Links to hosted and working apps

## Project Stretch Goals

- Wireframing (created via Figma)
- SASS
- Favicon/Logo
- Plant modals (add new plant / edit plant)
- Form dropdown menu
- React routing:
    - Homepage: `'/'`
    - Login: `'/login'`
    - Register: `'/register'`
    - User Dashboard: `'/dashboard'`


## Future Goals
These are additions I wasn't able to get to within project timeframe, but want to implement in the future:

- Responsive Design
- API: It was difficult to find a public plant API that worked for my project. Hoping to expand on this later on.
- Model Updates:
    - Plant:
        - default image
        - `pet_friendly = models.BooleanField` (possibly based on toxicity level)
        - `maintenance = ? ` (possibly based on hardiness)
    - Task (Water):
        - `schedule = ? ` (possibly based on drought/humidity resistance)
- Additional CRUD for User model:
    - Create new user
    - Update/Delete user account
    - User login/logout (username/password authentication)
- Search functionality for user added plants
- Upcoming Tasks React component
- User image upload via Cloudinary
- Sort plants and tasks by room name or a-z


## Credits

- Favicon and Logo 
    - [Favicon.io](https://favicon.io/emoji-favicons/potted-plant)
- Icons 
    - [FontAwesome](https://fontawesome.com/icons)
    - [Flaticon](https://www.flaticon.com/) via [Freepik](https://www.freepik.com) 
- Photos 
    - [Rainier Ridao](https://unsplash.com/@rainierridao?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
    - [Angèle Kamp](https://unsplash.com/@angelekamp?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/plants?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)