from pysdd.sdd import SddManager, Vtree, CompilerOptions

vtree = Vtree(var_count=2, vtree_type="balanced")
sdd = SddManager.from_vtree(vtree)

new_options = CompilerOptions(vtree_search_mode=0)
sdd.set_options(new_options)
#sdd.auto_gc_and_minimize_on()

a, b = sdd.vars

nnf = (a | ~b | (a & ~b)) & (b | ~a | (b & ~a)) # nested NNF (not DNF)
dnf = (a & b) | (a & ~a) | (b & ~b) | (~a & ~b) | (a & b & ~a) | (a & b & ~b) | (a & ~a & ~b) | (b & ~a & ~b) | (a & b & ~a & ~b) # DNF, doesn't work with sdd.auto_gc_and_minimize_on()

# equivalence checking
print(nnf.equiv(dnf))
print((nnf & dnf) | (~nnf & ~dnf))
