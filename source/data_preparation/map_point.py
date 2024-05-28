import numpy as np
import os
from default_config.masif_opts import masif_opts

class Map_pocket:
    def __init__(self):
        self.data_preparation = os.path.join(masif_opts["ligand"],'data_preparation')
        self.pdb_list = os.path.join(masif_opts["ligand"],'list','sequence_split_list.txt"')
        self.precomputation_path = masif_opts["ligand"]["masif_precomputation_dir"]
        self.atom_dict = {"N":0,"O":1,"C":2,"H":3,"S":4,"P":5,"Z":6}
        self.upper_radii = {0:1.8, 1:1.6, 2:2.0, 3:1.4, 4:2.0, 5:2.0, 6:1.6}
        self.lower_radii = {0:1.4, 1:1.2, 2:1.6, 3:1.0, 4:1.6, 5:1.6, 6:1.2}
    def extract_atom_info(self):
        
        with open(self.pdb_list, "r") as f:
            pdb_list = f.readlines()

            for pdb in pdb_list:
                pdb = pdb.strip()
                atom_info = []
                nowat_file = os.path.join(self.data_preparation,"01-benchmark_pdbs","{}nowat_out".format(pdb.strip()))
                rank_file = os.path.join(nowat_file,"pockets","bary_centers_ranked.types")
                pdb_file = os.path.join(nowat_file,"{}nowat_pockets.pqr".format(pdb.strip()))
                data_file = os.path.join(self.precomputation_path,pdb.strip(),"extract_atom.npy")
                with open(rank_file,"r") as rank:
                    pockets_num = []
                    rank_list = rank.readlines()
                    if len(rank_list) > 3:
                        pockets_count = 3
                    else:
                        pockets_count = len(rank_list)
                    for line in rank_list:
                        data = line.split()
                        pocket = data[0]
                        pockets_num.append(pocket)
                    sele_pocket = pockets_num[:pockets_count]
                with open(pdb_file, 'r') as atom_file:
                    atom_list = atom_file.readlines()
                    for line in atom_list:
                        parts = line.split()
                        if parts[0] == "ATOM":
                            pocket_num = parts[4]
                            if pocket_num in sele_pocket:
                                atom_type = parts[2]
                                x = float(line[30:38])
                                y = float(line[38:46])
                                z = float(line[46:54])
                                atom_info.append((self.atom_dict[atom_type], x, y, z))
                    np.save(data_file,np.array(atom_info))
                print(pdb.strip()) 
    
    def map_point(self):
        with open(self.pdb_list, "r") as f:
            pdb_list = f.readlines()
            # not_found_num = 0
            for pdb in pdb_list:
                pdb = pdb.strip()
                nowat_file = os.path.join(self.data_preparation,"01-benchmark_pdbs","{}nowat_out".format(pdb.strip()))
                
                pdb_file = os.path.join(nowat_file,"{}nowat_pockets.pqr".format(pdb.strip()))
                data_file = os.path.join(self.precomputation_path,pdb.strip(),"extract_atom.npy")
                atom_info = np.load(data_file)
                X = np.load(
                os.path.join(
                    self.precomputation_path, "{}".format(pdb.strip()), "p1_X.npy"
                    )
                )
                Y = np.load(
                    os.path.join(
                        self.precomputation_path, "{}".format(pdb.strip()), "p1_Y.npy"
                    )
                )
                Z = np.load(
                    os.path.join(
                        self.precomputation_path, "{}".format(pdb.strip()), "p1_Z.npy"
                    )
                )
                xyz_coords = np.vstack([X, Y, Z]).T
                
                mapped_flatten = np.empty((atom_info.shape[0]), dtype=np.int64)
                
                for index,atom in enumerate(atom_info):
                    atom_x = float(atom[1])
                    atom_y = float(atom[2])
                    atom_z = float(atom[3])
                    atom_xyz = [atom_x,atom_y,atom_z]
                    point_distance = np.sum((xyz_coords - atom_xyz)**2,axis=1)
                    nearest_index = np.argmin(point_distance)
                    
                    mapped_flatten[index] = nearest_index
                mapped_point = np.unique(mapped_flatten)
                np.save(os.path.join(self.data_preparation,"04a-precomputation_12A","precomputation",pdb.strip(),"mapped_point.npy"),mapped_point)
                print(pdb.strip())

map = Map_pocket()
map.map_point()
