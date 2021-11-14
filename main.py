from fastapi import FastAPI, Response, Depends
import uuid
import os
import zipfile
import io
import shutil
from starlette.responses import StreamingResponse

app = FastAPI()

@app.get("/")
async def root(token: str = ""):
    if token == os.getenv('SDAPI_PASSWORD'):
        directory_uuid = str(uuid.uuid4())
        synthea_dir = "../synthea/" + directory_uuid
        os.mkdir(synthea_dir)
        os.system("cd ../synthea && ./run_synthea --exporter.baseDirectory  \"" + directory_uuid + "\"")
        shutil.make_archive(synthea_dir, 'zip', synthea_dir)

        s = open(synthea_dir + ".zip", "rb")

        resp = StreamingResponse(s, media_type="application/x-zip-compressed", headers={
            'Content-Disposition': f'attachment;filename={directory_uuid+".zip"}'
        })

        os.system("rm -rf " + synthea_dir)
        os.system("rm " + synthea_dir + ".zip")

        return resp
    else:
        return Response("UNAUTHORIZED, KNAVE")
