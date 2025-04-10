import json

# 加载json格式测试用例
def load_json_cases(json_path):
    with open(json_path, 'r', encoding="utf-8") as f:
        cases=json.load(f)
    
    case_list=[]
    for item in cases:
        for case in item["cases"]:
            case["module"]=item["module"]
            case["preconditions"]=item["preconditions"]
            case_list.append(case)
    
    return case_list


if __name__ == '__main__' :
    print(load_json_cases("docs/ddt/cases.json"))