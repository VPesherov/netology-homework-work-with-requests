import requests
from pprint import pprint


# написал униварсальную функцию,
# которая может сравнивать любое количество героев по любому переданному атрибуту
def compare_hero(hero_json_list, hero_list, attribute):
    max_attribute = -1
    try:
        for hero_json in hero_json_list:
            for hero in hero_list:
                if hero == hero_json['name']:
                    if hero_json['powerstats'][attribute] > max_attribute:
                        max_attribute = hero_json['powerstats'][attribute]
                        best_hero = hero
    except KeyError:
        return 'Ошибка атрибута'

    return best_hero


def main():
    url = r'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url=url)
    hero_json_list = response.json()

    print(compare_hero(hero_json_list, ['Hulk', 'Captain America', 'Thanos'], 'intelligence'))


if __name__ == '__main__':
    main()
