import os

def create_dict_from_env_variable():
    # 獲取環境變數TARGET的值
    target = os.getenv('TARGET')
    
    # 如果TARGET不存在，返回空字典
    if target is None:
        return {}
    
    # 使用split以"\n"切割並轉換成list
    target_list = target.split('\n')
    
    # 將list的每個value作為字典的key，預設value為""
    result_dict = {key: "" for key in target_list}
    
    return result_dict

# 示例使用
if __name__ == "__main__":
    result = create_dict_from_env_variable()
    print(result)