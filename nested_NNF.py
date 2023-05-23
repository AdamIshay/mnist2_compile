from pysdd.sdd import SddManager, Vtree

vtree = Vtree(var_count=4, vtree_type="balanced")
sdd = SddManager.from_vtree(vtree)
a, b, c, d = sdd.vars

nnf = (a | ~b | (a & ~b)) & (b | ~a | (b & ~a)) # nested NNF (not DNF)
dnf = (a & b) | (a & ~a) | (b & ~b) | (~a & ~b) | (a & b & ~a) | (a & b & ~b) | (a & ~a & ~b) | (b & ~a & ~b) | (a & b & ~a & ~b) # DNF

# equivalence checking
print(nnf.equiv(dnf))
print((nnf & dnf) | (~nnf & ~dnf))
