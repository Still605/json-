import json

with open('data/123.json', 'r', encoding='utf-8') as file:
    # 使用json.load()方法解析JSON数据
    data1 = json.load(file)
print(data1)

with open('data/456.json', 'r', encoding='utf-8') as file:
    # 使用json.load()方法解析JSON数据
    data2 = json.load(file)
print(data2)


def compare_dif_value(json1, json2):
    # 输出两个json中相同key不同value的结果
    for key in json1:
        if isinstance(json1[key], dict):
            compare_dif_value(json1[key], json2[key])
        elif json1[key] != json2[key]:
            print(f"Key: {key}, Value1: {json1[key]}, Value2: {json2[key]}")


def compare_dif_value_type(json1, json2):
    # 输出两个json中相同key,value类型不一致的结果
    for key in json1:
        if isinstance(json1[key], dict):
            compare_dif_value_type(json1[key], json2[key])
        elif type(json1[key]) != type(json2[key]):
            print(f"Key: {key}, Value1: {type(json1[key])}, Value2: {type(json2[key])}")


def compare_lack_key(json1, json2):
    # 输出两个json,第一个json中有的但第二个json中没有的key的结果
    for key in json1:
        if isinstance(json1[key], dict):
            compare_lack_key(json1[key], json2[key])
        elif not (key in json2):
            print(f"Key: {key}, Value1: {json1[key]}")
