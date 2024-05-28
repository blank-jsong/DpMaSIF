#!/bin/bash

# 指定包含 PDB 文件名的文本文件路径
file="/mobile_disk/masif/data/masif_ligand/lists/all_pdbs_sequence.txt"

# 逐行读取文本文件
while IFS= read -r line
do
    # 添加文件扩展名 ".pdb"
    pdb_file="$line.pdb"
    
    # 打印当前正在处理的文件名
    echo "Processing file: $pdb_file"
    
    # 运行 Python 脚本进行预测，假设脚本名为 predict.py
    python predict.py -p "/mobile_disk/masif/data/masif_ligand/data_preparation/01-benchmark_pdbs/$pdb_file" -c first_model_fold1_best_test_auc_85001.pth.tar -s seg0_best_test_IOU_91.pth.tar 
    
    # 可以根据需要在此处添加额外的操作
    
done < "$file"

