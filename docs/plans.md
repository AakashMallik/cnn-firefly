**Part I** - Feature visualization ✅  
**Part II** - Adversarial Examples -> Use of CPPN to generate images -> Fast Gradient Signum Method  
**Part III** - Memorization and Generalization  

***

## Part I
We will try to observe what the filters learn at different levels of the network:
1. Binary Classifier (Simple)
2. Multi Class Classification (Advanced)

### The network
1. We'll start with a custom network to begin with, something a bit shallow. 
2. Next we'll consider a deeper model to see the granularity of the things

### The Data
We will use **CIFAR-10** for both binary classification and multiclass classification. When we opt for binary class classification, we'll pick one class at radom as our positive class and mix the rest of the images up and label them as negative class. We have to be aware of **class imbalance** in this case.
  
Data can be downloaded from this [link](https://www.kaggle.com/swaroopkml/cifar10-pngs-in-folders).

### Framework and Code
**Pytorch / Pytorch Lightning** written in **Python**.