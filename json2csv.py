import csv  
import json  
import os
  



def json2csv(json_file_path,csv_file_path):
        
    fieldnames = []
    data = []
    # 加载JSON数据  
    with open(json_file_path, 'r', encoding='utf-8') as json_file:  
        data = json.load(json_file)  


        for i in data[0]:
            fieldnames.append(i)



    # 写入CSV文件  
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:  
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)  
        
        # 写入表头  
        writer.writeheader()  

        # 遍历每个JSON对象并写入CSV  
        for item in data:  
            writer.writerow(item)  
    
    print(f'CSV文件已保存至：{csv_file_path}')

def get_all_files_and_dirs(root_dir):  
    """  
    获取指定文件夹下的所有文件
    :param root_dir: 根目录路径  
    :return: 包含所有文件列表  
    """  
    all_files_and_dirs = []  
    for dirpath, dirnames, filenames in os.walk(root_dir):  
        for file in filenames:  
            all_files_and_dirs.append(os.path.join(dirpath, file))  
    return all_files_and_dirs 

if __name__ == "__main__":
    # # JSON文件路径  
    # json_file_path = os.path.join("data/xhs/search_comments_2024-04-05.json")
    
    # # CSV文件路径  
    # csv_file_path = 'output1.csv'  # 输出的CSV文件名  
    files = get_all_files_and_dirs(os.path.join("data\\xhs"))
    for file in files:
        json2csv(file,file[:-4] + 'csv')
    