masif_root=/storage1/masif
i=1
while read p; do
    ./data_prepare_one.sh $p
    i=$((i+1))
done < $masif_root/data/masif_ligand/lists/sequence_split_list.txt