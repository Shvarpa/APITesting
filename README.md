# Project Management Course - HM 3
### presented by: Lior Vaknin, Pavel Shvarchov, Mordi Dabah

In this Project we used two API:
Link to the API: https://ipapi.co/developers,
				 https://domainsdb.info
				 
## First Feature:
Find the location of the domain of an email address
Input: A valid email from the user
Output: Finds the domain of the email and find it’s IP address (using socket library).
and then find the location of the ip using the first API.
			
## Second Feature:
Check validation of an email address.
We are using the second API to check if the domain of the email address from the user exist.
This is one of the criterions for a valid email.
Input: An email address from the user.
Output: If the email is valid the feature will return true. False otherwise.
	
## How to install:
```
python -m pip install pipenv
pipenv install
```
#### Tests:
```
pipenv run python -m unittest discover tests
```