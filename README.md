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
