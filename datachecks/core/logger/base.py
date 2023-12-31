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

from abc import ABC, abstractmethod
from typing import Dict


class MetricLogger(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def log(
        self, metric_name: str, metric_value: float, metric_tags: Dict[str, str] = None
    ):
        """
        Log a metric to the logger
        :param metric_name:
        :param metric_value:
        :param metric_tags:
        :return:
        """
        pass
