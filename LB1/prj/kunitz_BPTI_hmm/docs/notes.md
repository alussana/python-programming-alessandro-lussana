

# LB1 Module 2 Prj

## Serine Protease BPTI Kunitz-Type Inhibitor

The pancreatic trypsin inhibitor (Kunitz) family is one of the numerous families of serine proteinase inhibitors. They are short (~50 residue) alpha/beta proteins with a molecular weight of 6 kDa. Their fold is constrained by 3 disulphite bonds

Kunitz domains are stable as standalone peptides, and work as competitive protease inhibitors in their free form, recognizing specific protein structures. These properties have led to attempts at developing  biopharmaceutical drugs from Kunitz domains. Candidate domains are selected from molecular libraries containing over 10 million variants with the aid of display techniques like phage display,[11] and can be produced in large scale by genetically engineered organisms.

Our study focuses on the development of a hidden markov model-based binary classification method to predict the presence of BPTI/Kunitz domains in protein where only the covalent structure is known

### Protein Domain Entry Pages

**Family**: Kunitz_BPTI

* [PF00014](https://pfam.xfam.org/family/Kunitz_BPTI)

**Domain**: Kunitz_BPTI

* [IPR002223](http://www.ebi.ac.uk/interpro/entry/IPR002223)

**Superfamily**: Kunitz_BPTI_sf

* [IPR036880](http://www.ebi.ac.uk/interpro/entry/IPR036880)

**Gene Ontology**: serine-type endopeptidase inhibitor activity

* [GO:0004867](https://www.ebi.ac.uk/QuickGO/term/GO:0004867)

### 5pti entry pages

STRUCTURE OF BOVINE PANCREATIC TRYPSIN INHIBITOR. RESULTS OF JOINT NEUTRON AND X-RAY REFINEMENT OF CRYSTAL FORM II

* [PDBe](http://www.ebi.ac.uk/pdbe/entry/pdb/5pti)

* [RCSB_PDB](https://www.rcsb.org/structure/5PTI)

### Secondary Structure

### Fold

Basic structure:

* the 3-dimensional conformation is stabilized by three disulfide bonds

```
            +-----------------------+
            |  +--------+           |
            |  |      **|*******    |
          xxCxxC#xxxCxxxCxxxxxxCxxxxCxx
                    |          |
                    +----------+

            {------50 residues------}

'C': conserved cysteine involved in a disulfide bond.
'#': active site residue.
'*': position of the pattern.
```

This core is the scaffold that supports the convex and exposed canonical binding loop at positions P3–P3' , according to the Pn–Pn' notation of Schechter and Berger (1967). This loop is highly complementary to the
concave protease active site and is, thus, responsible for the extreme stability of the interaction with the target enzyme in a substrate-like manner (Laskowski et al., 2000). Typically, trypsin inhibitors contain Arg/Lys at position P1, whereas chymotrypsin inhibitors have Leu/Met at this position. However, other residues at the primary binding site and within the secondary binding loop (residues 34–39 in BPTI) are also suggested to have significant influence on the association energy (Scheidig et al., 1997; Czapinska et al., 2000; Laskowski et al., 2000).7

The pancreatic trypsin inhibitor (Kunitz) family is one of the numerous families of serine proteinase inhibitors. The members of this family are short (50-60 residues) alpha/beta proteins with a molecular weight of around 6 kDa. Their compact structure includes a hydrophobic core, containing a central $\beta​$-sheet and three disulfide bridges \cite{Fernandez12}. This core is the scaffold that supports the convex and exposed canonical binding loop, that is highly complementary to the concave protease active site and is, thus, responsible for the extreme stability of the interaction with the target enzyme.

Kunitz domains are stable as standalone peptides, and work as competitive protease inhibitors in their free form, recognizing specific protein structures. These properties have led to attempts at developing  biopharmaceutical drugs from Kunitz domains. Candidate domains are selected from molecular libraries containing over 10 million variants with the aid of display techniques like phage display,[11] and can be produced in large scale by genetically engineered organisms.

Our study focuses on the development of a hidden markov model-based binary classification method to predict the presence of BPTI/Kunitz domains in existing proteins where only the covalent structure is known. 

### Supplementary materials

* there are 35 identical sequences among human kunitz structures

`snakemake -p PF00014_pdb.5pti_pdbefold_S100_L1_clust.gz`

`zcat PF00014_pdb.5pti_pdbefold_S100_L1_clust.gz | wc -l`

