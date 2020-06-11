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
#### Visitor Goals

- Provide access to a portfolio of works for visitors to browse.
- Give potential clients a list of previous clients and their type of business.
- Allow customers the option to purchase items directly from the site.
- Give the user additional places to view more current WIP items through social media.
- Allow the visitor to be able to contact the artist easily and through a variety of methods.
- Allow the visitor to be able to create and account, add items to their basket and checkout when they have completed shopping.
- Allow the visitor to return to their basket if they leave and come back to the site.

#### User Stories

- As a visitor i want to be able to see their portfolio and discover items i haven't seen before.
- As a visitor i want to be able to purchase items that i like.
- As a visitor i want to be able to shop with confidence and pay with my card directly not through a third party site.
- As a visitor i want to be able to contact the artist to discuss my own projects.
- As a visitor and potential client i want to be able to see their past collection of works and clients.
- As a visitor i want to be able to find social media links so i can follow the artists latest works.
- As an Admin i want to be able to add products easily.
- As an Admin i want to be able to manage orders in a simple and easy manner.
- As an Admin i want to be able to upload to my portfolio easily.

### Design Choices

#### Fonts

The artist has request that the site use [Playfair Display](https://fonts.google.com/specimen/Playfair+Display) as they feel this best suits their work and style they want to achieve.

As a secondary font i have chosen to use [Montserrat](https://fonts.google.com/specimen/Montserrat) to compliment this and allow for the extra content to stand out from the rest of the site content.

#### Colours

The client has specified #323e48 as their desired choice but has said they would allow anything to go with this as long as it contrasted well with the main colour choice.

With this information i have chosen to use the following colours to provide a great contrast and to help the content stand out.

#D9D9D9 #C5DCDD

<div style="text-align:center;height:5rem;">
<img src="https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/media/colours.png"></img>
</div>

#### Styling

### Wireframes

#### Desktop
- [Splash Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa_desktop_Splash.png)
- [Portfolio Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa_desktop_portfolio.png)
- [Store Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa_desktop_store.png)

#### Tablet
- [Splash Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa_tablet_splash.png)
- [Portfolio Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa_tablet_portfolio.png)
- [Store Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa_tablet_store.png)

#### Mobile
- [Splash Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa_mobile_splash.png)
- [Portfolio Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa_mobile_portfolio.png)
- [Store Desktop](https://raw.githubusercontent.com/D0nni387/Fragile_Art/master/wireframes/fa_mobile_store.png)


## Features

### Exisiting Features

### Future Goals

## Information Architecture

### Data Storage

#### User Table
| Title            | Key In Database | Form Validation | Data Type |
|------------------|-----------------|-----------------|-----------|
| Account id       | _id             | No Validation   | ObjectId  |
| Username         | username        | Text            | string    |
| Password         | password        | hashed          | string    |
| E-mail Address   | email           | text            | string    |
| House Number     | house           | text            | string    |
| Street Address   | street_address1 | text            | string    |
| Street Address 2 | street_address2 | text            | string    |
| County/State     | county          | text            | string    |
| Postal Code      | post_code       | text            | string    |
| Contact Number   | tel             | Number          | string    |
| Country          | country         | text            | string    |

#### Products Table

| Title              | Key In Database | Form Validation | Data Type |
|--------------------|-----------------|-----------------|-----------|
| Product Id         | _id             | No Validation   | ObjectId  |
| Product Name       | prod_name       | Text            | string    |
| Product Fancy Name | prod_fancy      | text            | string    |
| Has Size           | size            | Boolean         | Boolean   |
| Sizes Available    | sizes           | text            | string    |
| Colour             | colour          | text            | string    |
| Price              | price           | text            | string    |

#### Orders Table



## Technology Used

### Languages

HTML
CSS
Javascript
Python

### Frameworks

Django
Bootstrap

## Testing

### Validators

### UI

### Functionality

### Responsive Design

### Issue & Resolutions

### Unresolved Issues

## Deployment

Lots of text here about doing things!

## Credits

### Content

### Media

All images have been provided by Jim Vickers to aid in the development of this project.

### Acknowledgements

- [Simen Daehlin](https://github.com/Eventyret) - (mentor) for his invaluable input, advice & support
- Jim Vickers
## Disclaimer

All images & content used for this site are for educational purposes only.