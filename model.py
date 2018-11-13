# Packages
from sklearn.preprocessing import StandardScaler
from keras.layers import Input, Dense, Dropout
from keras.models import Model
from keras.optimizers import Adam


def train(trainX=None, trainY=None, testX=None, testY=None, featureExtractor=False, n_y=1):
	# print(trainX)
	sc = StandardScaler()
	trainX = sc.fit_transform(trainX)
	trainY = sc.fit_transform(trainY)
	testX = sc.fit_transform(testX)
	testY = sc.fit_transform(testY)
	n_features = len(trainX[0])
	inputs = Input(shape=(n_features,))
	preds = inputs
	if featureExtractor:
		preds = Dense(128, activation='relu')(preds)
		preds = Dropout(0.1)(preds)
		preds = Dense(256, activation='relu')(preds)
		preds = Dropout(0.1)(preds)
		pres = Dense(128, activation='relu')(preds)
		preds = Dropout(0.1)(preds)
	preds = Dense(n_y, activation='linear')(preds)

	model = Model(inputs=inputs,outputs=preds)
	sgd = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
	model.compile(optimizer=sgd ,loss='mse',metrics=['mse', 'mae'])
	model.fit(trainX, trainY, validation_data=[testX, testY], batch_size=8, epochs=1000, shuffle=True)