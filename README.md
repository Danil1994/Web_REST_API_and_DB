Install
Put command in your CLI 'git clone https://github.com/Danil1994/Web_REST_API_and_DB.git'
Install dependencies 'pipenv install --dev'

Activate this project's virtualenv, run 'pipenv shell'
Create .env file like .env.example and write path to the data and DB.
(Folder 'example folder' contain data to example. Also, you may put the way to this folder)

Run your application.
Create test data, use 'entrypoint.py' file.

work link: http://127.0.0.1:5000/apidocs

Test ability of this project by link http://127.0.0.1:5000/apidocs

/api/v1/report - full report
/api/v1/report/drivers - short report
/api/v1/report/drivers/{driver_abbr} - report about onr driver

You may choose preferred format json/xml
You may choose ascending order or descending order


Simple web application.

I developed a web application using REST API and SQLite database, leveraging my
own Python package. The package, which I designed and implemented, enhances the 
functionality and efficiency of the application. Additionally, I wrote 
comprehensive unit tests to ensure the reliability and stability of the codebase.
The application, built with technologies like Python, Swagger, and Flask, 
provides various features such as generating reports and retrieving information 
about drivers. It supports multiple data formats, including JSON and XML, and 
delivers formatted responses based on user preferences. I successfully created 
a robust and user-friendly web app with efficient data handling capabilities,
reinforced by the usage of my custom package and a strong focus on test-driven
development.