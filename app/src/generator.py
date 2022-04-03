# shutil.make_archive(synthea_dir, "zip", synthea_dir)

# s = open(synthea_dir + ".zip", "rb")

# resp = StreamingResponse(
#     s,
#     media_type="application/x-zip-compressed",
#     headers={
#         "Content-Disposition": f'attachment;filename={directory_uuid+".zip"}'
#     },
# )

# os.system("rm -rf " + synthea_dir)
# os.system("rm " + synthea_dir + ".zip")

import docker


class Generator:
    def generate_synthea_patient():
        client = docker.from_env()
        client.containers.run(
            "conceptant/synthea-fhir",
            auto_remove = True,
            network="syntheticdatagenerator_default",
            environment={
                "SYNTHEA_SIZE": 1,
                "FHIR_URL": "http://172.19.0.2:80/generate_receive"
            }
        )
        # os.system("docker run --rm --network=syntheticdatagenerator_default -e SYNTHEA_SIZE=1 -e FHIR_URL=http://172.19.0.2:80/generate_receive conceptant/synthea-fhir")


        # directory_uuid = str(uuid.uuid4())
        # synthea_dir = "../synthea/" + directory_uuid
        # os.mkdir(synthea_dir)
        # os.system("hello world")
        # os.system(
        #     f'cd ../synthea && ./run_synthea --exporter.baseDirectory  "{directory_uuid}"'
        # )

    # docker run --rm --network=syntheticdatagenerator_default -e SYNTHEA_SIZE=1 -e FHIR_URL=http://172.19.0.2:80/generate_receive conceptant/synthea-fhir

    # def docker_test():
    #     client = docker.from_env()
    #     client.containers.run("ubuntu", "echo hello world")
        # docker inspect 0e68205a99ac | jq '.[].NetworkSettings.Networks.syntheticdatagenerator_default.IPAddress'
