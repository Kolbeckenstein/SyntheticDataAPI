from fastapi import FastAPI, Response, Request
import uuid, os, shutil
from starlette.responses import StreamingResponse
from dotenv import load_dotenv
from .generator import Generator
import docker

load_dotenv("../config/")

app = FastAPI()


@app.get("/")
async def root(token: str = ""):
    if token == os.getenv("SDAPI_PASSWORD"):
        directory_uuid = str(uuid.uuid4())
        synthea_dir = "../synthea/" + directory_uuid
        os.mkdir(synthea_dir)
        os.system(
            'cd ../synthea && ./run_synthea --exporter.baseDirectory  "'
            + directory_uuid
            + '"'
        )
        shutil.make_archive(synthea_dir, "zip", synthea_dir)

        s = open(synthea_dir + ".zip", "rb")

        resp = StreamingResponse(
            s,
            media_type="application/x-zip-compressed",
            headers={
                "Content-Disposition": f'attachment;filename={directory_uuid+".zip"}'
            },
        )

        os.system("rm -rf " + synthea_dir)
        os.system("rm " + synthea_dir + ".zip")

        return resp
    else:
        return Response("UNAUTHORIZED, KNAVE")

@app.get("/generate")
def generate():
    Generator.generate_synthea_patient()
    return 200


@app.post("/generate_receive/")
async def generate_receive(request: Request):
    print(await request.json())
    return 200

# docker run --rm --network=syntheticdatagenerator_default -e SYNTHEA_SIZE=1 -e FHIR_URL=http://172.19.0.2:80/generate_receive conceptant/synthea-fhir
# docker image remove --force synthetic-data-api && docker-compose up