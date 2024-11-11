import urllib3
import logging
import pdb

logging.basicConfig(filename="scraper.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def get_web_page(url):
  pdb.set_trace()
  assert url != "", "You must include a url!"
  http = urllib3.PoolManager()

  print("Scrapping URL:", url)
  logging.info("Scrapping url:", url)
  
  response = http.request("GET", url)

  print("Response code:", response.status, response.reason)
  logging.info("Response code:", response.status, response.reason)
  print(response.data.decode("utf-8"))