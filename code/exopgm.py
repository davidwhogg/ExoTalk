from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

pgm = daft.PGM([3.6, 2.7], origin=[1.15, 0.65])
pgm.add_node(daft.Node("exoplanet", r"exoplanet", 1.8, 2, aspect=2.0))
pgm.add_node(daft.Node("star", r"star", 3, 2, aspect=2.0))
pgm.add_node(daft.Node("camera", r"camera", 4.2, 2, aspect=2.0))
pgm.add_node(daft.Node("data", r"data", 3, 1, aspect=2.0, observed=True))
pgm.add_edge("exoplanet", "data")
pgm.add_edge("star", "data")
pgm.add_edge("camera", "data")
pgm.render()
pgm.figure.savefig("threecauses.pdf")
pgm.figure.savefig("threecauses.png", dpi=150)

