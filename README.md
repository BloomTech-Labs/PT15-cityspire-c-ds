# CitySpire - Data Science

[Docs](https://docs.labs.lambdaschool.com/data-science/)

## Mission

Be a one-stop resource for users to receive the most accurate city information.

## Description

An app that analyzes data from cities such as populations, cost of living, rental rates, crime rates, park (walk score), and many other social and economic factors that are important in deciding where someone would like to live. This app will present such important data in an intuitive and easy to understand interface.

Use data to find a place right for you to live.


(provide FastAPI image and info on API endpoints)
![alt text](cityspire-c-ds/cityspire.png/cityspire.png?raw=true)


## Data Engineering

FastAPI app, [deployed to AWS](http://cityspire-c-ds.eba-p3pw36sj.us-east-1.elasticbeanstalk.com/),
provides 3 primary routes:

- `/cityspire` is a GET route that provides all of the data in the database in a table format.
- `/locations` is a GET route that provides a list of all cities in the database.
- `/location/data` is a POST route that takes a request of location in the form of "City, State" and returns all of the data about that location.


| Type | Endpoint | Required Parameters | Returns |
| ---- | -------- | ---------- | ------- |
| GET  | /cityspire  | none | "[[0, 0, \"Akron, Ohio\", 197597.0, 678.0, 1782.0, 27.0, 181.0, 328.0, 1246.0, 6568.0, 1686.0, 4305.0, 577.0, 65.0, 8484.440553247267, 46, 46, 90.8, 7972.779227752733], ...]" |
| GET | /locations | none | { "locations": ["Akron, Ohio", "Albany, New York", ...] }|
| POST | /location/data/ | "location": "City, State" | {
  "city_name": "El Paso, Texas",
  "population": 681728,
  "rent_per_month": 990,
  "walk_score": 41,
  "livability_score": 12687
} |

[TODO]
More details about the API endpoints can be found at the
[ReDoc](https://blahblahblah.herokuapp.com/redoc) interface or by
exploring the interactive [SwaggerUI](https://blahblahblah.herokuapp.com).

## Machine Learning

Nearest Neighbors ML Model for CitySpire City Living Recommendations

The data wrangling and merging and can be found in the wrangling.ipynb notebook, while the tokening and TFIDF vectoring of text, creation of Nearest Neighbors model, training on tokenized and vectorized text, and pickling of Nearest Neighbors Model and TFIDF Vectorizer can all be found in the rec_modeling.ipynb notebook in the notebooks directory.

The Nearest Neighbors and TFIDF Vectorizer pickles can be found in the pickles directory.

The pickled Nearest Neighbors model and TFIDF Vectorizer are imported into recommend.py in the app directory so that they can be used in a recommend function in the Data Engineering API in order to recommend cities to live in to users based on desired population, rental rate, crime rate, walkability score, cost of living index, and livability score.

## Deployment

The CitySpire API is backed by a Postgres DB in AWS RDS. The data was uploaded to the DB using the df_to_sql.py script in the notebooks directory.

After you create your own PG DB on AWS RDS you need to add the DB URL to a .env file:

`DATABASE_URL=postgresql://DBusername:DBpassword@blah.blah.blah.us-east-1.rds.amazonaws.com/dbname`

Commands to deploy locally:

Create virtual environment in root directory of project:
`pipenv shell`

Install project dependencies in virutal environment:
`pipenv install --dev`

Launch app locally:
`uvicorn app.main:app --reload`

Launch app locally on different port:
`uvicorn app.main:app --reload --port 8080`


The API app is deployed to AWS Elastic Beanstalk using a Dockerfile. **It is crucial to organize all of the app directories into the app directory because the Dockerfile copies the app structure from the app directory, not the root directory of this repo.**

[Documentation on how to set up AWS and EB CLI](https://docs.labs.lambdaschool.com/data-science/tech/aws-elastic-beanstalk#deploy-the-first-time)

Commands to deploy to Elastic Beanstalk:

Commit your work:
`git add --all`
`git commit -m "Your commit message"`

Then use these EB CLI commands (Elastic Beanstalk command line interface) to deploy. (Replace CHOOSE-YOUR-NAME with your own name.)
`eb init --platform docker --region us-east-1 CHOOSE-YOUR-NAME`
`eb create --region us-east-1 CHOOSE-YOUR-NAME`

Do you have environment variables? Then [configure environment variables in the Elastic Beanstalk console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-softwaresettings.html#environments-cfg-softwaresettings-console).

Now you can open your deployed app! 🎉
`eb open`

Commands to redeploy to Elastic Beanstalk:

Commit your work:
`git add --all`
`git commit -m "Your commit message"`

Then use these EB CLI commands (Elastic Beanstalk command line interface) to re-deploy.
`eb deploy`
`eb open`

It is also possible to redeploy without committing your work with these commands:
`git add .`
`eb deploy --staged`


# Contributors

| John Dailey | Neha Kumari  | Theda | Mickey Wells |
| :---------: | :--------: | :--------: | :----------: |
| Data Scientist | Data Scientist | Data Scientist | Data Scientist |
| [<img src="https://github.com/favicon.ico" width="15">](https://github.com/johnjdailey) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/johnjdailey/) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/Neha-kumari31) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/neha-kumari-3325ba40/) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/LambdaTheda) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/MickeyLeewells2020/) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/) |
