# Biochar linear regression

## Yield
### Linear regression (1 layer)
- All features (Xs) used: MSE 0.38
- Structural components (X1s) omitted: MSE 0.40
- Chemical elements (X2s) omitted: MSE 0.47
- Pyrolysis parameters (X4s) omitted: MSE 0.83
- Particle size (X3) omitted: MSE 0.38

### Linear regression with features extractor neural network
Features used | MSE | R2
---| ---|---
All features (Xs) | 0.0320 | 0.9610
Structural components (X1s) omitted |0.0450|0.9391
Chemical elements (X2s) omitted|0.0267|0.9101
Pyrolysis parameters (X4s) omitted |0.5945|0.2986
Particle size (X3) omitted |0.0424|0.9339

## Surface Area
### Linear regression (1 layer)
- All features used: MSE 0.55
- Structural components (X1s) omitted: MSE 0.67
- Chemical elements (X2s) omitted: MSE 0.63
- Pyrolysis parameters (X4s) omitted: MSE 0.77
- Particle size (X3) omitted: MSE 0.5615

### Linear regression with features extractor neural network
Features used | MSE | R2
---| ---|---
All features (Xs) |0.0097 | 0.9827
Structural components (X1s) omitted | 0.0086 |0.9689
Chemical elements (X2s) omitted|0.0099|0.9864
Pyrolysis parameters (X4s) omitted|0.2835|0.6797
Particle size (X3) omitted|0.0114|0.9911