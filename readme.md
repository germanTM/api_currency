_____________________
Project description

api_currency is an RESTful APi to manage transactions and get the exchange rate and fee charge between two currencies.

The api was developed in Flask to achieve an easy deployment.

The exhange module is contained in the app folder.
Each of the parts of the exchange module were divided in controllers, services and models to let us expand our api as much as we want with the desired modularity to maintain the quality and organization of the project.

To make the project flexible and organized it was implemented a blueprint arquitecture to register each developed module in their own separated environment.

Also swagger was implemented to maintain the documentation of the endpoints that are developed.
______________
Installation

First of all, you should make a virtual environment

$virtualenv env

Then, activate it with

$source env/bin/activate

Now, to install the project dependencies you can run the command make install

$make install

___________
Run

To deploy the project, you should enter to any debugger tool available on your editor, then start debugging and then automatically is going to make the necessary steps to deploy the project.
The port changes each time the project is deployed this way so to run the services the URL should be localhost/{{port}}
If the deployment worked correctly, it is going to redirect you to your browser, directly to the swagger file with the documentation.

_______________
REST API

The REST API is described below

Get exhcange rate and fee charge

Request
    -POST /getFeeAndRate

    {
        "from_currency":"USD",
        "to_currency":"CAD",
        "evaluate_amount":10.1
    }

Response
    -HTTP/1.1 201 OK
    -Status 201 OK
    -Content-Type: application/json

    {
        "exchange_rate": 1.103, 
        "fee_amount":0.01
    }

The REST API is described below

Get exhcange rate and fee charge

Request
    -POST /exchange/transaction

    {
        "from_currency":"USD",
        "to_currency":"CAD",
        "exchange_amount":190
    }

Response
    -HTTP/1.1 201 OK
    -Status 201 OK
    -Content-Type: application/json

    {
        "exchange_rate": 1.103, 
        "fee_amount":0.01,
        "accumulated_fee_over_base": 0.01
    }

