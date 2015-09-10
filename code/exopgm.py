from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

foo = [4., 3.]
origin = [1., 0.4]
pgm = daft.PGM(foo, origin=origin)
pgm.add_node(daft.Node("exoplanet", r"exoplanet", 3, 2, aspect=2.0))
pgm.add_node(daft.Node("data", r"data", 3, 1, aspect=2.0, observed=True))
pgm.add_edge("exoplanet", "data")
pgm.render()
pgm.figure.savefig("onecause.pdf")
pgm.figure.savefig("onecause.png", dpi=150)

pgm.add_node(daft.Node("star", r"star", 1.8, 2, aspect=2.0))
pgm.add_node(daft.Node("camera", r"camera", 4.2, 2, aspect=2.0))
pgm.add_edge("star", "data")
pgm.add_edge("camera", "data")
pgm.render()
pgm.figure.savefig("threecauses.pdf")
pgm.figure.savefig("threecauses.png", dpi=150)

pgm.add_node(daft.Node("exopop", r"exopop", 3, 3, aspect=2.0))
pgm.add_node(daft.Node("starpop", r"starpop", 1.8, 3, aspect=2.0))
pgm.add_node(daft.Node("spacecraft", r"s/c", 4.2, 3, aspect=2.0))
pgm.add_edge("exopop", "exoplanet")
pgm.add_edge("starpop", "star")
pgm.add_edge("star", "exoplanet")
pgm.add_edge("spacecraft", "camera")
pgm.add_plate(daft.Plate([1.2, 0.5, 3.6, 2.], label=r"light curves"))
pgm.render()
pgm.figure.savefig("morecauses.pdf")
pgm.figure.savefig("morecauses.png", dpi=150)

pgm2 = daft.PGM(foo, origin=origin)
pgm2.add_node(daft.Node("kittens", r"kittens?", 3, 2, aspect=2.0))
pgm2.add_node(daft.Node("data", r"data", 3, 1, aspect=2.0, observed=True))
pgm2.add_edge("kittens", "data")
pgm2.render()
pgm2.figure.savefig("onecause2.pdf")
pgm2.figure.savefig("onecause2.png", dpi=150)
