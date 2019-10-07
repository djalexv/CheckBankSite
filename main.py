import requests

if __name__ == '__main__':
    path = 'tb.txt'
    with open(path) as f:
        for line in f:
            try:
                print(line.strip())
                r = requests.get(line).status_code
                print(r)
                # if r != 200: сделать ping -проверить доступнсть
            # except Exception: # разобрать
            #     r = -1---
            except requests.ConnectionError:
                print('something network trouble')
            except requests.RequestException:
                print('alarm, is disaster happen')

