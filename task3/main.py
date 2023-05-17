import requests


def find_questions_with_tag(tag):
    # дата с 16 по 17 мая
    # /2.3/questions?
    # fromdate=1684195200&todate=1684281600&order=desc&sort=activity&tagged=python&site=stackoverflow
    url = "https://api.stackexchange.com/2.3/questions"
    tag = "python"
    params = {
        "fromdate": 1684195200,
        "todate": 1684281600,
        "order": "desc",
        "sort": "activity",
        "site": "stackoverflow",
        "tagged": tag
    }
    response = requests.get(url=url, params=params)
    data = response.json()
    # print(data['items'])
    print(f'Список вопросов за последние два дня с тэгом {tag}:\n')
    for i in data['items']:
        print(i['title'])


def main():
    tag = "python"
    find_questions_with_tag(tag)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


