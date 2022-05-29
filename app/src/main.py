from fastapi import FastAPI, Response, Request
from .generator import Generator
from .scraper import Scraper
from fastapi_utils.tasks import repeat_every

app = FastAPI()

@app.get("/")
async def root(token: str = ""):
    return Response("OK")

@app.get("/generate")
def generate():
    Generator.generate_synthea_patient()
    return 200

@app.post("/generate_receive/")
async def generate_receive(request: Request):
    request_json = await request.json()
    patients =  Generator.filter_synthea_response(request_json)
    return 200

@app.get("/scrape_addresses")
async def scrape_addresses(zip: str):
    return Scraper.scrape(zip)

@app.on_event("startup")
@repeat_every(seconds=60)  # 1 hour
def process_address_csvs_task() -> None:
    addresses = Scraper.process_address_csv()

    # print(request_json)
    # filenumber = 0
    # while exists(f'outfile{filenumber}.json') == True:
    #     filenumber += 1
    # with open(f'outfile{filenumber}.json', "w") as outfile:
    #     outfile.write(json.dumps(request_json))
