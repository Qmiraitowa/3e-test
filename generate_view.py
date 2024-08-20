import pandas as pd

# 读取Excel文件
file_path = "C:/Users/F-miraitowa/Desktop/Category_Product.xlsx"
xls = pd.ExcelFile(file_path)

# 加载两个工作表的数据
category_df = pd.read_excel(file_path, sheet_name='Category')
product_df = pd.read_excel(file_path, sheet_name='Product')

# 合并category和product数据表，基于外键进行连接
merged_df = pd.merge(product_df, category_df, left_on='CategoryForeignId', right_on='Foreignld')

# 按类别分组并格式化输出
output_lines = []
for i, (category, group) in enumerate(merged_df.groupby('Name_y'), start=1):
    output_lines.append(f"{i}: {category}")
    for _, row in group.iterrows():
        if pd.notna(row['Code']):  # 检查编号是否存在
            output_lines.append(f"-  {row['Name_x']} ({row['Code']}) ")
        else:  # 如果编号不存在，只输出菜品名称
            output_lines.append(f"-  {row['Name_x']}")
    output_lines.append("")

# 将所有行连接成一个字符串，使用换行符分隔
output_text = "\n".join(output_lines)

# 定义输出文件路径
output_file_path = 'C:/Users/F-miraitowa/Desktop/study abroad/Python_learning/output.txt'

# 将输出写入文本文件
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(output_text)

print(f"文件已保存为 {output_file_path}")
