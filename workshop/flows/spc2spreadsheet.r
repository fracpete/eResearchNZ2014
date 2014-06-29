library(hyperSpec)
spc = hyperSpec::read.spc("/home/fracpete/documents/conferences/eResearchNZ2014/workshop/data/spc/nir.spc")
data = attr(spc, "data")
v = data[3]
x = as.matrix(v, ncol = 700)