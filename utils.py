termination_types = {'100': ['AO', 'BO2'], '110': ['O2', 'ABO'], '111': ['AO3', 'B']}

charge_state_A_site = {0: 1, 1: 1, 2: 2, 3: 1}
charge_state_B_site = {0: 2, 1: 2, 2: 4, 3: 5}
charge_state_C_site = {0: -1, 1: -1, 2: -2, 3: -2}

A_site_list = [['Li', 'Na', 'K', 'Rb', 'Cs'], ['Li', 'Na', 'K', 'Rb', 'Cs'], ['Mg', 'Ca', 'Sr', 'Ba'],
               ['Li', 'Na', 'K', 'Rb', 'Cs']]
B_site_list = [['Pb', 'Sn', 'Ge'], ['V', 'Ta', 'Nb'], ['Ti', 'Zr'], ['V', 'Ta', 'Nb']]
C_site_list = [['F', 'Cl', 'Br', 'I'], ['F', 'Cl', 'Br', 'I'], ['O', 'S', 'Se', 'Te'], ['O', 'S', 'Se', 'Te']]


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