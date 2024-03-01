# Project Name: Virtual Currency Exchange Platform (VCEP)
A Web-based virtual currency exchange platform for the IST303 course:

![78](https://github.com/Ahmed5641/Virtual-Currency-Exchange/assets/157667926/f92fe1c5-eb96-4bd4-8883-fe53ffe8bdc4)

# Group 4:
<li>Ahmed</li>
<li>Ameya</li>
<li>Clement</li>
<li>Divya</li>


# Objective:
To create a web-based platform where users can simulate the experience of trading virtual currencies. The application will provide functionalities for currency conversion, tracking currency values, and managing virtual portfolios.

# Application Features:
### User Registration and Authentication:

1. Allow users to sign up and log in to their accounts.
2. Secure password storage and authentication process.
   
### Currency Conversion and Trading:
1. Enable users to convert between different virtual currencies.
2. Simulate buying and selling currencies with a virtual wallet.
   
### Real-time Currency Data:
1. Integrate with a third-party API to fetch real-time data on virtual currency values.
2. Display current rates and trends.

### Transaction History:
1. Track and display the history of user transactions and trades.
2. Include details like date, amount, currencies involved, and conversion rate.

### User Portfolio Management:
1. Allow users to view their current virtual currency holdings.
2. Display the current value of their portfolio based on live market rates.

### Interactive Dashboard:

1. A user-friendly dashboard showing currency trends, user portfolios, and recent transactions.
2. Visualization of currency trends over time.

# Project Stakeholders:
<li>Development Team</li>
<li>End Users</li>
<li>Digital currency traders</li>
<li>Other trading platforms</li>

# Project Requirements:
1. Python 3.12
2. Backend development using Flask
3. Frontend development using HTML, CSS, and JavaScript
4. Database integration with Flask-SQLAlchemy
5. Virtual Environment
6. API integration for real-time currency data
7. pytest

# User Stories:
1. As a user, I want to be able to register an account using my email and password.
2. As a user, I want to be able to log in to my account using my email and password to access my dashboard.
3. As a logged-in user, I want to access a dashboard that shows an overview of my account.
4. As a user, I want to view real-time currency exchange rates to make informed trading decisions.
5. As a user, I want to be able to buy virtual currencies at the current market rate.
6. As a user, I want to be able to sell virtual currencies at the current market rate.
7. As a user, I want to view my transaction history to track my past activities.
8. As a user, I want to see the current value of my portfolio, so that I know the performance of my investments.
9. As a user, I want to be able to communicate with other users.

# User Stories Completion Estimations:
### User Account Registration:
  ##### Estimated Time: 5 - 6 days

### User Login System:
  ##### Estimated Time: 5 - 6 days
  
### View Real-Time Currency Exchange Rates:
  ##### Estimated Time: 4 - 5 days

### Buy Virtual Currencies:
  ##### Estimated Time: 1 week

### Sell Virtual Currencies:
  ##### Estimated Time: 4 - 5 days

### View Transaction History:
  ##### Estimated Time: 4 - 5 days

### User Portfolio Value and Dashboard:
  ##### Estimated Time: 1 week

### User communication forum:
  ##### Estimated Time: 1 week

# Revised User Stories with Decomposed Tasks:
### 1. Register an Account:
#### Tasks:
   1. Designing database schema for user information. Ahmed
   2. Creating a registration form (User Interface). Divya
   3. Developing server-side logic to store user credentials securely. Ameya

### 2. Log in to Account:
#### Tasks:
   1. Designing and implementing login UI. Divya
   2. Developing backend logic authentication for session management and password handling. Clement
   3. Implementing password recovery mechanism. Ameya

### 3. User Dashboard Access:
#### Tasks:
   1. Designing the layout of the user dashboard. Clement
   2. Implementing backend logic to retrieve and fetch user data. Ahmed
   3. Implementing frontend components to display user information. Clement
   4. Developing a mechanism for editing user information. Ahmed

### 4. View Real-time Currency Exchange Rates:
#### Tasks:
   1. Integrating a third-party API for fetching real-time currency exchange rates. Ameya
   2. Designing UI components to display the rates. Ahmed

### 5. Buy Virtual Currencies:
#### Tasks:
   1. Designing a trading interface for a purchase form. Ahmed
   2. Implement purchase transactions including validations. Ameya

### 6. Sell Virtual Currencies:
#### Tasks:
   1. Designing a trading interface for a sell form. Ahmed
   2. Implement sell transactions including validations. Ameya

### 7. View Transaction History:
#### Tasks:
   1. Designing a page to list transactions.
   2. Implementing backend logic to retrieve transaction data.

### 8. View Portfolio Value:
#### Tasks:
   1. Designing UI to display portfolio value.
   2. Integrating portfolio value into the user dashboard.

### 9. Communicate with Other Users:
#### Tasks:
   1. Designing and implementing a messaging or forum feature.

 # Milestone 1.0 Features:
 ### 1. User Account Management:
 #### - Registration: 
   Users can create an account by providing their email and password.
#### - Login: 
   Users can log in to their accounts using their credentials.
#### - Dashboard Access: 
   Upon login, users are directed to their dashboard, displaying an overview of their account.

### 2. Real-time Currency Exchange Rates:
#### - Exchange Rate Viewing: 
   Users can view real-time exchange rates for various virtual currencies.

### 3. Basic Trading Functionality:
#### - Buying Virtual Currencies: 
   Users can buy virtual currencies at current market rates. This involves selecting a currency, specifying the amount, and executing the purchase.
#### - Selling Virtual Currencies: 
   Users can sell virtual currencies they own, based on current market rates.
   For Buying and Selling, Developing a chatroom where users can exchange cryptocurrency by engaging in chat, sharing insights, and securely posting and messaging their crypto wallet's public keys.


# Milestone 1.0
## Total Allocation:
### Total: 23 days (until 03/06/2024 when Milestone 1 is due)
#### User Account Management and Dashboard: 11 days.
#### Real-time Data and Basic Trading Functionality: 12 days.

## Iteration 1: User Account Management and Dashboard:
#### Duration: 11 workdays

11 working days (60% velocity) Days of actual work: 4 (Four Team Members) * 11 * 0.60 = 26 Days
#### 1. User Registration: 9 days
Designing and implementing the registration form and backend logic. (Ameya, Divya)
#### 2. Database Setup: 7 days
Designing a database for storing users information. (Ahmed, Clement)
#### 3. Login System: 6 days
Implementing login functionality with session management. (Ameya, Divya)
#### 4. Basic Dashboard: 4 days
Setting up a simple dashboard to display user profile information. (Ahmed, Clement)

![Iteration1](https://github.com/Ahmed5641/Virtual-Currency-Exchange/assets/157667926/ace14852-2704-4c74-89b3-6ec19b273e7a)

The Burndown Chart for iteration 1 will be updated regularly to show the actual work that has been done against the planned work.

## Iteration 2: Real-time Data and Basic Trading Functionality:
#### Duration: 12 workdays

12 working days (60% velocity) Days of actual work: 4 (Four Team Members) * 12 * 0.60 = 29 Days
#### 1. UI for data and trading functions: 4 days
Users can access the trading form through their dashboard or main home page. (Divya, Clement)
#### 2. Real-time Currency Exchange Rates Viewing: 8 days
Users can view real-time exchange rates for various virtual currencies through integrated API. (Ahmed, Ameya)
#### 3. Buying Virtual Currencies: 9 days
Users can buy virtual currencies at current market rates. This involves selecting a currency, specifying the amount, and executing the purchase. (Ahmed, Ameya)
#### 4. Selling Virtual Currencies: 8 days
users can sell virtual currencies they own, based on current market rates. (Ahmed, Ameya)

![Iteration2](https://github.com/Ahmed5641/Virtual-Currency-Exchange/assets/157667926/987a1672-1cf5-40b0-ae0c-885d968f20de)

The Burndown Chart for iteration 2 will be updated regularly to show the actual work that has been done against the planned work.










   



