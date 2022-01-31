import matplotlib.pyplot as plt, cmasher as cmr, pandas as pd
import numpy as np, os, sys, networkx as nx, warnings
import mercator, nngt
from itertools import product
from tqdm import tqdm

n = 300
ps = np.linspace(0.5, 0.85, 8)
ks = np.arange(3, 15)
trials = 1
combs = list(product(ps, ks))
for p, k in tqdm(combs):
    for trial in tqdm(range(trials)):
        g = nngt.generation.sparse_clustered(p, n, avg_deg = k).graph.to_undirected()
        #g = nx.watts_strogatz_graph(n, k, p)
        lc = max(nx.connected_components(g), key=len)
        g = g.subgraph(lc)

        fn = f"./watts_{trial=}_{k=}_{p=}_{n=}.edge"
        nx.write_edgelist(g, fn)
        mercator.embed(fn)
