from typing import List

amino_acids = "ACDEFGHIKLMNPQRSTVWY"
aa_map = {c : i for c, i in zip(amino_acids, range(1,21))}

csv_target_columns = {
    "HIC" : "HIC",
    "CHO" : "PR_CHO",
    "AC-SINS" : "AC-SINS_pH7.4",
    "Tm2" : "Tm2",
    "Titer" : "Titer"
}

xl_target_columns = {
    "HIC" : "hic_rt",
    "CHO" : "polyreactivity_prscore_cho",
    "AC-SINS" : "acsins_dLmax_ph7.4",
    "Tm2" : "tm2_nanodsf",
    "Titer" : "titer"    
}

def sequence_to_vector(seq: str) -> list[int]:
    try:
        return [aa_map[c] for c in seq]
    except KeyError:
        raise KeyError(f"Found unknown amino acid in sequence {seq}")
