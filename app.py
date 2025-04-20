import streamlit as st
import requests
import datetime 
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
# passanger count
passenger_count = st.number_input("Number of Passengers", step =  1)
st.write(passenger_count)

#date and time of the ride
date = str(st.date_input("when your Taxi ride?!", datetime.date(2024, 5, 14)))
time  = str(st.time_input("Number of Passengers", datetime.time(8, 45)))

date_and_time = 'Your ride is on :' + ' '+ date + ' ' + time

#date_and_time = datetime.datetime.strptime(date_and_time, '%Y/%m/%dT%H:%M:%S')
st.write(date_and_time)

#pickup Location 
pickup_longitude = st.number_input("Enter the pickup longitude Number:")
pickup_latitude = st.number_input("Enter the pickup latitude Number:")
st.write("the pickup Location:", (pickup_longitude, pickup_latitude))

#dropoff Location 
dropoff_longitude = st.number_input("Enter the  dropoff longitude Number:")
dropoff_latitude= st.number_input("Enter the dropoff latitude Number:")
st.write("the dropoff Location:", (dropoff_longitude, dropoff_latitude))

parms = {'pickup_datetime':date_and_time,
         'pickup_longitude':pickup_longitude,
         'pickup_latitude':pickup_latitude,
         'dropoff_longitude' : dropoff_longitude,
         'dropoff_latitude' : dropoff_latitude,
         'passenger_count': passenger_count
         }

res = requests.get('https://taxifare.lewagon.ai/predict', params = parms)
st.write(res.json())
