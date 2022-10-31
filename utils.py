from ase.geometry.analysis import Analysis
import numpy as np

termination_types = {'100': ['AO', 'BO2'], '110': ['O2', 'ABO'], '111': ['AO3', 'B']}

charge_state_A_site = {0: 1, 1: 1, 2: 2, 3: 1}
charge_state_B_site = {0: 2, 1: 2, 2: 4, 3: 5}
charge_state_C_site = {0: -1, 1: -1, 2: -2, 3: -2}

A_site_list = [['Li', 'Na', 'K', 'Rb', 'Cs'], ['Li', 'Na', 'K', 'Rb', 'Cs'], ['Mg', 'Ca', 'Sr', 'Ba'],
               ['Li', 'Na', 'K', 'Rb', 'Cs']]
B_site_list = [['Pb', 'Sn', 'Ge'], ['V', 'Ta', 'Nb'], ['Ti', 'Zr'], ['V', 'Ta', 'Nb']]
C_site_list = [['F', 'Cl', 'Br', 'I'], ['F', 'Cl', 'Br', 'I'], ['O', 'S', 'Se', 'Te'], ['O', 'S', 'Se', 'Te']]

charge_state_A_site = {0: 1, 1: 1, 2: 2, 3: 1}
charge_state_B_site = {0: 2, 1: 2, 2: 4, 3: 5}
charge_state_C_site = {0: -1, 1: -1, 2: -2, 3: -2}

def load_all_uids():
    import os,glob
    import sqlite3, json
    all_dbs = glob.glob('2dpv_set*.db')
    for db in all_dbs:
        dbname = os.path.join(os.getcwd(), db)
        all_uids = []
        _db = sqlite3.connect(dbname)
        cur = _db.cursor()
        cur.execute("SELECT * FROM systems")
        rows = cur.fetchall()

        for row in rows:
            for i in row:
                if 'uid' in str(i):
                    this_dict = json.loads(str(i))
                    this_uid = this_dict['uid']
                    if this_uid not in all_uids:
                        all_uids.append(this_uid)
    return all_uids

#some helper functions to get the BO-bond vectors in different structures
def BO_bond_vectors_in_bulk_perovskite(db, a, b, c):
    system_name = a + b + c
    uid = system_name + '3_pm3m'
    row = db.get(selection=[('uid', '=', uid)])
    atoms = row.toatoms()
    analyzer = Analysis(atoms)
    all_vectors = []
    for bonds in analyzer.get_bonds(b, c)[0]:
        v = atoms.get_distances(bonds[0], [bonds[1]], mic=True, vector=True)[0]
        #v = np.array(*atoms.get_distances(bonds[0], [bonds[1]], mic=True, vector=True)[0])
        #print(v)
        #v = cVector3D(*atoms.get_distances(bonds[0], [bonds[1]], mic=True, vector=True)[0])
        #v = cVector3D(*v)
        all_vectors.append(v)
    return all_vectors


def BO_bond_vectors_in_twod_perovskites(db, a, b, c, orientation, termination, thickness):
    system_name = a + b + c
    uid = system_name + '3_' + str(orientation) + "_" + str(termination) + "_" + str(thickness)
    #print(uid)
    try:
        row = db.get(selection=[('uid', '=', uid)])
    except:
        return None
    atoms = row.toatoms()
    analyzer = Analysis(atoms)
    all_vectors = []
    for bonds in analyzer.get_bonds(b, c)[0]:
        v = atoms.get_distances(bonds[0], [bonds[1]], mic=True, vector=True)[0]
        #v = cVector3D(*atoms.get_distances(bonds[0], [bonds[1]], mic=True, vector=True)[0])
        #v = cVector3D(*v)
        all_vectors.append(v)
    return all_vectors