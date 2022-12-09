import math

import hydrus_api

from homura_art.model import File


def sync(acccess_key):
    data = []
    client = hydrus_api.Client(acccess_key)
    hashes = set(client.search_files(["system:everything"], return_hashes=True))
    existing_hashes = set(
        [
            f"{int.from_bytes(file.hash, 'little'):064x}"
            for file in File.select(File.hash)
        ]
    )
    hashes = list(hashes.difference(existing_hashes))

    service = None
    step = 1000
    hashes_len = len(hashes)
    for i in range(math.ceil(len(hashes) / step)):
        s = i * step
        e = s + step
        for file in client.get_file_metadata(hashes[s:e]):
            if not service:
                service = next(iter(file["file_services"]["current"]))
            data.append(
                (
                    int(file["hash"], 16).to_bytes(32, "little"),
                    file["file_services"]["current"][service]["time_imported"],
                )
            )
        print("step/all", f"{e}/{hashes_len}")
    File.insert_many(data, fields=[File.hash, File.import_time]).execute()
