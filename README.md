# SOXS E-commerce Platform

SOXS is an Asia-based specialist retailer of socks. Found in 2010 by Elizabeth Graham and Jennifer Greive, they started their first store in Singapore. Till date, the socks are sold in over 1,000 distribution stores across Asia. <br><br>
The store is looking to further the sales of the products by creating a online platform for their customers to make purchase. The wesbite is designed to meet the user experience and deployed in Heroku with the link below: <br><br>

## UX Design- User Stories
### Customer View
1) “I want to view the products from any device via my laptop or mobile device.”
2) “The interface must be simple and easy to use.”
3) “I want to view the products in category that I want.”
4) “I must be able to search products that I want using text search.”
5) “I want to filter the products by the price to look for the socks that is within my budget.”
6) “I want to make online purchase of the socks trhough secure payments.”

### Company Goals
1) “The company wants to build up the product branding by setting up a online platform.”
2) “The company wants to improve the product sales by allowing customers to make online purchase.”
3) “The company wants to collect contact details of customer so that the company can inform them of any new products or promotion.”

## Project Structure

### Wire Frame
The wireframe can be viewed in the link below:

### ER Diagram
The ER Diagram can be viewed in the link below:

## Project Skeleton

### Features

Page | Description
--- | ---
Top Navigation Bar | The navigation bar has the following items: <br><br> 1. **Company Logo** - *direct to the index page when customer click on it.* <br> 2. **About** - *direct to the About Us page.* <br>  3. **Category** - *Display 3 links, MEN, WOMEN and KIDS, when hover over. Customer can go to individual category when they click on the link.* <br> 4. **Shop** - *direct to the Show_Item page which displays all the socks for the customer to choose.* <br> 5. **Login** - *direct to the login page for users to log into their account. The Log in will change to Log out after the user login. User will log out their account when they click on the Log Out link.* <br> 6. **Search Icon** - *Search Textbox will be displayed when customer clicks on the icon. Customer can input the product name and press the Enter key to conduct the search.* <br> 7. **Cart Icon** -  *this icon will display the number of items that the customer added to the cart. Customer are direct to the View_Cart page to see their cart items.* <br><br>
Footer Bar | The footer bar has the following items:<br><br> 1. **About Us** - *A short Introduction on the Organisation and link to direct the customer to the About Us page with full details of the organisation.* <br> 2. **FAQ** - *direct to the FAQ page* <br> 3. **Privacy Policy** - *direct to the Privacy_Policy page* <br> 4. **Return & Refund** - *direct to Return_n_Refund page* <br> 5. **Terms & Condition** - *direct to Term_n_Condition page* <br> 6. **Company Contact Information** *such as Email, Contact Number and Address are shown here.* <br><br>
Index | This is the landing page. The **Shop Now** button in the middle of the page will direct the customer go to the show_item page to start their online shopping.  <br><br> There are also 3 links below, MEN, WOMEN and KIDS which allow the customer to go directly to the category of products without going through the entire product list. <br><br>
About |	This is the About Us page that introduce the Company to the customer. Full description such as Company History and Team members of the organisation are display here. <br><br>
FAQ	| This page display some of the frequent questions asked by the customer. This is display in the bootstrap feature and collapse feature. The answers will be displayed in the expanded views when customer click on the questions in the collapse view. <br><br>
Privacy_Policy | This page displays the Privacy Policy of the Company. <br><br>
Return_n_Refund	| This page displays the Return and Refund Policy of the Company. <br><br> 
Terms_n_Conditions | This page displays the Terms and Conditions of the Company. <br><br>
Show_Item | This page displays all the socks in the store. <br><br> Customers can filter the list of the socks by adjusting the price bar on the right side of the page. Only socks that fit in between price range set by the customer will be display. <br><br> In addition, customer can view the list by their category, MEN, WOMEN or KIDS. <br><br>
Create_Item	| This page let the staff of the store to add new products. Details like Product Name, Product Image, Color, Material, Size and Price are mandatory to fill in before the staff can add the item. <br><br>
Update_Item	| This page allows the staff of the store to amend or update the products details. <br><br>
Delete_Item	| This page alllows the staff to delete the products from the product list. <br><br>
View_Cart |	This page displays all the products that the customer added to the shopping cart. The product image, name and price will be display for individual item. Customer can change the quantity of the purchase. The sub total and grand total price will change accordingly to tell the user how much they need to pay for the purchase. <br><br> Customer can continue shopping for more products by clicking on the continue shopping button. <br><br> Once the customers are satisfy with their purchase, they will click on the checkout button to make payment. <br><br>
Checkout | This page is the payment page using Stripe Online Payment Platform. Customer will see the items and the amount that they will be paying. They will be able to pay through their credit card. <br><br>
Thankyou | After succesful payment, the customer will be directed to this Thank you page. <br><br>
Login |	This page allows the customer to log into their account using their username and password. There is a link for the new user to go to the Sign Up page to register their new account.There is also another link to the Password reset Page for User to reset their password. <br><br> The staff with administration account can log in using this log in page. After they log in , they will be able update and delete the product items. Normal user will not able to amend or the delete the products. <br><br>
Logout | After the user log in, the Log In link in the navigation bar will change to Log Out link. User can click on this link to log our their account. <br><br>
Sign Up | This page will allow customer without any account to sign up for one. They will receive news on the store latest Products and Promotion. <br><br> The store can build up their customer base using all the emails collected to promote their products. <br><br>
Password Reset | This page is Django default password reset page. User will be ale to reset their password when they enter their email address. <br><br>
Base | This is the template HTML containing the Navigation and the Footer page. All the rest of the pages inherient their Naviagtion and Footer from this Base HTML. <br><br>

### Features to implement in the future
1. I will like to add in the stock element so that staff do not need to keep track of the products stocks level. The staff will be prompt to replenish the stocks if there is no more stocks available.
2. I will like to add in virtual assistant to assist the customer on any queries and issue that they faced.
3. I will like to generate feature to generate self generate invoice for the customer.

## Project Surface
The theme that I wished to present is simple and user-friendly website as per the user requirement

### Colours
● **White and Blue** are main colors chosen for the website. <br>
● **White** - The White background is choosen so that the colourful socks image will stand out. <br>
● **Blue** - Blue Color is choosen to make the customer feel comfortable and at peace. Blue also subtle messages of trustworthiness and serenity, loyalty and tranquill. <br><br>

### Technologies Used
● <a href = "https://aws.amazon.com/cloud9/"> **Cloud9** </a> - The project was developed using Cloud9 Integrated Development Environment. <br>
● **HTML** - The project uses HTML to create the pages. <br>
● **CSS** - The project uses CSS to style the pages. <br>
● <a href="https://getbootstrap.com/">**Bootstrap**</a> - The project uses Bootstrap for styling and responsive design. <br>
● <a href="https://fonts.google.com/">**Google Fonts**</a> - The project uses Google Fonts to style the Fonts. <br>
● **JavaScript** - The project uses JavaScript for responsiveness. <br>
● **Python** - The project uses Python to write the websites logic. <br>
● **Django** - The project was built using the Django framework. <br>
● <a href="https://stripe.com/en-sg">**Stripe**</a> - The project uses Stripe for handling online payments. <br>
● <a href="https://uploadcare.com/">**Uploadcare**</a> - The project usess Uploadcare for uploading all the products images. <br>
● <a href="https://github.com/">**GitHub**</a> - The project uses GitHub as it's version control system. <br>
● <a href="https://id.heroku.com/login">**Heroku**</a> - The project uses the Heroku platform for hosting the website. <br><br>