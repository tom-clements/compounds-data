from typing import TypedDict, List


class Assay(TypedDict):
    result_id: int
    target: str
    result: str
    operator: str
    value: float
    unit: str


class Compound(TypedDict):
    compound_id: int
    smiles: str
    molecular_weight: float
    AlogP: float
    molecular_formula: str
    num_rings: int
    image: str
    assay_results: List[Assay]
