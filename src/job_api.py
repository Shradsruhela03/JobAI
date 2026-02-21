from apify_client import ApifyClient
import os
from dotenv import load_dotenv
load_dotenv() 

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))  # Initialize the Apify client with the API token from environment variable








# for apify i am creating func
# first fetch linkedin jobs based on search query and location and then return the data to caller function
def fetch_linkedin_jobs(search_query, location="india",rows=60):
    run_input = {
        "title": search_query,
        "location": location,
        "rows": rows,
        "proxy":{
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"]
            }
       
    }
    run=apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs=list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs



# naukri jobs
def fetch_naukri_jobs(search_query, location="india",rows=70):
    run_input = {
        "keyword": search_query,
        "maxjobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
        
        
       
    }
    run=apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
    jobs=list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs
    