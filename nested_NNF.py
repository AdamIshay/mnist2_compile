from pysdd.sdd import SddManager, Vtree, CompilerOptions

vtree = Vtree(var_count=2, vtree_type="balanced")
sdd = SddManager.from_vtree(vtree)
a, b = sdd.vars

new_options = CompilerOptions(vtree_search_mode=0)
sdd.set_options(new_options)
sdd.auto_gc_and_minimize_on()


nnf = (a | ~b | (a & ~b)) & (b | ~a | (b & ~a)) # nested NNF (not DNF)
dnf = (a & b) | (a & ~a) | (b & ~b) | (~a & ~b) | (a & b & ~a) | (a & b & ~b) | (a & ~a & ~b) | (b & ~a & ~b) | (a & b & ~a & ~b) # DNF, doesn't work with sdd.auto_gc_and_minimize_on()
dnf2 = (a & b) | (a & ~a) | (b & ~b) | (~a & ~b) | (a & ~a) # DNF, works with sdd.auto_gc_and_minimize_on()


nnf = (a | ~b | (a & ~b)) & (b | ~a | (b & ~a)) # compiles fine (nested NNF)
dnf = (a & b) | (a & ~a) | (b & ~b) | (~a & ~b) # compiles fine (DNF)
#dnf = (a & b) | (a & ~a) | (b & ~b) | (~a & ~b) | (a & ~a) # compiles fine (DNF)
#dnf = (a & b) | (a & ~a) | (b & ~b) | (~a & ~b) | (a & b & ~a) # fails to compile with "error in sdd_apply: accessing sdd node that has been garbage collected" error (DNF)


# equivalence checking
print(nnf.equiv(dnf))
print((nnf & dnf) | (~nnf & ~dnf))
