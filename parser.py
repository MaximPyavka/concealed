import requests
from lxml import html
import json

from time import sleep

from config import ADDITIONAL_HEADERS, POST_URL, CSV_OUTPUT
from utils import parse_container, grab_keys, build_dict_by_keys
from file_handler import CSVWriterContextManager, field_names


def check_session(func):
    """
    Decorator for web_client functions to use one session
    :param func: function to use session
    :return: web client function
    """

    def wrapper(*args):
        obj = args[0]
        if obj.session is None:
            obj.session = requests.Session()
            obj.session.headers.update(ADDITIONAL_HEADERS)
        return func(*args)

    return wrapper


def html_parser(dumped_text):
    """
    Return generator of ids
    :param dumped_text: dumped html text
    :return: generator of members ids
    """
    raw_dump = html.fromstring(dumped_text)
    return (member_id for member_id in raw_dump.xpath('//h5/a[@class="orange"]/@href'))


class JSONParser:
    def __init__(self, ids):
        self.ids = ids
        self.session = None

    @check_session
    def make_post(self, data):
        data = f'"{data}"'
        response = self.session.post(
            POST_URL,
            data=data,
        )
        sleep(1)
        return response

    def get_final_json(self, member_id):
        data = member_id.split('=')[-1]
        resp = self.make_post(data)
        data_dict = json.loads(resp.json())
        return data_dict

    def parse_data(self, data_dict):
        data = parse_container(data_dict, exclude={'EventInfo'})
        return data

    def write_to_csv(self):
        with CSVWriterContextManager(CSV_OUTPUT, field_names) as output_file:
            for n, id_ in enumerate(self.ids):
                print('ID', n)
                data_dict = json_parser.get_final_json(id_)
                data = self.parse_data(data_dict)
                for d in data:
                    data_to_write = build_dict_by_keys(field_names, d)
                    print(d)
                    output_file.writerow(data_to_write)

    def save_json(self, member_id):
        print(member_id)
        data = member_id.split('=')[-1]
        resp = self.make_post(data)
        data_dict = json.loads(resp.json())
        print(data_dict)

        with open('results/{}.json'.format(data), 'w') as file:
            json.dump(data_dict, file)


if __name__ == '__main__':
    csv_headers = set()

    with open('data/dump') as dump:
        dumped = dump.read()

    ids_gen = html_parser(dumped)
    json_parser = JSONParser(ids_gen)
    for n, i in enumerate(json_parser.ids):
        print(f'{n}, id = {i}')
        json_parser.save_json(i)
    # json_parser.write_to_csv()

    # for n, i in enumerate(json_parser.ids):
    #     print('ID', n, len(csv_headers))
    #     data_dict = json_parser.get_final_json(i)
    #     add_to_csv = grab_keys(data_dict, exclude={'EventInfo'})
    #     csv_headers = csv_headers | set(add_to_csv)
    #     print(csv_headers)
