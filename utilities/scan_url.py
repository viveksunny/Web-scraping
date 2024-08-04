from utilities.configurations.create_headers import Headers
from utilities.config import ScanConfigurations
from bs4 import BeautifulSoup
import requests


freq = {'d': 'daily',
        'w': 'weekly',
        'h': 'hourly',
        'm': 'monthly'}


class RoutineScan:
    def __init__(self, scan_name, frequency=None):
        """
        The class will be used to initialize the scan type and frequency
        :param scan_name: expected Values PINKALERTS
        :param frequency: d, h, m, w
        freq = {'d': 'daily', 'w': 'weekly', 'h': 'hourly', 'm': 'monthly'}
        """
        self.scan_name = scan_name
        self.frequency = frequency
        self.frequency_clause_name = 'hourly' if self.frequency is None else freq[frequency]
        self.scan_clause = str.__add__(str(scan_name),'-SCAN-CLAUSE')
        self.scan_urls = str.__add__(str(scan_name),'-URLS')
        self.header = Headers().getDefaultHeader()
        self.screener_val = str.__add__(self.frequency_clause_name, '-screener')
        self.screener_url = self.read_url_config(self.screener_val)
        self.process_url = self.read_url_config('process')
        self.scan_criteria = self.read_scan_config(self.frequency_clause_name)
        self.response = []

    def read_url_config(self, sub_config):
        return ScanConfigurations(self.scan_urls, sub_config).getvalue()

    def read_scan_config(self, sub_config):
        return ScanConfigurations(self.scan_clause, sub_config).getvalue()


def scan_main(alertname=None, frequency=None):
    alert_name = 'PINKALERTS' if alertname is None else alertname
    obj_pink = RoutineScan(alert_name, frequency)
    with requests.session() as scan:
        response = scan.get(obj_pink.screener_url)
        soup = BeautifulSoup(response.text, "html.parser")
        obj_pink.header['x-csrf-token'] = soup.select_one("[name='csrf-token']")['content']
        datas = {'scan_clause' : obj_pink.scan_criteria}
        data_response = scan.post(obj_pink.process_url, data=datas, headers=obj_pink.header)
        obj_pink.total_record = data_response.json()['recordsFiltered']
        for response_data in data_response.json()['data']:
            obj_pink.response.append({'id': response_data.get('sr'),
                                      'short_name': response_data.get('nsecode'),
                                      'full_name' : response_data.get('name'),
                                      'price': response_data.get('close')})
        return obj_pink.response