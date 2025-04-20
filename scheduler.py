import schedule
import time 
from run_etl import run_etl

# Scheduler gets weather_data for every hour from the Open Weather API and performs the etl process
schedule.every().hour.do(run_etl)

print("Scheduler started job, extracting data every hour")

while True:
    schedule.run_pending()
    time.sleep(60)


