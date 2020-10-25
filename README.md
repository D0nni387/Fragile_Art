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

- As a user i want to be able to add products easily.
- As a user i want to be able to manage orders in a simple and easy manner.
- As a user i want to be able to upload to my portfolio easily.

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

- [Splash Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-desktop-splash.png)
- [Portfolio Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-desktop-portfolio.png)
- [Store Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-desktop-store.png)
- [Product Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-desktop-product.png)

#### Tablet

- [Splash Tablet](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-tablet-splash.png)
- [Portfolio Tablet](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-tablet-portfolio.png)
- [Store Tablet](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-tablet-store.png)
- [Product Tablet](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-tablet-product.png)

#### Mobile

- [Splash Mobile](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-mobile-splash.png)
- [Portfolio Mobile](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-mobile-portfolio.png)
- [Store Mobile](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-mobile-store.png)
- [Product Mobile](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa-mobile-product.png)

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
| First Name       | first_name      | string max length 20 | CharField |
| Last Name        | last_name       | hashed min length 8 | CharField |
| E-mail Address   | email           | Must contain @ & .com etc | Email |
| Street Address   | default_street_address1 | string max length 128 | string  |
| Street Address 2 | default_street_address2 | string max length 128 | string  |
| City Or Town     | default_city_town     | string max length 128 | string  |
| County/State     | default_county_state      | string max length 64 | string  |
| Postal Code      | default_postcode_zi      | string max length 12 | string  |
| Contact Number   | default_telephone_number | Number max length 20 | string  |
| Country          | country         | pycountry select  | Option    |

#### Products Table

As the brief for the project requires a portfolio and seperate store one table is created to ensure data isn't stored twice and can be
user by both components

| Title              | Key In Database | Form Validation | Data Type |
|--------------------|-----------------|-----------------|-----------|
| Product Id         | _id             | No Validation   | Primary Key  |
| Product Name       | name            | string max length 254 | CharField |
| Product Category   | category        | string max length 100 | CharField |
| Price              | price           | Max Digits 6 Decimal Places 2 | decimal field  |
| Client             | client          | No validation | CharField |
| description        | description     | No validation | CharField |
| tools              | colour          | No validation | CharField |
| is sold            | is_sold         | Default True | Boolean Field |
| sale_type          | sale_type       | string max length 20| Decimal Field |
| image              | image           | Null True Blank True | Image Field |

#### Orders Table

|     Title    | Key In Database |    Form Validation    |  Data Type  |
|:------------:|:---------------:|:---------------------:|:-----------:|
| Order Number | order_number    | No Validation         | Primary Key |
| User Profile | user_profile    | text                  | Foreign Key |
| First Name   | first_name      | string max length 100 | CharField   |
| Last Name    | last name       | string max length 100 | CharField   |
| email        | email           | string max length 100 | CharField   |
| telephone Number | telephone_number | string max length 20 | CharField   |
| street address 1| street_address1 | string max length 100 | CharField   |
| street address 2 | street_address2 | string max length 100 | CharField   |
| City Town    | city_town       | string max length 100 | CharField   |
| County/State | county_state | string max length 100 | CharField   |
| Postcode Zip | postcode_zip    | string max length 8   | CharField   |
| Country      | country         | country select        | Option      |
| Order Date   | order_date      | datetime.date.today   | DateField   |
| Total Order   | total_order      | max digits 10   | Decimal Field   |
| Delivery Charge | delivery_charge | max digits 5   | decimal Field   |
| Grand total  | grand_total     | max digits 10 | Decimal Field    |

#### Clients Table

| Title         | Key in Database | Form Validation | Data Type  |
|---------------|-----------------|-----------------|------------|
| name          | name            | max length 128  | CharField  |
| Friendly name | friendly_name   | max length 254  | CharField  |
| business type | Business Type   | max length 50   | CharField  |
| Description   | description     | None            | TextField  |
| image         | image           | None            | ImageField |

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
- [PopperJS](https://popper.js.org/)]

## Testing

No automated testing has been used on this project, i have opted to do all testing manually and through numerous user experiences.

- <strong>Implementation</strong> 🏭:
When i had set up the products fixtures and loaded into the database i could then view all saleable items in the store, i wanted to ensure all products loaded as expected and that item information was visable when selected.

- <strong>Test</strong> 🧪:
To test this, I went through each item and loaded the products information page, then looked at changing the url to ensure each item was loading correctly

- <strong>Result</strong> 🏆:
All products loaded as expected to the main store page, some items were missing their images but they were still selectable and loaded their page correctly. When amending the url all items again loaded as expected however if i tried to access an item id that didn't exist i was presented with a 404 page.

- <strong>Verdict</strong> ✅:
This test passed in it's basic form, amendments are required to the fixtures to ensure all the items images load correctly, also as the 404 page is the generic template provided with Django creating a custom page to handle these errors is desireable.

---

- <strong>Implementation</strong> 🏭:
As with the store the portfolio page is populated from all items even if they aren't saleable. i need to ensure these load correctly to their specific pages and the overlays work correctly.

- <strong>Test</strong> 🧪:
To test this, I went through each item and loaded the portfolio item information page, then looked at changing the url to ensure each item was loading correctly

- <strong>Result</strong> 🏆:
All portfolio items again populated the main page correctly, some with missing images and when clicked presented their specific pages with information displaying correctly.

- <strong>Verdict</strong> ✅:
This test was deemed to be a pass, some minor edits are needed to the fixtures to ensure when the items are loaded out of development branches they are displaying as expected.

---

- <strong>Implementation</strong> 🏭:
As a user can purchase items without signing in, i wanted to ensure that an order can be completed from start to finish.

- <strong>Test</strong> 🧪:
To test this i will select items at random and add them to the basket and proceed through checkout.

- <strong>Result</strong> 🏆:
Items were added to the basket correctly and the totals calculated as expected, going through the checkout process i was able to complete the order with stripes debug card ref and the order was confirmed and added to the db correctly.

- <strong>Verdict</strong> ✅:
This test completed as expected without bugs.

---

- <strong>Implementation</strong> 🏭:
With a logged in user, i want to make sure the user can view previous orders through the users account page.

- <strong>Test</strong> 🧪:
To test this i created a new user and proceeded to add items to the basket and complete the checkout process.

- <strong>Result</strong> 🏆:
As expected the checkout process completed and upon checking the users account page i could see the order details. upon completing multiple orders i was able to view these in a list as designed

- <strong>Verdict</strong> ✅:
This test completed as expected without bugs, it did flag a minor style change needed to the account page but information was present.

---

- <strong>Implementation</strong> 🏭:
To ensure the user can navigate the site as expected i need to test each view and link to ensure the user isn't 'lost' within the page.

- <strong>Test</strong> 🧪:
This test will be carried out by systematically navigating to each page from the previous and all links are clicked until all checked.

- <strong>Result</strong> 🏆:
Each page and link was checked and each provided a positive result, at no point was the user sent to an unexpected destination.

- <strong>Verdict</strong> ✅:
This test passed and no amendments were required.

---

- <strong>Implementation</strong> 🏭:
To test the responsiveness of the site, the page was loaded on local mobile devices to check design choices

- <strong>Test</strong> 🧪:
This test was carried out by loading the site and navigating to each page and adding and completing an order with more than one item

- <strong>Result</strong> 🏆:
Each page loaded and displayed correctly, an issue was found with the basket which caused the table to overflow the edge of the page.

- <strong>Verdict</strong> ✅:
This test was classed as a fail and upon rereading the code a redesign of the basket was required to ensure mobile users were presented with the correct information that could be easily read.

### Bugs

---
* Problem 🐞: Confirmation e-mail link produces a 404 error.
* Cause: The environmental variable isn't configured correctly.
* Resolution: adding an initial / to the env path allows the confirmation e-mail to work correctly.
---
* Problem 🐞: Custom AllAuth templates not loading
* Cause: Base template no correctly being referenced.
* Resolution: removing allauth from the templates file and reinstating fixed this issue.
---
* Problem 🐞: Application won't deploy.
* Cause: A migration file was deleted accidently and hadn't been commited to GitHub
* Resolution: The only sure fire way i found to fix this was to 'nuke' the database on the server, delete all local migration files and run all migrations again and reimporting all fixtures.
---
* Problem 🐞: Images when uploaded were not being displayed.
* Cause: When the S3 bucket was enabled static files were not being served correctly.
* Resolution: on checking the img tag urls each file was being referenced incorrectly, each was required to reference the store.product.image.url instead of store.product.image
---

### Unresolved Issues

The only known but that is still present in the site is that the user can remove the max limit on the quantity by removing the flag in the html using Dev tools, should this site go live and used, a different solution would need to be found on the backend to ensure this can't be submitted.

## Deployment

Below is an example of how to deploy this site locally based on using *VsCode IDE*, deploying to Heroku using *Amazon S3* for hosting of static and media files. This will allow the site to deploy automatically with commits to the master branch. The code can also be run locally.

### Deployment Requirements

- [VScode](https://code.visualstudio.com/) IDE Local development tool
- [python](https://www.python.org/downloads/) Documentation is based on Python v3.8
- PIP package installer
- [Stripe](https://stripe.com/gb) Payment infrastructure

### Deploying Locally

1. Clone a copy of the repository by clicking code at the top of the page and selecting 'Download Zip' when this has downloaded, extract the files to your folder of choice.
   Alternatively if you have git installed on your client you can run the following command from the terminal.

   ```bash
   git clone https://github.com/D0nni387/FragileArt.git
   ```

1. Open us your local IDE (For this example we will be using VScode as linked in the requirements) and open the working folder.

1. Ideally you will want to work within a virtual environment to allow all packages to be kept within the project, this can be installed using the following command (please note some IDE's require pip3 instead of pip, please check with the documentation for your chosen IDE)

```bash
pip install pipenv
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
pipenv install -r requirements.txt
```

1. Create a new folder within the root dir called env.py. Within this file add the following lines to set up the environmental variables.

```bash
import os

os.environ["SECRET_KEY"] = "[Your Secret Key]"
os.environ["DEV"] = "1"
os.environ["HOSTNAME"] = "0.0.0.0"
os.environ["STRIPE_PUBLIC_KEY"] = "[Your Stripe Key]"
os.environ["STRIPE_SECRET_KEY"] = "[Your Stripe Secret Key]"
os.environ["DATABASE_URL"] = "[Your DB URL]"
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