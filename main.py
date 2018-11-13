# Local files
from model import *
from data_biochar import *


# Biochar Yield
trainX, trainY, testX, testY = getBioCharYieldData()
train(trainX, trainY, testX, testY, featureExtractor=True)

# Biochar Surface Area
# trainX, trainY, testX, testvY = getBioCharSAData()
# train(trainX, trainY, testX, testY, featureExtractor=True)