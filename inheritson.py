#!/usr/bin/env python3
'''

'''


def resolve_inheritance(
        data: list,
        ref_field: str = 'copy-from',
        id_field: str = 'id') -> list:
    '''
    Fill in values from parent by reference field.
    '''
    return data


if __name__ == '__main__':
    data = [{
            "id": "parent",
            "uniq": "parent uniq",
            "common": "value",
            }, {
            "id": "child",
            "copy-from": "parent",
            "uniq": "child uniq",
            }, {
            "id": "grandchild",
            "copy-from": "child",
            "uniq": "grandchild uniq",
            }]
    reversed_data = list(reversed(data))

    assert resolve_inheritance(data)[0].get('common') == 'value'
    assert resolve_inheritance(reversed_data)[0].get('common') == 'value'
