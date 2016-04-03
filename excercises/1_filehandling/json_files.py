__author__ = 'elopptj'
import json


def populate_json_file():
    data = {'key1': 'data1',
            'key2':
                [
                    1,
                    2,
                    3
                ],
            'key3':
                {
                    'subkey1': 'subvalue1',
                    'subkey2': 'subvalue2'
                }

            }

    print(data)

    with open('data.json', 'w') as file_obj:
        json.dump(data, file_obj, indent=4)


def read_json_file():
    with open('data.json', 'r') as file_obj:
        data = json.load(file_obj)

    print(data)


def main():
    populate_json_file()
    read_json_file()


if __name__ == '__main__':
    main()
