masif_root=/mobile_disk/masif
masif_source=$masif_root/source/
masif_matlab=$masif_root/source/matlab_libs/
export PYTHONPATH=$PYTHONPATH:$masif_source
export masif_matlab

python -u $masif_source/data_preparation/04b-make_ligand_tfrecords.py
