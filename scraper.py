
#Packages needed for authentication
import httplib2 as lib2 #Example of the "as" function
from oauth2client import client #Importing a sub-package

#Packages needed for connecting with Google API
from googleapiclient.discovery import build as google_build #An example with all the statements together

#Data processing packages

import json
from datetime import datetime, timedelta #importing multiple sub-packages from one package


ACCESS_TOKEN = "<your access token>"
REFRESH_TOKEN = "<your refresh token>"
CLIENT_ID = "<your client id>"
CLIENT_SECRET = "<your client secret>"

#This is consistent for all Google services
TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'

#We are essentially setting the expiry date to 1 day before today, which will make it always expire
TOKEN_EXPIRY = datetime.now() - timedelta(days = 1)

#¯\_(ツ)_/¯
USER_AGENT = 'my-user-agent/1.0'



def createAnalyticsReport():

    #The real code that initalized the client
    credentials = client.GoogleCredentials(access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN,
                                           client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                           token_uri=TOKEN_URI, token_expiry=TOKEN_EXPIRY,
                                           user_agent=USER_AGENT)
    #Initialize Http Protocol
    http = lib2.Http()

    #Authorize client
    authorized = credentials.authorize(http)

    #API Name and Verison, these don't change until
    #they release a new API version for us to play with.
    api_name = 'analyticsreporting'
    api_version = 'v4'

    #Let's build the client
    analytics = google_build(serviceName=api_name, version=api_version, http=authorized)
    return analytics

def getResponse(analytics, start_date, end_date, view_id):
    sample_request = {
          'viewId': str(view_id),
          'dateRanges': {
              'startDate': str(start_date),
              'endDate': str(end_date)
          },
          'metrics': [
            {'expression': 'ga:users'},
            {'expression': 'ga:newUsers'},
            {'expression': 'ga:sessions'},
            {'expression': 'ga:sessionsPerUser'},
            {'expression': 'ga:pageviews'},
            {'expression': 'ga:pageviewsPerSession'},
            {'expression': 'ga:avgSessionDuration'},
            {'expression': 'ga:bounceRate'},
          ]
        }
    response = analytics.reports().batchGet(
          body={
            'reportRequests': sample_request
          }).execute()
    parsed = response["reports"][0]["data"]["totals"][0]["values"]
    return parsed
