# pyre-strict

import csv
import json
import os
import time
from datetime import datetime

import pandas as pd
import requests

from src.Aufgaben.WeatherDto import WeatherDto


class Weather:
    # OpenWeather API Key
    API_KEY: str = 'bdcba0e834a44aeba348908ada9729f5'
    API_BASE_URL: str = 'https://api.openweathermap.org'
    DIR: str = os.path.dirname(os.path.abspath(__file__))

    def __int__(self):
        """Main Method"""
        print("Init Class!")

    def _call_api(self, p_city: str, ) -> str:
        """Call Remote API and return data"""
        try:
            url = self.API_BASE_URL + '/data/2.5/weather?q=' + p_city + '&appid=' + self.API_KEY + '&units=metric'
            response = requests.get(url)
            return response.content.decode()
        except Exception as e:
            print(e)
            raise

    def _get_target_cities(self) -> list:
        """Read Cities from CSV File and return list"""
        resp = []

        with open(self.DIR + '/citylist.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                resp += row

        return resp

    def write_out_json(self, record_identifier, data) -> None:
        file_path = self._get_file_path('json', record_identifier)
        print("Writeout File" + file_path)
        file = open(file_path, "a+")
        file.write(data)
        file.close()

    def write_out_csv(self, record_identifier, data: WeatherDto) -> None:
        file_path = self._get_file_path('csv', record_identifier)
        print("Writeout File" + file_path)
        file = open(file_path, "a+")
        file.write(data.to_csv())
        file.close()

    def write_out_parquet(self, record_identifier, data: WeatherDto) -> None:
        file_path = self._get_file_path('parquet', record_identifier)
        print("Writeout File" + file_path)
        df = pd.DataFrame(data=data.to_flat_obj())
        df.to_parquet(file_path, compression='gzip')

    def _get_file_path(self, file_type: str, name: str) -> str:
        data_dir = '/data'
        dt = datetime.now()
        ts = time.time()
        dir_path = \
            self.DIR \
            + data_dir + "/" \
            + file_type + "/" \
            + str(dt.year) + "/" \
            + str(dt.month) + "/" \
            + name + "/"

        os.makedirs(os.path.dirname(dir_path), exist_ok=True)
        file_path = dir_path + str(ts) + "." + file_type

        return file_path

    def run(self):

        print("Welcome to the fancy weather exporter ;)")

        input1 = input("Download the Cities from the given CSV list [Yes]:")
        if input1 != "" and input1.lower() != "yes":
            print("Aborting the script. Bye")
            return

        input2 = input("Enter the name of the city you want to download. (must be part of the CSV list). Use * for "
                       "all cities:")
        city_list_csv = self._get_target_cities()
        if input2 == "*":
            city_list = city_list_csv
        else:
            if input2 in city_list_csv:
                city_list = [input2]
            else:
                print("Please select a valid city, defined in the CSV file. Aborting.")
                return

        try:

            for city in city_list:
                response = self._call_api(city)

                parsed = json.loads(response)
                data: str = json.dumps(parsed, indent=4)
                self.write_out_json(city, data)

                data_dto = WeatherDto.from_json(parsed)
                self.write_out_csv(city, data_dto)
                self.write_out_parquet(city, data_dto)

        except Exception as e:
            print(e)
            raise
