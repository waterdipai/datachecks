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

import datetime
import json
from abc import ABC
from typing import Dict

from datachecks.core.common.models.metric import MetricsType, MetricValue
from datachecks.core.datasource.base import DataSource
from datachecks.core.logger.base import MetricLogger


class MetricIdentity:
    @staticmethod
    def generate_identity(
        metric_type: MetricsType,
        metric_name: str,
        data_source: DataSource,
        index_name: str = None,
        table_name: str = None,
        field_name: str = None,
    ):
        """
        Generate a unique identifier for a metric
        """

        identifiers = [data_source.data_source_name]

        if index_name:
            identifiers.append(index_name)
        elif table_name:
            identifiers.append(table_name)

        if field_name:
            identifiers.append(field_name)

        identifiers.append(metric_type.value)
        identifiers.append(metric_name)
        return ".".join([str(p) for p in identifiers])


class Metric(ABC):
    """
    Metric is a class that represents a metric that is generated by a data source.
    """

    def __init__(
        self,
        name: str,
        data_source: DataSource,
        metric_type: MetricsType,
        metric_logger: MetricLogger = None,
        **kwargs,
    ):
        if "index_name" in kwargs and "table_name" in kwargs:
            if kwargs["index_name"] is not None and kwargs["table_name"] is not None:
                raise ValueError(
                    "Please give a value for table_name or index_name (but not both)"
                )
        if "index_name" not in kwargs and "table_name" not in kwargs:
            raise ValueError("Please give a value for table_name or index_name")

        self.index_name, self.table_name = None, None
        if "index_name" in kwargs:
            self.index_name = kwargs["index_name"]
        if "table_name" in kwargs:
            self.table_name = kwargs["table_name"]

        self.name: str = name
        self.data_source = data_source
        self.metric_type = metric_type
        self.filter_query = None
        if "filters" in kwargs and kwargs["filters"] is not None:
            filters = kwargs["filters"]
            if ("search_query" in filters and filters["search_query"] is not None) and (
                "where_clause" in filters and filters["where_clause"] is not None
            ):
                raise ValueError(
                    "Please give a value for search_query or where_clause (but not both)"
                )

            if "search_query" in filters and filters["search_query"] is not None:
                self.filter_query = json.loads(filters["search_query"])
            elif "where_clause" in filters:
                self.filter_query = filters["where_clause"]
        self.metric_logger = metric_logger

    def get_metric_identity(self):
        return MetricIdentity.generate_identity(
            metric_type=self.metric_type,
            metric_name=self.name,
            data_source=self.data_source,
        )

    def _generate_metric_value(self) -> float:
        pass

    def get_metric_value(self) -> MetricValue:
        metric_value = self._generate_metric_value()
        tags = {
            "metric_name": self.name,
        }

        value = MetricValue(
            identity=self.get_metric_identity(),
            metric_type=self.metric_type.value,
            value=metric_value,
            timestamp=datetime.datetime.utcnow().isoformat(),
            data_source=self.data_source.data_source_name,
            tags=tags,
        )
        if "index_name" in self.__dict__ and self.__dict__["index_name"] is not None:
            value.index_name = self.__dict__["index_name"]
        elif "table_name" in self.__dict__ and self.__dict__["table_name"] is not None:
            value.table_name = self.__dict__["table_name"]

        if "field_name" in self.__dict__ and self.__dict__["field_name"] is not None:
            value.field_name = self.__dict__["field_name"]

        return value


class FieldMetrics(Metric, ABC):
    def __init__(
        self,
        name: str,
        data_source: DataSource,
        metric_type: MetricsType,
        metric_logger: MetricLogger = None,
        **kwargs,
    ):
        super().__init__(
            name=name,
            data_source=data_source,
            metric_type=metric_type,
            metric_logger=metric_logger,
            **kwargs,
        )
        if "field_name" in kwargs:
            self.field_name = kwargs["field_name"]

    @property
    def get_field_name(self):
        return self.field_name
