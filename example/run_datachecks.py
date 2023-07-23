#  Copyright 2022-present, the Waterdip Labs Pvt. Ltd.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import requests

from datachecks import Configuration, Inspect, load_configuration

if __name__ == "__main__":
    # Reding Config File
    configuration: Configuration = load_configuration("config.yaml")

    # Generating Metrics
    metrics = Inspect(configuration).start()

    # Sending to ELK
    for metric in metrics:
        print(metric)
        requests.post(
            "https://localhost:9201/example_indices/_doc",
            json=metric,
            auth=("admin", "admin"),
            verify=False,
        )