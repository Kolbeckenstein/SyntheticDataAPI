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

    def filter_synthea_response(synthea_response):
        patients = list(filter(lambda entry: entry["resource"]["resourceType"] == "Patient", synthea_response)) 
        for patient in patients:
            del patient["resource"]["text"]
        return patients