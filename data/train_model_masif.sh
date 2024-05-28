export PYTHONPATH=$PYTHONPATH:$MONET_DIR:./
masif_root=/mobile_disk/masif
masif_source=$masif_root/source/
masif_matlab=$masif_root/source/matlab_libs/
export PYTHONPATH=$PYTHONPATH:$masif_source
source $masif_root/set_up.sh

python -u $masif_source/masif_ligand/masif_ligand_train.py