import json
from json.decoder import JSONDecodeError


def recursive_find(obj, value, type, par):
    if isinstance(obj, dict):
        if obj.get('values') is not None:
            if obj['id'] == value['id']:
                recursive_find(obj['values'], value, type='value', par=1)
            else:
                recursive_find(obj['values'], value, type='value', par=0)
        elif obj.get('params') is not None:
            recursive_find(obj['params'], value, type='param', par=0)
        if obj['id'] == value['id'] and obj['value'] == value['value'] and type == 'param':
            return value
        elif par == 1 and obj['id'] == value['value'] and type == 'value':
            value['value'] = obj['title']
            return value
    elif isinstance(obj, list):
        for item in obj:
            recursive_find(item, value, type, par)
    return value


def recursive_post(obj, value, res, lvl, type):
    if isinstance(obj, dict):
        if obj.get('values') is not None:
            recursive_post(obj['values'], value, res, lvl + 1, type='value')
        elif obj.get('params') is not None:
            recursive_post(obj['params'], value, res, lvl + 1, type='param')
        if obj['id'] == value['id'] and type == 'param':
            obj['value'] = value['value']
    elif isinstance(obj, list):
        for item in obj:
            recursive_post(item, value, res, lvl + 1, type)
            if lvl == 0:
                res.append(item)
    return res


try:
    with open("TestcaseStructure.json", "r") as structure_file:
        structure = json.load(structure_file)
    with open("Values.json", "r") as values_file:
        values = json.load(values_file)
except JSONDecodeError as e:
    error = {"error": {"message": "Входные файлы некорректны"}}
    with open("error.json", "w") as error_file:
        json.dump(error, error_file, ensure_ascii=False, indent=4)
else:
    structure_values = structure['params']
    for value in values['values']:
        new_value = recursive_find(structure_values, value, type='param', par=0)
        structure_values = recursive_post(structure_values, value, res=[], lvl=0, type='param')
    structure_values = {'params': structure_values}
    print(structure_values)
    with open("StructureWithValues.json", "w") as structure_values_file:
        json.dump(structure_values, structure_values_file, ensure_ascii=False, indent=4)
