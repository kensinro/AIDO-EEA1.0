import math
from aido_eea.validation import exact_accuracy, pairwise_agreement, confusion_matrix, macro_f1, fleiss_kappa

def test_exact_accuracy():
    assert exact_accuracy(["ENTITLED","QUALIFIED"],["ENTITLED","ENTITLED"]) == 0.5

def test_legacy_not_entitled_serialization():
    assert exact_accuracy(["NOT ENTITLED"],["NOT_ENTITLED"]) == 1.0

def test_confusion_identity():
    states=["ENTITLED","QUALIFIED","ABSTAIN","NOT ENTITLED","CONTRADICTED"]
    m=confusion_matrix(states,states)
    assert all(m[s][s] == 1 for s in states)
    assert macro_f1(states,states) == 1.0

def test_fleiss_perfect():
    rows=[["ENTITLED"]*3,["QUALIFIED"]*3,["ABSTAIN"]*3]
    assert math.isclose(fleiss_kappa(rows),1.0)
