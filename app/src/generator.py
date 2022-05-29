import docker
import json

class Generator:
    def generate_synthea_patient():
        print("Generating patients")
        client = docker.from_env()
        container = client.containers.get("syntheticdatagenerator_syntheticDataAPI_1")
        ip_address = container.attrs['NetworkSettings']['Networks']['syntheticdatagenerator_default']['IPAddress']

        client.containers.run(
            "conceptant/synthea-fhir",
            auto_remove = True,
            network="syntheticdatagenerator_default",
            environment={
                "SYNTHEA_SIZE": 1,
                "FHIR_URL": f"http://{ip_address}/generate_receive"
            }
        )
        print(f"starting synthea with a callback url of http://{ip_address}/generate_receive")

    def filter_synthea_response(synthea_response):
        # print(json.dumps(synthea_response))
        if synthea_response and "entry" in synthea_response:
            patients = list(filter(lambda entry: entry != None and "resource" in entry and entry["resource"]["resourceType"] == "Patient", synthea_response["entry"])) 
            for patient in patients:
                del patient["resource"]["text"]
            return patients