<div style="text-align:center;height:5rem;">
<img src="https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/media/beetle_logo.png"></img>
</div>

# Fragile Art

Fragile Art is a website to showcase and sell the works of Jim Vickers an artist located in Sheffield.
He has previously worked with bands such as InMe, Dave McPhearson & Fei Comodo, alongside other projects for brands such as Acoda, Balance, Arkaik Clothing & many more.

## Table of Contents

1. [UX](#ux)
    - [Goals](#goals)
        - [Project Goals](#project-goals)
        - [Visitor Goals](#visitor-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#exisiting-features)

    - [Future Goals](#future-goals)

3. [Information Architecture](#information-architecture)
    - [Database Choice](#design-choice)
    - [Data Storage](#data-storage)

4. [Technology Used](#technology-used)

5. [Testing](#testing)

6. [Deployment](#deployment)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

8. [Disclaimer](#disclaimer)

# UX

## Visitor Goals

- Provide access to a portfolio of works for visitors to browse.
- Give potential clients a list of previous clients and their type of business.
- Allow customers the option to purchase items directly from the site.
- Give the user additional places to view more current WIP items through social media.
- Allow the visitor to be able to contact the artist easily and through a variety of methods.
- Allow the visitor to be able to create and account, add items to their basket and checkout when they have completed shopping.
- Allow the visitor to return to their basket if they leave and come back to the site.

### User Stories

#### User

- As a user i want to be able to see their portfolio and discover items i haven't seen before.
- As a user i want to be able to purchase items that i like.
- As a user i want to be able to shop with confidence and pay with my card directly not through a third party site.
- As a user i want to be able to contact the artist to discuss my own projects.
- As a user and potential client i want to be able to see their past collection of works and clients.
- As a user i want to be able to find social media links so i can follow the artists latest works.

#### Admin

- As an Admin i want to be able to add products easily.
- As an Admin i want to be able to manage orders in a simple and easy manner.
- As an Admin i want to be able to upload to my portfolio easily.

#### Developer

- As a developer i want to ensure the user can't break the flow of the site with correct defensive design choices.
- As a developer i want to ensure an authenticated user can access all required information correctly.
- As a developer i want to include options for the admin to quickly edit the site.


### Design Choices

#### Fonts

The artist has request that the site use [Playfair Display](https://fonts.google.com/specimen/Playfair+Display) as they feel this best suits their work and style they want to achieve.

As a secondary font i have chosen to use [Montserrat](https://fonts.google.com/specimen/Montserrat) to compliment this and allow for the extra content to stand out from the rest of the site content.

#### Colours

The client has specified #323e48 as their desired choice but has said they would allow anything to go with this as long as it contrasted well with the main colour choice.

With this information i have chosen to use the following colours to provide a great contrast and to help the content stand out.

<div style="text-align:center;height:5rem;">
<img src="https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/media/colours.png"></img>
</div>

#### Styling

### Wireframes

#### Desktop

- [Splash Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-desktop-Splash.png)
- [Portfolio Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-desktop-portfolio.png)
- [Store Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-desktop-store.png)
- [Store Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-desktop-product.png)

#### Tablet

- [Splash Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-tablet-splash.png)
- [Portfolio Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-tablet-portfolio.png)
- [Store Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-tablet-store.png)
- [Store Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-tablet-product.png)

#### Mobile

- [Splash Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-mobile-splash.png)
- [Portfolio Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-mobile-portfolio.png)
- [Store Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-mobile-store.png)
- [Store Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-mobile-product.png)

## Features

### Exisiting Features

#### Portfolio

The portfolio section provides the artist a platform to add his works to the site and gives the user the chance to view all his current and past works in one place, each item has a description and a look at who the client for project was.

If the item is also available for sale then the user can also add this to their shopping cart.

#### Clients

The clients section of the site allows the user and potential new clients to see an overview of previous clients and in what field they operate also pointing the user to get in touch with the artist with regards to their own potential projects

#### Store

The store will provide the user the oppertunity to purchase any available products directly from the web page and this was previously handled through a third party site.

The user is able to add multiple items to the cart and either securely checkout in their current session or the items can be held until the user returns to the site later.

Payment is handle on the site and keeps the user in the same loop without having to redirect to a third party site.

#### Contact

The contact page allows the user a variety of methods to contact the artist in relation to either new potential clients or with regards to queries related to existing orders, potential orders or stock queries.

### Future Goals

## Information Architecture

### Data Storage

#### User Table

| Title            | Key In Database | Form Validation | Data Type |
|------------------|-----------------|-----------------|-----------|
| Account id       | _id             | No Validation   | Primary Key  |
| Username         | username        | string max length 20 | CharField |
| Password         | password        | hashed min length 8 | CharField |
| E-mail Address   | email           | Must contain @ & .com etc | Email |
| House Number     | house           | Max Digits 6 | NumField |
| Street Address   | street_address1 | string max length 100 | string    |
| Street Address 2 | street_address2 | string max length 100 | string    |
| County/State     | county          | string max length 100 | string    |
| Postal Code      | post_code       | string max length 8 | string    |
| Contact Number   | tel             | Number max length 15 | string    |
| Country          | country         | pycountry select  | Option    |

#### Products Table

| Title              | Key In Database | Form Validation | Data Type |
|--------------------|-----------------|-----------------|-----------|
| Product Id         | _id             | No Validation   | Primary Key  |
| Product Name       | prod_name       | string max length 100 | CharField |
| Product Fancy Name | prod_fancy      | string max length 100 | CharField |
| Has Size           | size            | False Default   | Boolean |
| Sizes Available    | sizes           | string max length 4 | CharField |
| Colour             | colour          | string max length 20 | string |
| Price              | price           | Max Digits 6 Decimal Places 2 | Decimal Field |

#### Orders Table

|     Title    | Key In Database |    Form Validation    |  Data Type  |
|:------------:|:---------------:|:---------------------:|:-----------:|
| Order Id     | _id             | No Validation         | Primary Key |
| Username     | username        | text                  | Foreign Key |
| Address 1    | address_line_1  | string max length 100 | CharField   |
| Address 2    | address_line_2  | string max length 100 | CharField   |
| Town/City    | town_or_city    | string max length 100 | CharField   |
| County/State | county_or_state | string max length 100 | CharField   |
| Postcode     | postcode        | string max length 8   | CharField   |
| Country      | country         | country select        | Option      |
| Order Date   | order_date      | datetime.date.today   | DateField   |
| Paid         | paid            | False default Stripe  | Boolean     |

## Technology Used

### Languages

- HTML
- CSS
- Javascript
- [Python](https://www.python.org/)

### Frameworks

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

### Libraries
- [Jquery](https://jquery.com/)
- [Sweet Alert](https://sweetalert2.github.io/)
- [Stripe Payments](https://stripe.com/)

## Testing

No automated testing has been used on this project, i have opted to do all testing manually and through numerous user experiences.

### UI


1. Navigation
    - Hovering over each link has the desired response from the nav bar
    - *portfolio* takes the user to the portfolio and all items display as expected
    - *store* navigates the user to the store and all items display correctly
    - *clients* takes the user to the clients page with all items displaying correctly
    - *contact* takes the user to the contact page with the form displaying as expected
    - *sign-in* produces the sign in form and the user can either navigate to create an account or create an account and logs the user in
    - *Sign-out* removes the user from the session and returns
    - User can add items to the *cart* calculations work as expected.

### Functionality

1. *Portfolio*
    - Items display correctly and any added to the database automatically are added to the DOM
    - Rollover information is displayed as expected

2. *Store*
    - Items all displaying correctly with correct price and category of each item
    - On click the user is taken to the products specific page
    - User can choose a quantity and add to the cart
    - Correct information is passed to the cart with images and all relevent information

3. *Clients*
    - All client information is displayed with images as expected.

4. *Contact*
    - User is able to complete the contact form and submit.
    - User is presented with a thank you message to confirm result.

5. *Login/log out*
    - User is able to log in when logged out and retrieve their party.
    - When user is logged in and selects log out the username is removed from the session correctly.

6. *Shopping Basket*
    - User is able to see their current cart total from the navigation bar.
    - User is able to add items to the cart from the store
    - Multiple lines are displaying correctly.
    - User can edit the quantity of the Cart or delete when needed

7. *Checkout*
    - User is able to complete the billing form with their information.
    - If the user has default delivery information this is autocompleted.
    - User can complete the purchase using 4242 4242 4242 4242 42/42 42424
    - User is presented with an order confirmation.
    - Confirmed orders are viewable in the users profile.

### Responsive Design

1. *Mobile*
    - All pages tested on Android and current iOS platforms and returns as expected.
    - No overflow seen in testing and all information is displayed correctly.
    - Navbar is working as collapse menu working as expected.

2. *Tablet*
    - All pages testing in Chrome dev tools
    - All Loading as expected with no overflow seen
    - Navbar responding correctly

3. *Desktop*
    - Tested with Safari & Chrome
    - All items load as expected
    - Navbar working and displaying correctly
    - No overflow issues experienced
    - All items in correct positioning.

### Bugs

---
* Problem: Confirmation e-mail link produces a 404 error.
* Cause: The environmental variable isn't configured correctly.
* Resolution: adding an initial / to the env path allows the confirmation e-mail to work correctly.
---
* Problem: Custom AllAuth templates not loading
* Cause: Base template no correctly being referenced.
* Resolution: removing allauth from the templates file and reinstating fixed this issue.
---
* Problem: Application won't deploy.
* Cause: A migration file was deleted accidently and hadn't been commited to GitHub
* Resolution: The only sure fire way i found to fix this was to 'nuke' the database on the server, delete all local migration files and run all migrations again and reimporting all fixtures.
---

### Unresolved Issues

## Deployment

Below is an example of how to deploy this site locally based on using *VsCode IDE*, deploying to Heroku using *Amazon S3* for hosting of static and media files. This will allow the site to deploy automatically with commits to the master branch. The code can also be run locally.

### Deployment Requirements

- [VScode](https://code.visualstudio.com/) IDE Local development tool
- [python](https://www.python.org/downloads/) Documentation is based on Python v3.7.7
- PIP package installer
- [AWS-S3](https://aws.amazon.com/s3/) Web based cloud storage
- [Stripe](https://stripe.com/gb) Payment infrastructure

### Deploying Locally

1. Clone a copy of the repository by clicking code at the top of the page and selecting 'Download Zip' when this has downloaded, extract the files to your folder of choice.
   Alternatively if you have git installed on your client you can run the following command from the terminal 

   ```bash
   git clone https://github.com/D0nni387/FragileArt.git
   ```

1. Open us your local IDE (For this example we will be using VScode as linked in the requirements) and open the working folder.

1. Ideally you will want to work within a virtual environment to allow all packages to be kept within the project, this can be installed using the following command (please note some IDE's require pip3 instead of pip, please check with the documentation for your chosen IDE)

```bash
pip install virtualenv
```

1. To install the virtual environment within the project folder run the following command.

```bash
python -m .venv .env (the .env can be replaced by your folder name of choice)
```

1. To activate the virtual environment navigate to the below dir and run activate.bat

```bash
[folderinstalled]\scripts\activate\activate.bat
```

1. Next we need to install all modules required by the project to run, use the follow

```bash
pip install -r requirements.txt
```

1. Create a new folder within the root dir called .vscode and a file inside called settings.json. Within this file add the following lines to set up the environmental variables.

```bash
{
    "git.ignoreLimitWarning": true,
    "python.pythonPath": ".env\\Scripts\\python.exe",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": ["--load-plugins=pylint_flask"],
    "files.autoSave": "onFocusChange",
    "terminal.integrated.env.windows": {
      "SECRET_KEY": "[Your key]",
      "DEV": "1",
      "HOSTNAME": "0.0.0.0",
      "PORT": "5000",
      "STRIPE_PUBLIC_KEY": "[Your Key]",
      "STRIPE_SECRET_KEY": "[Your Key]",
      "DEBUG": "True",
    }
  }
```

### Database setup

1. To set up your database you will first need to run the following command

```bash
python manage.py migrate
```

1. To create a super user to allow you to access the admin panel run the following command in your terminal and complete the required information as prompted

```bash
python manage.py createsuperuser
```

1. From there you should now be able to run the server using the following command

```bash
python manage.py runserver
```

1. If everything has been correctly configure you should not get a message giving you a link to your locally hosted site usually at http://127.0.0.1:8000

1. Next close the server in your terminal using ctrl+c (cmd+c on mac) and run the following commands to populate the database

```bash
python manage.py loaddata store/fixtures/categories.json
python manage.py loaddata store/fixtures/products.json
python manage.py loaddata clients/fixtures/clients.json
```

### Deploying to Heroku

To run this application in an online environment you will need to deploy the code to *Heroku*.
Before moving on to this section please ensure you have followed the instructions for local deployment and this has been successful

1. Either create an account at [Heroku](https://www.heroku.com/) or log in to your account
1. Set up a new app under a unique name
1. In the resources section, in the addons field type the below command and select the free cost option

```bash
heroku Postgres
```

1. in the settings tab select Reveal Config Vars and copy the pre populated DATABASE_URL into your settings.py file in your project
1. in the Config Vars in Heroku you will need to populate with the following keys

|          Key          |     Value    |
|:---------------------:|:------------:|
| AWS_ACCESS_KEY_ID     | [your value] |
| AWS_SECRET_ACCESS_KEY | [your value] |
| SECRET_KEY            | [your value] |
| STRIPE_PUBLIC_KEY     | [your value] |
| STRIPE_SECRET_KEY     | [your value] |

1. Now this has been configured you will now migrate the local database to the cloud database using the migrate command as below

```bash
python manage.py migrate
```

1. Next you will need to create a super user and populate the database as described in the database set up section
1. When the migrations and data has been loaded, in your *Heroku* dashboard select the Deploy tab
1. From here select the Github option and connect the repository from GitHub and select the branch (Master) to deploy from.
1. It is advised to select automatic deployment to ensure for each push to Github the hosted version is up to date.
1. When this has deployed select open app from the top bar of the *Heroku* App.

## Credits

### Content

### Media

All images have been provided by Jim Vickers to aid in the development of this project.

### Acknowledgements

- [Simen Daehlin](https://github.com/Eventyret) - (mentor) for his invaluable input, advice & support
- Jim Vickers

## Disclaimer

All images & content used for this site are for educational purposes only.