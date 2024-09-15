# Postman Dog CEO API Collection
This repository contains a Postman collection for interacting with the Dog CEO API to extract and list individual dog breeds.

## Collection
The collection includes the following request:
"Get Dog Breeds": Makes a GET request to `https://dog.ceo/api/breeds/list/all` to retrieve a list of all dog breeds and their sub-breeds.

## Test Logic
The following tests are included in the Postman request:
1. Extract and List Dog Breeds 
2. Status Code Validation
3. Schema Validation
4. Data Validation Test 1: Check if the response contains the breed 'appenzeller'
5. Data Validation Test 2 : Check if the response status is 'success'
6. Additional Test scenario 1 : Check if the breeds list is not empty
7. Additional Test scenario 2 : Check if all breeds are in lowercase
   
## Steps to Use
1. Import the Postman collection JSON file into your Postman application.
2. Run the `Get Dog Breeds` request.
3. View the extracted list of dog breeds in the Postman console.

## Repository Link
https://github.com/Ajay5599/Rakuten/blob/main/Status%20code.postman_collection.json

# Sweet Shop Cypress Tests
1. Initialize npm and Install Cypress
   
2. Open Cypress
   Opened Cypress for the first time using `npx cypress open`.

3. Create Tests Structure
   Created a folder structure inside `cypress/integration` to organize tests.

4. Tests
   Created `basket.spec.js` file and wrote tests to:
   Add products to the basket.
   Verify all selected items are present in the basket.
   Verify the total price in GBP.
   Change the delivery type to Standard Shipping and verify the total price.
   Fill in details and click on checkout.

## CircleCI Configuration
1. Create CircleCI Configuration File
    Created a `.circleci` directory and added a `config.yml` file.
    Configured CircleCI to run Cypress tests.

2. Set Up CircleCI Project
   Added the GitHub repository to CircleCI.
   Verified that CircleCI automatically detects the `config.yml` file and runs tests.

## Test Logic
1. Add Products to the Basket
   Added different quantities of at least 4 products to the basket.
   Navigated to the basket page to verify the items.

2. Verify Items in the Basket
    Checked that all selected items are present in the basket using `cy.get().should('exist')`.

3. Verify Total Price
   Calculated the total price based on individual item prices and quantities.
   Verified the total price displayed on the website matches the calculated price.

4. Change Delivery Type and Verify Total Price
   Changed the delivery type to Standard Shipping.
   Verified the updated total price including delivery cost.

5. Checkout
   Filled in the checkout form with user details.
   Clicked on the checkout button to complete the process.

