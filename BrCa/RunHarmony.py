import scanpy as sc
import scanpy.external as sce
import anndata as ad
import pandas as pd
import os
import sys

path_adata = str(sys.argv[1])
path_output = str(sys.argv[2])

adata = ad.read_h5ad(path_adata)
adata.obs['batch'] = pd.Categorical(adata.obs['ImageID'])
# adata.obs['batch'] = adata.obs['batch'].cat.rename_categories({'0': 'sample1', '1': ' sample2'})
sc.tl.pca(adata)
sce.pp.harmony_integrate(adata, 'batch')

adata.write_h5ad(path_output)
