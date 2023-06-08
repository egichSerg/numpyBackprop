import numpy as np

from tqdm import tqdm #for loops

from torchvision.datasets import MNIST
from torch.utils.data import DataLoader

mnistTrainSet = MNIST(root='./train', train=True, download=True, transform=None)
mnistTestSet = MNIST(root='./train', train=False, download=True, transform=None)
#trainLoader =