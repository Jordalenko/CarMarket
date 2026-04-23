# CarMarket
[Link to deployed site](https://car-market-9069020e42dd.herokuapp.com/)
<hr>
CarMarket is a full stack e-commerce project allowing users to post listings with their vehicle for sale. The project was built using the Django framework for the backend and HTML, CSS, Bootstrap and JavaScript on the frontend. CarMarket allows the users to create an account and perform CRUD functionality on their profile and listings. This project was created as part of Code Institute's Level 5 Web Development course.

![CarMarket Image](./assets/readme-images/CarMarket_main_image.png)

# Table Of Content

-   [User Experience](#user-experience)
    -   [User Stories](#user-stories)
    -   [Site Goals](#site-goals)
    -   [Scope](#scope)
-   [Design](#design)
    -   [Colour Scheme](#colour-scheme)
    -   [Database Schema](#Database-Schema)
    -   [Fonts](#Fonts)
    -   [Wireframes](#Wireframes)
    -   [Agile Methodology](#Agile-Methodology)
         -   [Overview](#overview)
         -   [EPICS(Milestones)](#epicsmilestones)
         -   [User Stories issues](#user-stories-issues)
         -   [MoSCoW prioritization](#moscow-prioritization)
         -   [GitHub Projects](#github-projects)
-   [Features](#features)
    -   [Navbar](#Navbar)
    -   [Footer](#Footer)
    -   [Home](#Home)
        -   [Hero Section](#hero-section)
        -   [Search Form](#search-form)
        -   [Recent Listings](#recent-listings)
        -   [Listing Card](#listing-card)
    -   [Listings Page](#listings-page)
    -   [Create Listing](#create-listing)
    -   [Profile Page](#profile-page)
    -   [My Listings](#my-listings)
    -   [My Favourites](#my-favourites)
    -   [Remove From Favourites](#remove-from-favourites)
    -   [Edit Listing](#edit-listing)
    -   [Delete Listing](#delete-listing)
    -   [View Listing](#view-listing)
    -   [User account and User account listings](#user-account-and-user-account-listings)
    -   [Sign In Page](#sign-in-page)
    -   [Sign Up Page](#sign-up-page)
    -   [Sign Out Confirmation](#sign-out-confirmation)
    -   [Edit Profile](#edit-profile)
    -   [Delete Profile Confirmation](#delete-profile-confirmation)
    -   [We are sorry to see you go](#we-are-sorry-to-see-you-go)
    -   [Password reset](#password-reset)
    -   [Password reset email sent](#password-reset-email-sent)
    -   [Enter a new password](#enter-a-new-password)
    -   [Password Reset Completed](#password-reset-completed)
    -   [Error Pages](#error-pages)
-   [Future Features](#future-features)
-   [Testing](#testing)
-   [Bugs](#Bugs)
-   [Technologies And Languages](#technologies-and-languages)
    -   [Languages Used](#languages-used)
    -   [Python Modules](#python-modules)
    -   [Technologies and programs](#technologies-and-programs)
-   [Deployment](#deployment)
    -   [Before Deployment](#before-deployment)
    -   [Deployment on Heroku](#deployment-on-heroku)
    -   [Creating A Fork](#creating-a-fork)
    -   [Cloning Repository](#cloning-repository)
-   [Credits](#credits)
    -   [Media](#media)
    -   [Code](#code)
    -   [Acknowledgements](#acknowledgements)
    -   [Comments](#comments)


## User Experience

### User Stories

1. As a developer I can set up a new Django project so that I can create the project's structure.
2. As a developer I can connect database and media storage so that the user's stored data is stored successfully
3. As a developer I can deploy the application early so that I can confirm that the initial setup is working and can continue testing the application during development.
4. As a developer I can create wireframes so that the layout of the website is clear for desktop and mobile
5. As a user I want the website to be responsive so I can view it on my mobile
6. As a user I want to be able to register an account so that I can have access to all functionality of CarMarket.
7. As a registered user I want to be able to log in to my account so I can view my profile page.
8. As a registered user I want to be able to see my profile page so that I can update my information.
9. As a registered user I want to be able to reset my password so that I can regain access to my account in case I forget my password.
10. As a registered user I want to be able to delete my profile if I do not wish to use the services of CarMarket.
11. As a user, I want to be able to see the most recent listings on the landing page so that I can quickly and easily discover the latest items available for sale
12. As a user I want to be able to see details about the listing such as a description and image so that I can find suitable car options and make informed decisions before I contact the seller.
13. As a user I want to be able to easily navigate through pages of listings so that I can view all the listings in an organised way (pagination)
14. As a site owner I want to ensure that the user is prompted with a notification message when performing CRUD operations or login/logout, and signup so that the user is informed about the outcome of the action taken
15. As a registered user I want to be able to send messages to the seller of the listing so that I can arrange viewings and ask questions about the listing. (Won't Have)
16. As a registered user I want to be able to view any messages I may have received so that I can keep track of communication with the seller. (Won't Have)
17. As a registered user I want to be able to reply to messages so that I can connect with the seller. (Won't have)
18. As a User I can navigate through the website so that I can access different sections efficiently
19. As a user I can visit the home page so that I can quickly browse and find relevant car listings based on my preferences
20. As a non-authenticated user, I want to access the listings, so that I can **view cars for sale.
21. As a registered user I want to be able to send emails to the seller so that I can arrange viewings and ask questions about the listing.
22. As the site administrator I want to be able to add listings. (Won't Have)
23. As the site administrator I want to be able to view all my listings. (Won't Have)
24. As the site administrator I want to be able to edit my listings. (Won't Have)
25. As the site administrator I want to be able to delete my listings. (Won't Have)

### Site Goals

1. To provide the users with a place to browse for cars.
2. To provide a range of available cars for sale to potential buyers.
3. To provide a place for the users to browse vehicles by brand, features and price range.
4. To make the website available and functional on every device.

### Scope
The project aims to develop an online car listing platform called "CarMarket" that facilitates users in viewing vehicle listings. The platform will be responsive and user-friendly, providing features for user registration, profile management and seamless navigation.

Key Features:

1. Initial Project Setup:

- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.

2. Responsive Design:
-The website will be responsive, allowing users to access it on desktop and mobile devices.

3. User Authentication:
- Users can register an account, providing access to all functionality of CarMarket.
- Registered users can log in to view their profile, listings, and favorites.

4. Profile Management:
- Registered users can view and edit their profiles, including personal details and profile pictures.
- Users can reset their passwords in case they forget them.
- Users can delete their profiles and associated listings.

5. Listing Management:
- Admin users can perform CRUD on the listings with vehicles for sale.
- The most recent listings will be displayed via a prominent link on the landing page.
- Listings will include details, descriptions, images, and a button to purchase from the site admin.

6. Pagination:
- Pagination will be implemented for easy navigation through pages of listings.

7. Notification Messages:
- Users will receive notification messages when performing CRUD operations, login/logout, and signup actions.

Benefits:

1. User-Centric Experience: The platform focuses on the user's needs, allowing efficient browsing, purchase and communication.
2. Efficient Navigation: Users can easily navigate through different sections of the website for seamless access.
3. Effective Communication: Sending messages and notification messages features, enhance user communication and interaction.

## Design
### Colour Scheme
The website features a calming and professional color palette that combines shades of blue, violet, and green with complementary neutrals. <br>
Overall, this color scheme creates a professional and user-friendly environment, with subtle variations in hue and transparency to guide users' attention and enhance the visual appeal of the website.
![Colour Scheme](./assets/readme-images/)

### Database Schema
![database schema](./assets/readme-images/CarMarket_db_schema_v4.png)

#### Models
1. Allauth User Model

The User model is part of Django Allauth. The model comes with predefined fields as standard. Some of them are username, email, name, password, and more. This model is used for user authentication, hence why changes directly to this model are not advisory. The User model is connected to the Profile model with one to one relationship. 

2. Profile Model

The Profile model is a custom custom-created model to handle the user profile details. Signals are used to reflect the changes between the User and Profile models. For example, if the Profile gets updated or deleted the changes will apply to the user model as well. 

3. Listing Model

The listing model is connected to the Profile with a ForeignKey field - owner. It is furthermore connected to the CarMake and CarModel models via ForeignKey field again

4. CarMake Model

This Model was created to store all of the car brands (car make) in the database 

5. CarModel Model

This model was created to store all of the car models in the database. It is connected to the CarMake model via ForeignKey field - car_make

6. Favourites

This model was created to store all of the favourite listings for each Profile. The model is connected to Listing and Profile models via ForeignKey fields - listing and owner.

### Fonts
The font used in this project is the default font. <br>


### Wireframes
- Home
![Home](./assets/readme-images/wireframes/Home.png)
- Listings
![listings](./assets/readme-images/wireframes/Listings.png)
- Single listing
![single-listing](./assets/readme-images/wireframes/Listing.png)
- Log in
![login](./assets/readme-images/wireframes/Login.png)
- Profile
![profile](./assets/readme-images/wireframes/Profile.png)

### Agile Methodology
#### Overview
This project was created using agile principles. This was a big learning curve together with my very first full-stack project. Using the agile approach allowed me to plan all the features of the website through user stories. Each user story has acceptance criteria and tasks to clearly outline the requirements for each feature to be completed.

#### EPICS(Milestones)
The user stories are grouped into eight EPICS or Milestones. An additional Milestone called Project Backlog was created to manage any additional features, bugs, or tasks that may arise during development. <br>


#### User Stories issues
The structure of the user story issue consists of the user story, acceptance criteria, and tasks that outline the steps that are required for this issue to be completed. <br>

During development where possible, the commit messages are connected to their corresponding issues. <br>
![User Story](./assets/readme-images/user_stories/user-story-commits.PNG)

#### GitHub Projects
The project was created using a basic Kanban Board structure, divided into columns such as Todo, In Progress, Done, and Backlog. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow. <br>
![User Story](./assets/readme-images/github-projects.PNG)

## Features
### Navbar
The navbar is a component that is present on all pages. It was created using Bootstrap and is fully responsive. The CarMarket logo which serves as a link to the homepage is located on the left side on the navbar. On the right are the nav links which allow the user to easily navigate through the website from any point. If the user is not authenticated the links displayed are Home, Listings, and Login/Signup.


 If the user is authenticated they will see Home, Listings, Create Listing, Profile, and Logout. The profile link will have the user's username displayed to indicate that the user is logged in. For a better user experience, each nav link when active is underlined with a border to let the user know the page they are currently on.


 ### Footer
 The footer consists of information about CarMarket and their contact details. To help the users connect with CarMarket there are icons with links to social media which open in a new tab. 


### Home
#### Hero Section
The choice of hero image for the website serves a specific purpose: it immediately communicates the main purpose of the website. The text overlay, "Find Your New Car," directly connects the image to the website's purpose. It encourages users to take action and search for their ideal vehicle, making the website's primary function clear right from the start. The high-end car image was carefully selected to create an immediate and powerful connection between the user and the website's mission, inviting them to explore the website further.

#### Search Form
The search form allows the users to select via multiple filters like keywords, town, county, fuel type, year, and price. 
The view that handles the search form on the back end, pulls all of the listings from the database and then applies all the filters from the user's request. The results are passed to the listings page which also has the same search form at the top. The search parameters are preserved within the form for a better user experience.

#### Recent Listings
This section displays the six most recent listings added to the system.

#### Listing Card
The listing card is designed to present to the user the most important information about the listing. 
The card consists of a title, location, time ago posted, year, miles, price, and a button for more info. The card and the button are links to the single listing page.


### Listings Page
The listings page consists of the same search form as the home page. Further down are displayed all the listings starting from the most recent ones. Once the user applies filters from the search form the results are refined based on the filter applied. Six cards per page are displayed followed by pagination to allow the user to easily navigate through multiple pages of listings. The pagination works well with search results as well.


### Create Listing
This page can be accessed only by authenticated users. It provides the user with a listing creation form. During the planning process, the initial idea was to try and connect to an external API to fetch the car details based on the reg plate, however, all of the available APIs are paid. This is a future feature I would like to add. Implementing this will save time for the user and they won't have to fill out this very long form which will improve the user experience. Another idea to make the form more user-friendly was to break it into sections and make it dynamic. The only reason this wasn't completed was due to the timeframe for the project's deadline. 
The form fields limit wrong user input as much as possible by implementing select elements with drop-down options and using regex validation. The car model field is dynamically populated by using JavaScript and making a call to the back end. The model field is then populated with the appropriate options based on the car make selection. This helps to prevent users from creating listings with wrong details. Django widget tweaks was used to render the form in a more user-friendly version. The required fields are indicated by the * symbol after each label.
The Images section consists of 1 main image and six additional images. The main image input field is indicated so that the user can easily select the best possible main image for the card listing.


### Profile Page
This page can be accessed only by authenticated users. It consists of a sidebar menu with links for Profile, My Listings, and My favourite listings. 
The profile page is essentially a large card that includes the user's profile image and details like name, user name, email, and about me. Underneath, there are two buttons one for edit profile and one for delete profile.


#### My listings
This page shows all of the listings that were created by this user. The cards have additional buttons for editing and deleting listings which allows each user to easily manage their listings. Maximum of 6 listings per page display and then pagination will appear at the bottom to help the user navigate through their listings.


#### Edit Listing
This page displays the same form as create a listing, with already populated fields with the current details of the listing. The user can amend all of the details on the page and upload new images or just save the form as it is. Once submitted the user is redirected to my listings page.


#### Delete Listing
When the user visits my listings page they can delete listings using the delete button on each card, which redirects the user to confirmation page. The page consists of a warning message and two buttons - one to go back and one to delete listing, which is in red colour to clearly indicate danger.  Once the user confirms, the listing is deleted. The user is then redirected to my listings page.


#### View Listing
This button leads to the single listing page. 
On the top left, there is a button to go back. Since this page can be accessed from multiple places, the path for a step back cannot be a link to a specific URL. This is why this button brings the user one step back. Below the button is the images section consisting of one large image and up to 6 smaller images below. To display the images in a more user-friendly way Lighbox2 was used. The button can easily navigate through the images with the buttons on the side.

Below that a description of the listing can be found. On the right side of the listing is where the most important information is presented to the user in a user-friendly manner. 
The listing's title (consisting of the car make and car model) followed by the price and then how long ago was this listing created.
Below that the relevant specifications are displayed, and by using icons the information is visually structured better.
If the user visits a listing that is not theirs there is a heart that they can click to save the listing into their favourites the action is clearly communicated with a flash message and the heart changing to a red heart. If the user clicks the heart again, they will remove the listing from favourites and will get a flash message letting them know that.



Further down there is a card with the seller's details, consisting of their image, name, email, phone, and location if added. Their image is a link to their user account page. Below that is an email seller button which when clicked opens a modal with a form. The form is prepopulated with the user's details if they are authenticated. Once submitted, an email is sent to the listing's owner with the details within the form. 
![contact form](./assets/readme-images/features/)
![contact email](./assets/readme-images/features/)


#### User account and User account listings
This page renders other user's profiles. It has a very similar layout to my profile page with a few small changes. There are no favourites links in the sidebar menu. The profile page does not have edit and delete buttons as users should only be able to amend their profile pages. The link for my listings shows all of the listings this user has created. The cards display with a view button only.

![user account](./assets/readme-images/features/)

![user account listings](./assets/readme-images/features/)

### Sign In page
Consist of a form with username and password. Below it has a link to reset password, followed by a sign in button which submits the form. The register link is position below that.


### Sign Up page
Consists of a form with name, email, username, password, and password confirmation. Below it has a link to log in if the user already has an account. Below that is the signup button. The user is sent a welcome email to the email provided and is redirected to the profile page update form to customize their profile


### Sign out confirmation
When the user clicks on the log out link in the nav, they are redirected to the confirmation page. This page consist of warning message and two buttons- one to go back and one to log out.


### Edit Profile
The edit profie page renders a form with prefilled fields with the existing information for this user. It consists of profie image, name, username, email, phone, town, county and about me section. Below that is the submit button which will update the profile details once submitted. 


### Delete Profile Confirmation
This page consists of warning message with two buttons - one to go back and one to delete the profile. Delete profile is in red to indicate danger. Once clicked the profile is deleted and the user is redirected to We are sorry to see you go page

### We are sorry to see you go
This page confirms that the profile was deleted. The user is presented with a flash message confirming the profile was deleted successfully. Below that there is a button to go back to the home page.


### Password reset
This page prompts the user to enter their email address. An email with instructions is then sent to their email and the user is redirected to a page that informs them about the email being sent.


### Password reset email sent
This page informs the user an email with instructions has been sent.


Email with instructions


### Enter a new password
When the user follows the link from the email, they are sent to a page to set up their new password.

![pass reset new pass](./assets/readme-images/features/)

### Password Reset Completed
Once the form is submitted the user is redirected to a page advising them the password reset was completed followed by a log-in button.

![pass reset completed](./assets/readme-images/features/)

### Error Pages
- 404

- 403

- 500




## Future Features
1. I would like to add a single-listing.html page to the listings app.
2. Each listing will have unique images
3. I would like to expand the application by adding email features and the option for the users to send and reply to messages.
4. 

## Testing
Testing documentation can be found [here.](./TESTING.md)
## Bugs

|Bug|Status|
| ---| ---|


## Technologies And Languages
### Languages Used
- HTML
- CSS
- JavaScript
- Bootstrap
- Python
- Django
- Django Rest Framework

### Python Modules
- Boto3 is the Amazon Web Services (AWS) SDK for Python. It allows to interact with AWS services, such as S3

- dj-database-url - This library is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.

- django-resized - This package provides utilities for resizing images in Django. 

- gunicorn - Gunicorn is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

- Pillow - Pillow is a Python Imaging Library (PIL) fork that provides tools for working with images in various formats.

- psycopg2 - Psycopg2 is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.


- whitenoise - Whitenoise is a middleware for serving static files directly from your Django application.

### Technologies and programs
 - [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Git](https://git-scm.com/) was used as a version control software to commit and push the code to the GitHub repository.
- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used as a starting point for the project.
- [Pixelmator Pro](https://www.apple.com/uk/pixelmator-pro/) was used for creating the mockup images of the website during planning stage.
- [Google Fonts](https://fonts.google.com/) was used to import fonts.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used during the testing of the website.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging and making the website responsive.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Js Hint](https://jshint.com/) was used to validate the JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.
- [Online Convert](https://image.online-convert.com/convert-to-webp) used to convert images to webp format
- [Coolors.co](https://coolors.co/) was used to display the colour scheme.
- [Box Shadow Generator](https://cssgenerator.org/box-shadow-css-generator.html) was used to generate the shadows

## Deployment
### Before Deployment
To ensure the application is deployed correctly on Heroku it is mandatory to update the requirements.txt. This is a list of requirements that the application needs in order to run.

- To create the list of requirements we use the command pip3 freeze > requirements.txt. This will ensure the file with the requirements is updated.
- Then commit and push the changes to GitHub.

! Before pushing code to GitHub ensure all credentials are in an env.py file, which is included in the .gitignore file. This tells Git not to track this file which will prevent it from being added to Github and the credentials being exposed.
### Deployment on Heroku
- To deploy the project on Heroku, first create an account.
- Once logged in, create a new app by clicking on the create app button
- Pick a unique name for the app, select a region, and click Create App.
- On the next page select the settings tab and scroll down to Config Vars. If there are any files that should be hidden like credentials and API keys they should be added here. In this project, there are credentials that need to be protected. This project requires credentials added for:
1. Django's secret key
2. Database Credentials
3. Cloudinary access key 
3. Cloudinary secret key
- Scroll down to Buildpacks. The buildpacks will install further dependencies that are not included in the requirements.txt. For this project, the buildpack required is Python
- From the tab above select the deploy section.
- The deployment method for this project is GitHub. Once selected, confirm that we want to connect to GitHub, search for the repository name, and click connect to connect the Heroku app to our GitHub code.
- Scroll further down to the deploy section where automatic deploys can be enabled, which means that the app will update every time code is pushed to GitHub. Click deploy and wait for the app to be built. Once this is done, a message should appear letting us know that the app was successfully deployed with a view button to see the app.
### Creating a fork
1. Navigate to the [repository](https://github.com/Dayana-N/CarMarket-PP4)
2. In the top-right corner of the page click on the fork button and select create a fork.
3. You can change the name of the fork and add description 
4. Choose to copy only the main branch or all branches to the new fork. 
5. Click Create a Fork. A repository should appear in your GitHub

### Cloning Repository
1. Navigate to the [repository](https://github.com/Dayana-N/CarMarket-PP4)
2. Click on the Code button on top of the repository and copy the link. 
3. Open Git Bash and change the working directory to the location where you want the cloned directory. 
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.
## Credits
### Media
- The images for the listing were pruned from a figma dataset [deepvisualmarketing](https://deepvisualmarketing.github.io/). They are for display purpose only.

### Code
- Learned how to setup django project and deploy to Heroku from CI Django Blog walkthrough 
- [How to create dependant drop down](https://github.com/akjasim/cb_dj_dependent_dropdown) The code was later refactored to use Django Rest Api
- [The Car models list is from (kaggle.com)](https://www.kaggle.com/datasets/abdulmalik1518/cars-datasets-2025) 
- [Pagination fix for multiple search parameters](https://stackoverflow.com/questions/46026268/pagination-and-get-parameters)
- [How to catch email sending exceptions](https://stackoverflow.com/questions/41457565/how-to-catch-email-sending-exceptions-in-django-1-10)
### Acknowledgements
- Huge thank you to my mentor Frank for helping me prune down my very ambitious idea to a trim MVP for my first full-stack project.
- The Discord community and especially Steve Powell who listened to my struggles during development.

### Comments
This project consists of two apps - Listings, and Users. 
The User's app handles everything related to the users. 
The Listings app handles everything related to the listings including CRUD functionality for the administrator of the site who would be selling the cars.
The API app was created to serialize the data and pass it to the front end. In particular the car models. On the front end, JavaScript makes a call to fetch all the models based on the user's selection of car make. 
The car makes and models were loaded into the database by calling a function in the enrich_csv_with_make_model_ids.py file. The code loops over all of the car models in the cars dictionary and uploads them to the database. This function should not be called otherwise. It has been left there to document the process. 
The .csv was converted to a fixture using convert_csv_to_json.py. It required much back and forth with my tutor to fine tune the code to take the non-utf-8 excel doc and parse all the records into the database.

I wanted to include some automated testing, but unfortunately i ran out of time. However, this is something I plan to add in the future to help me manage the project as I keep adding more features.

This project is particularly close to my heart, not only because it's my very first full-stack project but also because it's inspired by my love for cars. 