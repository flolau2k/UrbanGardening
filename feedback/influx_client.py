from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.flux_table import TableList
from influxdb_client.client.write_api import SYNCHRONOUS
import logging


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


class influx_interface():
    def __init__(self) -> None:
        self.token = "dfLsGRYXZahjy2r8wseXtfzhkZ4fObpc4Jz0YSzi2IThpO_60ZqnBxkB7q6So5AmTp4OLOsrspuKwzkQF0Al_A=="
        self.org = "42Heilbronn"
        self.url = "http://localhost:8086"
        self.client = InfluxDBClient(url=self.url,
                                     token=self.token, org=self.org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()
        self.bucket = "urban"
        self.logger = get_logger("influx_interface")

    def write(self, point: Point):
        # self.logger.info(f"writing point: {point.__str__()}")
        self.write_api.write(bucket=self.bucket, org=self.org, record=point)

    def get(self, query) -> TableList:
        # self.logger.info(f"processing query: {query}")
        tables = self.query_api.query(query, org=self.org)
        return tables

    def create_point(self, name: str, measurement: str, tag: str,
                     value: float):
        point = (Point(f"{name}")
                 .measurement(f"{measurement}")
                 .tag("sensor_id", f"{tag}")
                 .tag("bucket", f"{self.bucket}")
                 .field("value", value)
                 )
        return point
