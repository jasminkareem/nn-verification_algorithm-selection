using MIPVerify
using JuMP
using Gurobi
using MAT


# Get MNIST dataset (10k images)
mnist = MIPVerify.read_datasets("MNIST")

# Import neural network used for MNIST classification
###### Specify the structure of the model ######

# mnistnet
include("mnist_sample_1.jl")
model_path = joinpath("mnist_sample_1.mat")
param_dict = matread(model_path)
n1 = get_mnist_sample_1_network(param_dict, name="mnist_sample_1")



# Specify which samples to extract (full: 1-10k)
#arr = collect(1:10000)
arr = collect(1:1000)
#arr = [
#    1,
#    4
#]


for n in arr
    println(n)
    sample_image = MIPVerify.get_image(mnist.test.images, n)
    target_label_index = MIPVerify.get_label(mnist.test.labels, n) + 1
    d = MIPVerify.find_adversarial_example(n1, sample_image, target_label_index, invert_target_selection=true, 
    GurobiSolver(TimeLimit=60), pp=MIPVerify.LInfNormBoundedPerturbationFamily(0.05), norm_order=Inf, cache_model=false)
    JuMP.writeLP(d[:Model], "mips10k_mnistnet/mip_$n.lp")

end


