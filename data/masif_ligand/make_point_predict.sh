
file="/masif/data/masif_ligand/lists/all_pdbs_sequence.txt"
while IFS= read -r line
do
    pdb_file="$line.pdb"    
    echo "Processing file: $pdb_file"    
    python predict.py -p "/masif/data/masif_ligand/data_preparation/01-benchmark_pdbs/$pdb_file" -c /masif/source/DeepPocket-main/first_model_fold1_best_test_auc_85001.pth.tar -s /masif/source/DeepPocket-main/seg0_best_test_IOU_91.pth.tar 
            
done < "$file"