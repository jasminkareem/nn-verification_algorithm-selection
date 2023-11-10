README
----------------------------------------------------------------------------------------
This is a human readable file meant to allow the creator to explain any and
all peculiarities of how the data came into existence. Most importantly, this file
is where the creators must explain the reason for any missing data in the set.
In addition to this, consider the following as a starting list of things that must
be mentioned in this file. But please be aware that explaining things here is no
excuse to not have perfectly machine-readable information in the other files or
for circumventing format specifications!

----------------------------------------------------------------------------------------
Must describe where and how the data originated.
--------------------------------------------------
The dataset used is of 10000 instances created by MIPVerify for neural network verification.
These were encoded neural networks that were encoded into mip instances as .lp files. 
Features were then extracted from each of these 10k mip instances.
These features are taken from the paper 'Algorithm Runtime Prediction: Methods & evaluation' (2014),
authored by Frank Hutter, Lin Xu, Holger H. Hoos, and Kevin Leyton-Brown. 
The running times, or PAR10s, are taken from the paper 'Speeding up neural network robustness verification 
via algorithm configuration and an optimised mixed integer linear programming solver portfolio' (2022),
authored by Matthias König, Holger H. Hoos, and Jan N. van Rijn. 

--------------------------------------------------
Describe the problem that the algorithms are supposed to solve and how their performance is measured.
--------------------------------------------------
The problem, as mentioned above, is of MIPs generated for neural network verification.
The different algorithms are the different MIP solver configurations described by König et. al
The different algorithms aim to solve the mip instances, with a running time that it takes to solve or timeout.

---------------------------------------------------
Describe the used solvers, their configurations, versions and origins.
---------------------------------------------------
The solver used for the running time data is Gurobi. 
This is also what the MIP solver configurations are based on.
This is done using Hydra (see paper by König et. al above).
The solver used to extract features is CPLEX (see paper by Hutter et. al).

----------------------------------------------------
Reference the feature generator.
----------------------------------------------------
See paper by Hutter et. al mentioned above
