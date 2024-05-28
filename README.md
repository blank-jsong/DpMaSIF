# DpMaSIF：Prediction of Protein-Compound Interactions Based On Protein Molecular Surface
DpMaSIF is a geometric deep learning framework based on [MaSIF](https://github.com/LPDI-EPFL/masif) , which utilizes [DeepPocket](https://github.com/devalab/DeepPocket?tab=readme-ov-file) to predict protein-compound binding sites, for the prediction of protein-compound interactions.
If you want to use DpMaSIF, we recommend going through [MaSIF](https://github.com/LPDI-EPFL/masif) first.
## Requirements
Most dependencies are sourced from MaSIF, which you can find specific details about by clicking [here](https://github.com/LPDI-EPFL/masif).Performing neural network calculations requires the following dependencies .
* [Python](https://www.python.org/) (3.6)
* [reduce](http://kinemage.biochem.duke.edu/software/reduce.php) (3.23). To add protons to proteins. 
* [MSMS](http://mgltools.scripps.edu/packages/MSMS/) (2.6.1). To compute the surface of proteins. 
* [BioPython](https://github.com/biopython/biopython) (1.66) . To parse PDB files. 
* [PyMesh](https://github.com/PyMesh/PyMesh) (0.1.14). To handle ply surface files, attributes, and to regularize meshes.
* PDB2PQR (2.1.1), multivalue, and [APBS](http://www.poissonboltzmann.org/) (1.5). These programs are necessary to compute electrostatics charges.
* [open3D](https://github.com/IntelVCL/Open3D) (0.5.0.0). Mainly used for RANSAC alignment.
* [Tensorflow](https://www.tensorflow.org/) (1.9). Use to model, train, and evaluate the actual neural networks. Models were trained and evaluated on a NVIDIA Tesla K40 GPU.
* [StrBioInfo](https://pypi.org/project/StrBioInfo/). Used for parsing PDB files and generate biological assembly for MaSIF-ligand.
* [Dask](https://dask.org/) (2.2.0). Run function calls on multiple threads (Optional for reproducing some benchmarks).
* [Pymol](https://pymol.org/2/). This optional plugin allows one to visualize surface files in PyMOL.
* [Fpocket](https://github.com/Discngine/fpocket).  Predict protein-compound binding sites.
* [libmolgrid](https://github.com/gnina/libmolgrid). The essential dependencies of DeepPocket.
## Installation
After preinstalling dependencies, you can configure the necessary appropriate directories by modifying set_up.sh and running it.
## Data Preparation
For each application, MaSIF requires a preprocessing of data. This entails a running a scripted protocol, 
which performs the following steps: 

1. Download the PDB. 
2. Protonate the PDB, extract the desired chains, triangulate the surface (using MSMS), and compute chemical features. 
3. Extract all patches, with features and coordinates, for each protein.
4. Predict sites of protein-compound interactions

To prepare proteins data, you should change path to MaSIF-ligand.
```
cd /masif/data/masif_ligand
```
And you can run this protocol for all proteins:
```
bash ./data_prepare_all.sh
```
If you have access to a cluster, then this process can be run in parallel. If your cluster supports slurm files, we provide a slurm file under each application data directory. which can be run using sbatch: 

```
sbatch data_prepare.slurm
```

Most of the PDBs that were used for the paper, and their corresponding surfaces (with precomputed chemical features) are available at: https://doi.org/10.5281/zenodo.2625420 . The unbound proteins are available in this repository under [data/masif_ppi_search_ub/data_preparation/00-raw_pdbs/](https://github.com/LPDI-EPFL/masif/tree/master/data/masif_ppi_search_ub/data_preparation/00-raw_pdbs).

Note that the preparation of the data can consume a large amount of space for large protein databases. This is due to the fact that the preprocessing step decomposes protein surfaces into overlapping patches, which results in a large amount of duplicated data.

After protein data preparation, you can predict the sites of protein-compound interactions, you can run this process to get them:
```
bash ./map_point.sh
```
## Training Model
Once the data has been precomputed, DpMaSIF requires the generation of Tensorflow 
[TFRecords](#https://www.tensorflow.org/tutorials/load_data/tf_records) for training.
You can run this file to get it:
```
bash make_tfrecords_dpmasif.sh
```
Once the tfrecords have been precomputed, the training for the network can start, where we strongly recommend a GPU:

```
bash  train_model_dpmasif.sh
```

To evaluate the neural network run: 
```
bash evaluate_test_dpmasif.sh
```
If you want to compare DpMaSIF and MaSIF, you can run these process to get evaluation of MaSIF-ligand:
```
bash evaluate_test_masif.sh
```
The output of the evaluation is placed under the data/masif_ligand/test_set_predictions/ directory, with two numpy files per input protein databank structure, e.g.: 

```
5LXM_AD_labels_dpmasif.npy
5LXM_AD_logits_dpmasif.npy
```
where the labels file contains the ground truth, and the logits file contains the prediction logits.
## License
This project is covered under the Apache 2.0 License.
## Contact
jsong: songhuajian2002@gmail.com
