import requests

if __name__ == '__main__':
    # print(__name__)
    path = 'tb.txt'
    with open(path) as f:
        for line in f:
            print(line.strip())
            # print(type(line))
            r = requests.get(line).status_code
            print(r)
            # print(requests.get(line))
            # .status_code)

    # r = requests.get('https://alfabank.ru/' )
    # print(r.status_code)
