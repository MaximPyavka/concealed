from collections.abc import MutableSequence, MutableMapping
from itertools import product


def parse_container(container_dict, exclude=None):
    """
    Function to parse inclusive containers, for now dictionaries with unknown deep
    :param container_dict: dict or list
    :param exclude: possible set of keys to exclude
    :return: generator
    """
    exclude_keys = exclude if exclude else set()
    keys_to_parse = container_dict.keys() - exclude_keys

    main_dict = {}
    lists = []

    for key in keys_to_parse:
        data = container_dict.get(key, '')
        if isinstance(data, MutableMapping):
            _dict = parse_container(data, exclude=exclude)
            # print(f'_dict data --> {data}, _dict  --> {_dict}')
            lists.append(_dict)
        elif isinstance(data, MutableSequence):
            data_list = sum((parse_container(d, exclude=exclude) for d in data), [])
            # print(f'DT_list,         data --> {data}, data_list --> {data_list}')
            lists.append(data_list)
        elif data is None:
            main_dict[key] = ''
        else:
            main_dict[key] = data

    # print('lists BEFORE', lists)
    lists = list(build_dict_from_tuple(l) for l in product(*lists))
    ret_list = []
    for i in lists:
        res = {k: v for k, v in main_dict.items()}
        res.update(i)
        ret_list.append(res)

    # print('RET_LIST', ret_list)
    return ret_list


def build_dict_from_tuple(tuple_of_dicts):
    # print('TOD', tuple_of_dicts)
    res_dict = {}
    for dic in tuple_of_dicts:
        res_dict.update(dic)
    return res_dict


def grab_keys(dct, exclude=None):
    # keys = [f'{key}_{d}' for d in dct.keys()] if key else [d for d in dct.keys()]
    exclude_keys = exclude if exclude is not None else set()
    # print('EXCLUDE', exclude)
    # print(dct.keys(), exclude)
    keys = (set(dct.keys()) - exclude_keys)
    # print('KEYS          ', keys)
    for k, v in dct.items():
        if k in keys:
            # print('k', k)
            if isinstance(v, MutableMapping):
                add_keys = grab_keys(v, exclude=exclude)
            elif isinstance(v, MutableSequence):
                add_keys = grab_keys(v[0], exclude=exclude) if v else []
            else:
                continue
            keys = keys.union(add_keys)
    return keys


def build_dict_by_keys(set_of_keys, dct2):
    keys_to_use = set_of_keys
    return {key: dct2.get(key, '') for key in keys_to_use}


if __name__ == '__main__':
    dct = {'name': 'Max', 'skills': [{'football': 5}, {'basketball': 6}],
           'test1': {'Liverpool': 'Salah', 'MC': 'DeBruyne'},
           'science': [{'maths': 5}, {'biology': 7}], 'EventInfo': 62}
    #
    # inclusive_dict = {'books': [{'Illuzii': 15}, {"HP": 19}],
    #                   'cinema': [{'Matrix': 13}, {"Avengers": 134}],
    #                   'animals': [{'Wombat': 40}, {'Pig': 12}],
    #                   }
    #
    # dct['ogurci'] = inclusive_dict
    #
    # main_dict = {'M': 15, 'K': 9}
    # main_dict['super'] = dct
    # # dct.update(inclusive_dict)
    #
    # ret = parse_container(main_dict)
    # print('----------------------------')
    # print(ret)

    print(grab_keys(dct, exclude={'EventInfo'}))
