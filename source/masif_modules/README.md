### source/masif_modules

+ *DpMaSIF.py*: DpMaSIF neural network class and definition.
+ *MaSIF_ligand.py*: MaSIF-ligand neural network class and definition.
+ *MaSIF_ppi_search.py*: MaSIF-search neural network class and definition.
+ *MaSIF_site.py*: MaSIF-site neural network class and definition.
+ *compute_input_feat.py*: precompute the input features to the neural network in the format used for input (with, for example, padding)
+ *extract_features.py*: Precomputation step: extract features from matlab files, extract patches, and compute the distant dependend curvature.
+ *read_data_from_matfile.py*: Read the data from matlab files. 
+ *read_ligand_tfrecords.py*: Read the tf records for MaSIF-ligand.
+ *train_masif_site.py*: Train, test, and evaluate MaSIF-site.
+ *train_ppi_search.py*: Train test and evaluate MaSIF-search
