# Methodological Knowledge Universe Coverage Map

**Status:** Initial broad construction map  
**Date:** 2026-08-25  
**Authority:** Planning and coverage-routing artifact only. Presence in this map does not make a topic accepted methodological knowledge, establish applicability, or imply production support.  
**Governing framework:** `docs/research/033_methodological_knowledge_universe_construction_framework.md`

## Purpose

This map makes the intended methodological universe visible before the project creates large numbers of reusable knowledge assets.

It answers:

```text
What broad neighborhoods exist?
Which neighborhoods should be decomposed first?
Where is current coverage only nominal?
Where should deep source-backed construction begin?
```

It does not answer:

```text
What is true for a particular project?
Which method is applicable?
Which knowledge is accepted?
Which action is recommended or required?
```

The internal knowledge universe is expected to be cross-linked and many-to-many. This document uses a hierarchy because humans need a navigable projection.

---

## Coverage-depth legend

Coverage depth is deliberately separate from epistemic maturity, source quality, and enforcement authority.

```text
C0  MAPPED
    neighborhood appears in this map

C1  SOURCED
    candidate source bundle has been registered

C2  DECOMPOSED
    canonical concepts and candidate asset/component boundaries identified

C3  OPERATIONALIZED
    important questions, evidence requirements, alternatives, failure modes,
    assumptions, diagnostics, or claim constraints represented

C4  CONNECTED
    important relations and conditional guidance represented

C5  BEHAVIORALLY_TESTED
    representative positive / negative / boundary / failure cases exist

C6  PROJECT_EXPOSED
    knowledge has been exercised in real project trials
```

Current initial state is mostly `C0` by design.

Priority markers:

```text
VS1  first six deep vertical slices
CORE high-priority broad core after the first pressure test
LATER important but not first-wave construction
```

---

# A. Project formulation, purpose, and analytical contract

**Initial depth:** C0  
**Priority:** CORE

```text
A1  project objective and decision context
A2  intended use
A3  deliverables and reporting obligations
A4  target / outcome definition
A5  prediction vs explanation vs description vs decision support
A6  estimand / quantity of interest
A7  unit of observation
A8  population and sampling frame
A9  prediction moment
A10 prediction horizon
A11 intervention / action horizon
A12 constraints and resources
A13 human-control preferences
A14 risk / consequence class
A15 success criteria
A16 baseline and comparator definition
A17 scope exclusions
A18 project completion / stopping criteria
```

Operational knowledge to develop:

```text
question templates
definition requirements
semantic validity checks
claim-scope constraints
objective-dependent method-selection principles
human clarification hooks
```

Cross-links expected to:

```text
validation
metrics
calibration
causal inference
risk / assurance
deployment
reporting
```

---

# B. Data provenance, semantics, and data-generating process

**Initial depth:** C0  
**Priority:** CORE

```text
B1  data source and lineage
B2  data collection process
B3  measurement process
B4  sampling / inclusion mechanism
B5  survivorship / selection mechanisms
B6  observational vs experimental data
B7  retrospective vs prospective data
B8  entity identity and repeated entities
B9  temporal ordering and timestamps
B10 spatial structure
B11 hierarchical / clustered structure
B12 panel / longitudinal structure
B13 label-generation process
B14 proxy targets
B15 measurement error
B16 censoring / truncation
B17 delayed labels
B18 data joins and multi-source integration
B19 feature availability timing
B20 schema and semantic variable roles
B21 data version / snapshot semantics
```

Operational knowledge to develop:

```text
source-of-data questions
lineage evidence requirements
information-legitimacy checks
measurement failure modes
selection-bias warnings
prediction-time feature eligibility
```

---

# C. Data quality and missingness

**Initial depth:** C0  
**Priority:** `VS1` for Missing Data, CORE for the rest

```text
C1  missing feature values                         VS1
C2  missing target labels                          VS1
C3  structural missingness                         VS1
C4  informative missingness                        VS1
C5  missingness indicators                         VS1
C6  complete-case analysis                         VS1
C7  simple imputation                              VS1
C8  model-based imputation                         VS1
C9  multiple imputation                            VS1/LATER
C10 native model missing-value handling            VS1
C11 production missingness regime                  VS1
C12 evaluation with missing labels                 VS1
C13 duplicates
C14 impossible / invalid values
C15 inconsistent categories
C16 data-type errors
C17 range and constraint violations
C18 natural vs unnatural outliers
C19 anomaly detection for data quality
C20 corrupted observations
C21 inconsistent units
C22 schema drift
C23 label noise
C24 covariate measurement error
C25 data reconciliation across sources
```

Expected Missing Data knowledge roles:

```text
framework / concern
question templates
strategy alternatives
evidence requirements
selection-bias failure modes
information-legitimacy constraints
production-regime reasoning
claim limitations
```

---

# D. Exploratory and descriptive analysis

**Initial depth:** C0  
**Priority:** CORE

```text
D1  dataset orientation and shape
D2  univariate numeric summaries
D3  robust location / scale summaries
D4  categorical frequency analysis
D5  target distribution
D6  histogram
D7  ECDF
D8  density estimation for EDA
D9  box / violin / quantile views
D10 bivariate numeric association
D11 categorical association
D12 target-conditional distributions
D13 multivariate relationships
D14 correlation analysis
D15 nonlinear association
D16 mutual information for exploration
D17 subgroup exploration
D18 temporal EDA
D19 seasonality exploration
D20 trend and structural change exploration
D21 missingness patterns
D22 outlier exploration
D23 entity-level longitudinal exploration
D24 train/validation/test distribution comparison
D25 dimensionality exploration
D26 visualization selection
D27 multiplicity / exploratory overinterpretation cautions
```

Operational knowledge to develop:

```text
which question a visualization answers
interpretation limits
redundancy / clutter guidance
follow-up triggers
failure modes such as treating exploratory patterns as confirmed claims
```

---

# E. Validation, evaluation design, and generalization

**Initial depth:** C0  
**Priority:** `VS1`

```text
E1  train / validation / test separation                         VS1
E2  final-test protection                                        VS1
E3  holdout evaluation                                           VS1
E4  k-fold cross-validation                                      VS1
E5  repeated cross-validation                                    VS1
E6  stratified splitting                                         VS1
E7  grouped splitting                                            VS1
E8  StratifiedGroup-style splitting                              VS1
E9  nested cross-validation                                      VS1
E10 temporal holdout                                             VS1
E11 rolling / walk-forward validation                            VS1
E12 expanding-window validation                                  VS1
E13 sliding-window validation                                    VS1
E14 grouped-temporal validation                                  VS1
E15 spatial validation                                           LATER
E16 blocked / clustered validation                               CORE
E17 bootstrap-based performance assessment                       CORE
E18 repeated-entity generalization regimes                       VS1
E19 unseen-entity generalization                                 VS1
E20 future-known-entity generalization                           VS1
E21 mixed known/unseen deployment                                VS1
E22 distribution-shift-aware validation                          CORE
E23 validation sample-size / precision reasoning                 CORE
E24 multiple model / hyperparameter comparison bias              VS1
E25 validation as simulation of evaluation                       VS1
E26 evaluation as simulation of intended use                     VS1
E27 preprocessing within evaluation boundaries                   VS1
E28 feature selection within evaluation boundaries               VS1
E29 calibration within evaluation boundaries                     VS1
E30 threshold tuning within evaluation boundaries                VS1
E31 HPO within evaluation boundaries                             VS1
E32 model-selection uncertainty                                  CORE
E33 repeated random seeds / algorithmic variability              CORE
E34 leakage detection in validation                              VS1
E35 benchmark / external test-set reuse                          CORE
```

Expected knowledge roles:

```text
generalization-regime concepts
hard information-boundary rules
question templates
method alternatives
evidence requirements
claim constraints
sequencing/dependency relations
```

---

# F. Preprocessing and representation

**Initial depth:** C0  
**Priority:** CORE

```text
F1  categorical encoding
F2  one-hot encoding
F3  ordinal encoding
F4  target / supervised encoding
F5  high-cardinality categorical handling
F6  numeric scaling
F7  standardization
F8  normalization
F9  robust scaling
F10 whitening
F11 monotonic transformations
F12 log / power transforms
F13 winsorization / clipping
F14 discretization / binning
F15 text representation basics
F16 learned representation transforms
F17 preprocessing pipelines
F18 training-only fitting of learned transforms
F19 inverse transformations
F20 data-type-specific preprocessing
F21 model-specific preprocessing requirements
F22 sparse vs dense representation
```

Cross-links expected to:

```text
information legitimacy
validation
model families
feature engineering
missing data
interpretability
```

---

# G. Feature engineering and feature eligibility

**Initial depth:** C0  
**Priority:** CORE

```text
G1  prediction-time feature eligibility
G2  feature availability timing
G3  leakage-prone features
G4  target-derived features
G5  post-outcome features
G6  aggregate features
G7  lagged features
G8  rolling-window features
G9  interaction features
G10 polynomial features
G11 ratio / difference features
G12 domain transformations
G13 temporal calendar features
G14 cyclic encoding
G15 entity-history features
G16 group aggregates
G17 cross-fitting for learned feature construction
G18 feature lineage
G19 feature stability
G20 feature reproducibility
G21 feature semantics and proxy risk
```

---

# H. Feature selection and dimensionality reduction

**Initial depth:** C0  
**Priority:** `VS1` for feature selection, CORE for dimensionality reduction

```text
H1  feature selection vs dimensionality reduction                VS1
H2  low-variance filtering                                       VS1
H3  univariate score filtering                                   VS1
H4  chi-square feature selection                                 VS1
H5  ANOVA / F-score selection                                    VS1
H6  mutual-information selection                                 VS1
H7  SelectKBest / percentile-style selection                     VS1
H8  recursive feature elimination                                VS1
H9  RFECV-style selection                                        VS1
H10 model-based selection                                        VS1
H11 L1 / sparsity-based selection                                VS1
H12 tree-importance-based selection                              VS1
H13 permutation-importance-based selection                       VS1
H14 wrapper search                                               VS1
H15 stability selection                                          LATER
H16 leakage-safe feature-selection pipelines                     VS1
H17 selection inside cross-validation                            VS1
H18 selection uncertainty / instability                          VS1
H19 interpretability tradeoffs                                   VS1
H20 redundancy and correlated features                           VS1
H21 PCA                                                          CORE
H22 sparse PCA                                                   LATER
H23 truncated SVD                                                CORE
H24 supervised dimensionality reduction                          LATER
H25 manifold learning                                            LATER
H26 autoencoder representation reduction                         LATER
```

Expected knowledge roles:

```text
method families
comparison relations
pipeline constraints
evaluation requirements
tradeoff principles
interpretability implications
```

---

# I. Supervised learning foundations

**Initial depth:** C0  
**Priority:** CORE

```text
I1  supervised learning framing
I2  classification
I3  regression
I4  probabilistic prediction
I5  ranking
I6  multi-class classification
I7  multi-label prediction
I8  multi-output regression
I9  loss functions
I10 empirical risk minimization
I11 inductive bias
I12 bias-variance tradeoff
I13 underfitting / overfitting
I14 regularization
I15 model capacity
I16 parametric vs nonparametric modeling
I17 generative vs discriminative classification
I18 optimization vs generalization
I19 baseline modeling
I20 model-family comparison
```

---

# J. Linear and generalized linear models

**Initial depth:** C0  
**Priority:** CORE

```text
J1  ordinary least squares
J2  linear regression assumptions
J3  logistic regression
J4  multinomial logistic regression
J5  generalized linear model concepts
J6  regularized linear models
J7  ridge / L2 regularization
J8  lasso / L1 regularization
J9  elastic net
J10 interaction / basis expansion
J11 nonlinear transforms in linear predictors
J12 separation in logistic regression
J13 coefficient interpretation
J14 multicollinearity
J15 robust standard errors where inferentially relevant
J16 sparse high-dimensional regimes
```

---

# K. Nearest-neighbor and instance-based methods

**Initial depth:** C0  
**Priority:** CORE

```text
K1  k-nearest-neighbor classification
K2  k-nearest-neighbor regression
K3  distance metrics
K4  scaling sensitivity
K5  neighborhood size
K6  curse of dimensionality
K7  local methods / decision boundaries
K8  computational scaling
```

---

# L. Probabilistic classifiers

**Initial depth:** C0  
**Priority:** CORE

```text
L1  Bernoulli / categorical probabilistic classification
L2  Naive Bayes
L3  conditional independence assumption
L4  Gaussian Naive Bayes
L5  smoothing / pseudo-counts
L6  logistic probabilistic outputs
L7  generative vs discriminative modeling
L8  likelihood and log loss
L9  probability quality vs class decision
L10 model uncertainty vs predictive probability caveats
```

---

# M. Support-vector and margin methods

**Initial depth:** C0  
**Priority:** CORE

```text
M1  maximum-margin classification
M2  hard margin
M3  soft margin
M4  hinge loss
M5  regularization parameter
M6  kernels
M7  RBF kernel
M8  feature scaling
M9  high-dimensional behavior
M10 probability calibration of margin models
```

---

# N. Tree models and ensembles

**Initial depth:** C0  
**Priority:** `VS1`

```text
N1  decision trees                                         VS1
N2  regression trees                                       VS1
N3  classification trees                                   VS1
N4  decision stumps                                        VS1
N5  splitting criteria                                     VS1
N6  tree depth / capacity                                  VS1
N7  pruning                                                VS1
N8  tree overfitting                                       VS1
N9  model ensembles                                        VS1
N10 bagging                                                VS1
N11 bootstrap aggregation                                 VS1
N12 Random Forest                                         VS1
N13 random feature subsampling                            VS1
N14 Extra Trees                                           VS1
N15 boosting                                              VS1
N16 AdaBoost                                              VS1
N17 gradient boosting                                     VS1
N18 gradient-boosted tree families                        VS1
N19 bagging vs boosting                                   VS1
N20 bias / variance effects of ensembles                  VS1
N21 class imbalance interactions                          VS1
N22 probability calibration of tree ensembles             VS1
N23 feature importance caveats                            VS1
N24 permutation importance                                VS1
N25 partial dependence / accumulated effects               CORE
N26 computational / parallelization considerations        VS1
```

Expected knowledge roles:

```text
method / concept network
mechanism components
bias-variance concepts
alternative relations
configuration semantics
failure modes
interpretation caveats
```

---

# O. Neural networks and deep learning

**Initial depth:** C0  
**Priority:** LATER after supervised core

```text
O1  feedforward networks
O2  multilayer perceptrons
O3  activations
O4  backpropagation
O5  automatic differentiation
O6  minibatch optimization
O7  SGD variants
O8  optimization stability
O9  initialization
O10 vanishing / exploding gradients
O11 normalization layers
O12 dropout
O13 weight decay
O14 early stopping
O15 convolutional networks
O16 recurrent neural networks
O17 LSTM / gated recurrence
O18 attention
O19 transformers
O20 transfer learning
O21 pretrained representations
O22 deep probabilistic outputs
O23 deep-model calibration
O24 generative deep models
O25 model/data/compute regime considerations
```

---

# P. Hyperparameter optimization and model search

**Initial depth:** C0  
**Priority:** CORE

```text
P1  hyperparameter definition
P2  grid search
P3  random search
P4  Bayesian optimization
P5  successive halving / resource allocation
P6  early stopping in HPO
P7  search-space design
P8  conditional hyperparameters
P9  HPO within validation
P10 nested evaluation of model search
P11 multiple-testing / winner's-curse effects
P12 reproducibility of search
P13 computational budgets
P14 model-family search
```

---

# Q. Metrics and performance evaluation

**Initial depth:** C0  
**Priority:** `VS1` for classification/decision metrics, CORE otherwise

```text
Q1  metric selection by project objective                     VS1
Q2  classification error / accuracy                           VS1
Q3  confusion matrix                                          VS1
Q4  sensitivity / recall                                      VS1
Q5  specificity                                               VS1
Q6  precision                                                 VS1
Q7  F-score                                                   VS1
Q8  ROC curve                                                 VS1
Q9  ROC-AUC                                                   VS1
Q10 precision-recall curve                                    VS1
Q11 PR-AUC / average precision                                VS1
Q12 balanced accuracy                                         VS1
Q13 cost-sensitive evaluation                                 VS1
Q14 prevalence effects                                        VS1
Q15 macro / micro / weighted aggregation                      CORE
Q16 regression MAE                                            CORE
Q17 regression MSE / RMSE                                     CORE
Q18 R-squared and explanatory limits                          CORE
Q19 quantile / pinball loss                                   LATER
Q20 ranking metrics                                           LATER
Q21 metric uncertainty                                        CORE
Q22 subgroup metrics                                          CORE
Q23 confidence intervals for performance                      CORE
Q24 comparative performance tests                             LATER
```

---

# R. Class imbalance, probability calibration, and threshold decisions

**Initial depth:** C0  
**Priority:** `VS1`

```text
R1  class prevalence                                          VS1
R2  imbalance as an evaluation problem                        VS1
R3  majority-class baselines                                  VS1
R4  class weighting                                           VS1
R5  random under-sampling                                     VS1
R6  random over-sampling                                      VS1
R7  synthetic resampling                                      VS1
R8  resampling inside validation                              VS1
R9  effect of resampling on probability interpretation        VS1
R10 probability calibration                                  VS1
R11 calibration curves / reliability diagrams                VS1
R12 Brier score                                               VS1
R13 log loss as probability-quality metric                    VS1
R14 Platt / sigmoid calibration                               VS1
R15 isotonic calibration                                     VS1
R16 calibration evaluation split                             VS1
R17 threshold selection                                      VS1
R18 operating-point choice                                   VS1
R19 expected-cost thresholding                               VS1
R20 asymmetric error costs                                   VS1
R21 human / stakeholder threshold choice                     VS1
R22 ranking quality vs probability quality                   VS1
R23 thresholded decision quality                             VS1
R24 prevalence / prior shift and calibration                 VS1
```

Expected knowledge roles:

```text
cross-cutting concepts
metric-purpose distinctions
conditional guidance
human decision hooks
relations among resampling, calibration, and thresholding
```

---

# S. Uncertainty and statistical reliability

**Initial depth:** C0  
**Priority:** CORE

```text
S1  sampling uncertainty
S2  algorithmic randomness
S3  confidence intervals
S4  bootstrap inference
S5  prediction intervals
S6  predictive uncertainty
S7  parameter uncertainty
S8  epistemic vs aleatoric framing where useful
S9  repeated-run variability
S10 uncertainty under model selection
S11 multiple comparisons
S12 uncertainty under missing labels
S13 uncertainty communication
S14 probabilistic uncertainty caveats
```

---

# T. Diagnostics and model criticism

**Initial depth:** C0  
**Priority:** CORE

```text
T1  residual analysis
T2  normality diagnostics where relevant
T3  heteroskedasticity
T4  autocorrelation
T5  functional-form misspecification
T6  influence / leverage
T7  multicollinearity
T8  classification error analysis
T9  subgroup error analysis
T10 calibration diagnostics
T11 learning curves
T12 bias / variance diagnosis
T13 train-validation gap
T14 residual dependence
T15 model instability
T16 data leakage diagnostics
T17 error slicing
T18 adversarial / stress cases
```

---

# U. Robustness and sensitivity

**Initial depth:** C0  
**Priority:** CORE

```text
U1  robustness across seeds
U2  robustness across splits
U3  robustness across preprocessing choices
U4  robustness across plausible model families
U5  sensitivity to influential observations
U6  sensitivity to missing-data assumptions
U7  sensitivity to threshold choice
U8  subgroup robustness
U9  temporal robustness
U10 distribution-shift stress tests
U11 perturbation / noise sensitivity
U12 specification sensitivity
U13 negative controls where relevant
U14 ablation analysis
```

---

# V. Interpretability and explanation

**Initial depth:** C0  
**Priority:** CORE

```text
V1  coefficient interpretation
V2  feature importance
V3  permutation importance
V4  impurity-based importance caveats
V5  partial dependence
V6  ICE
V7  accumulated local effects
V8  local explanation methods
V9  SHAP-family methods
V10 surrogate models
V11 counterfactual explanations
V12 explanation stability
V13 predictive association vs causal interpretation
V14 explanation scope / claim constraints
```

---

# W. Time-series foundations and stochastic structure

**Initial depth:** C0  
**Priority:** `VS1`

```text
W1  stochastic process / time-series definition                 VS1
W2  temporal dependence                                         VS1
W3  white noise                                                 VS1
W4  random walk                                                 VS1
W5  weak stationarity                                           VS1
W6  strict stationarity                                         LATER
W7  autocovariance                                              VS1
W8  autocorrelation / ACF                                       VS1
W9  partial autocorrelation / PACF                              VS1
W10 lag operator                                                VS1
W11 Wold representation                                        VS1
W12 AR processes                                               VS1
W13 MA processes                                               VS1
W14 ARMA processes                                             VS1
W15 stability / stationarity of AR dynamics                    VS1
W16 invertibility / identification of MA dynamics              VS1
W17 ARIMA / integration                                        VS1
W18 differencing                                               VS1
W19 deterministic trends                                      VS1
W20 seasonal structure                                        CORE
W21 structural breaks                                         CORE
W22 unit roots                                                VS1
W23 ADF / unit-root testing                                   VS1
W24 break-aware stationarity testing                          LATER
W25 spurious regression                                       VS1
W26 cointegration                                             VS1
W27 Engle-Granger testing                                     VS1
W28 error-correction models                                   VS1
W29 ADL / distributed-lag models                              VS1
W30 long-run multipliers                                      VS1
W31 VAR                                                        CORE
W32 VECM                                                       CORE
W33 Granger causality                                         VS1
W34 impulse response functions                                VS1
W35 forecast construction                                    VS1
W36 forecast uncertainty                                     VS1
W37 forecast horizons                                        VS1
W38 rolling / expanding evaluation                           VS1
W39 time-series model selection                              VS1
W40 information criteria                                    VS1
W41 forecast comparison                                     VS1
W42 dynamic-model residual diagnostics                       VS1
```

Expected knowledge roles:

```text
specialized mathematical concepts
assumptions and identification conditions
model-family relations
testing / modeling dependencies
forecasting methods
validation constraints
dynamic interpretation
```

---

# X. Longitudinal, panel, and hierarchical data

**Initial depth:** C0  
**Priority:** LATER

```text
X1  repeated-measures structure
X2  panel data
X3  pooled models
X4  fixed effects
X5  random effects
X6  first differences
X7  between estimators
X8  two-way fixed effects
X9  clustered standard errors
X10 hierarchical / multilevel models
X11 within vs between variation
X12 entity/time leakage
X13 panel validation regimes
X14 dynamic panels
```

---

# Y. Causal inference and experimental design

**Initial depth:** C0  
**Priority:** LATER, high consequence

```text
Y1  prediction vs causation
Y2  causal estimand
Y3  potential outcomes
Y4  confounding
Y5  DAG concepts
Y6  randomized experiments
Y7  observational identification
Y8  backdoor adjustment
Y9  propensity scores
Y10 matching / weighting
Y11 instrumental variables
Y12 regression discontinuity
Y13 difference-in-differences
Y14 synthetic controls
Y15 heterogeneous treatment effects
Y16 mediation
Y17 sensitivity to unobserved confounding
Y18 post-treatment variables
Y19 collider bias
Y20 causal validation / falsification
```

---

# Z. Survival and event-time methods

**Initial depth:** C0  
**Priority:** LATER

```text
Z1  time-to-event outcome
Z2  censoring
Z3  Kaplan-Meier
Z4  hazard function
Z5  Cox proportional hazards
Z6  proportional-hazards assumption
Z7  parametric survival models
Z8  competing risks
Z9  time-dependent covariates
Z10 survival evaluation metrics
Z11 calibration for event-time predictions
```

---

# AA. Unsupervised learning and density structure

**Initial depth:** C0  
**Priority:** LATER

```text
AA1 clustering task definition
AA2 k-means
AA3 hierarchical clustering
AA4 mixture models
AA5 DBSCAN / density clustering
AA6 cluster validation
AA7 distance / scaling sensitivity
AA8 density estimation
AA9 Gaussian mixtures
AA10 EM algorithm
AA11 anomaly detection
AA12 unsupervised representation evaluation
```

---

# AB. Representation learning and matrix methods

**Initial depth:** C0  
**Priority:** LATER

```text
AB1 PCA
AB2 SVD
AB3 matrix factorization
AB4 embeddings
AB5 recommender systems
AB6 collaborative filtering
AB7 implicit vs explicit feedback
AB8 cold start
AB9 low-rank approximation
AB10 sparse matrix factorization
AB11 representation quality
```

---

# AC. Sequential models and sequence learning

**Initial depth:** C0  
**Priority:** LATER

```text
AC1 sequence task framing
AC2 Markov models
AC3 hidden Markov models
AC4 recurrent neural networks
AC5 LSTM / gated sequence models
AC6 sequence-to-sequence
AC7 causal sequence modeling
AC8 self-attention
AC9 positional information
AC10 transformers
AC11 masking
AC12 autoregressive modeling
AC13 sequence validation
```

---

# AD. Natural language processing

**Initial depth:** C0  
**Priority:** LATER

```text
AD1 text task framing
AD2 tokenization
AD3 bag of words / count representations
AD4 TF-IDF
AD5 word embeddings
AD6 contextual embeddings
AD7 text classification
AD8 language modeling
AD9 sequence labeling
AD10 retrieval
AD11 information extraction
AD12 evaluation for generative text
AD13 text leakage / duplication
AD14 domain shift in language
```

---

# AE. Computer vision and image data

**Initial depth:** C0  
**Priority:** LATER

```text
AE1 image task framing
AE2 image preprocessing
AE3 convolutional models
AE4 transfer learning
AE5 augmentation
AE6 object detection
AE7 segmentation
AE8 image leakage / duplicate detection
AE9 spatial invariances
AE10 vision evaluation
AE11 dataset shift
```

---

# AF. Audio and speech data

**Initial depth:** C0  
**Priority:** LATER

```text
AF1 waveform / spectrogram representation
AF2 speech recognition
AF3 forced alignment
AF4 phonetic / pronunciation analysis
AF5 audio augmentation
AF6 sequence timing
AF7 speaker / environment shift
AF8 transcription evaluation
AF9 audio leakage and duplicate speakers
```

---

# AG. Graph and relational data

**Initial depth:** C0  
**Priority:** LATER

```text
AG1 graph task framing
AG2 node / edge / graph prediction
AG3 graph sampling
AG4 relational leakage
AG5 graph embeddings
AG6 graph neural networks
AG7 link prediction
AG8 temporal graphs
AG9 graph evaluation splits
```

---

# AH. Spatial and geospatial methods

**Initial depth:** C0  
**Priority:** LATER

```text
AH1 spatial dependence
AH2 coordinate systems / geospatial semantics
AH3 spatial feature engineering
AH4 spatial autocorrelation
AH5 spatial validation
AH6 interpolation
AH7 geostatistical methods
AH8 spatial leakage
AH9 map-based interpretation
```

---

# AI. Reinforcement learning and sequential decision-making

**Initial depth:** C0  
**Priority:** LATER

```text
AI1 state / action / reward framing
AI2 Markov decision processes
AI3 policy
AI4 value functions
AI5 Q-learning
AI6 policy gradients
AI7 exploration / exploitation
AI8 off-policy vs on-policy learning
AI9 simulation environments
AI10 reward design
AI11 evaluation and safety
```

---

# AJ. Deployment and productionization

**Initial depth:** C0  
**Priority:** CORE after first modeling core

```text
AJ1 inference contract
AJ2 batch vs online inference
AJ3 prediction-time data availability
AJ4 preprocessing parity
AJ5 model serialization
AJ6 reproducible environments
AJ7 latency / throughput constraints
AJ8 resource constraints
AJ9 failure handling
AJ10 fallback behavior
AJ11 versioning
AJ12 shadow / canary evaluation
AJ13 decision integration
AJ14 human-in-the-loop deployment
```

---

# AK. Monitoring, drift, and revalidation

**Initial depth:** C0  
**Priority:** CORE after deployment core

```text
AK1 data-quality monitoring
AK2 feature-distribution drift
AK3 label / target drift
AK4 concept drift
AK5 performance monitoring
AK6 calibration drift
AK7 subgroup drift
AK8 delayed-label monitoring
AK9 alert thresholds
AK10 model staleness
AK11 retraining triggers
AK12 revalidation
AK13 rollback
AK14 knowledge-triggered project revalidation
```

---

# AL. Admissibility, ethics, fairness, privacy, and governance

**Initial depth:** C0  
**Priority:** CORE conceptually, detailed policies later

```text
AL1 admissible objective
AL2 data-use legitimacy
AL3 privacy constraints
AL4 sensitive attributes
AL5 fairness objectives
AL6 subgroup harms
AL7 proxy discrimination
AL8 consent / purpose limitation
AL9 explainability requirements
AL10 human authority / approval
AL11 auditability
AL12 legal / regulatory constraints
AL13 security / misuse constraints
AL14 prohibited analyses / outputs
AL15 risk acceptance
```

This neighborhood should be governed by appropriate authoritative policy/standards sources rather than generic methodological material alone.

---

# AM. Risk-sensitive assurance and review

**Initial depth:** C0  
**Priority:** CORE conceptually

```text
AM1 consequence / risk classification
AM2 independent review triggers
AM3 replication
AM4 robustness requirements
AM5 subgroup assurance
AM6 uncertainty requirements
AM7 human approval requirements
AM8 evidence sufficiency by risk
AM9 epistemic single points of failure
AM10 assurance debt
AM11 challenge / red-team review
AM12 monitoring obligations by risk
```

---

# AN. Reporting, reproducibility, and communication

**Initial depth:** C0  
**Priority:** CORE

```text
AN1 analytical narrative
AN2 methods reporting
AN3 data provenance reporting
AN4 validation reporting
AN5 metric interpretation
AN6 uncertainty reporting
AN7 limitations
AN8 negative results
AN9 model cards / structured model documentation
AN10 reproducible code and environments
AN11 experiment provenance
AN12 decision provenance
AN13 figure / table standards
AN14 stakeholder communication
AN15 technical vs executive reporting
AN16 artifact packaging
```

---

# AO. Software, implementation, and execution-method knowledge

**Initial depth:** C0  
**Priority:** LATER and explicitly separate from methodology

```text
AO1 execution capability metadata
AO2 library-specific implementations
AO3 API/version behavior
AO4 computational complexity
AO5 hardware acceleration
AO6 parallelization
AO7 memory constraints
AO8 numerical stability
AO9 reproducibility settings
AO10 implementation pitfalls
```

This neighborhood must remain distinct from the methodological identity of a method. For example, `Random Forest` methodological knowledge is not the same object as a scikit-learn execution adapter.

---

# AP. Knowledge-system meta-methodology

**Initial depth:** C0  
**Priority:** CORE for ADS construction

```text
AP1 source provenance
AP2 source freshness
AP3 knowledge revision
AP4 maturity / governance state
AP5 scope confidence
AP6 duplicate detection
AP7 contradiction handling
AP8 counterexample preservation
AP9 behavioral knowledge tests
AP10 project-derived knowledge proposals
AP11 coverage-gap tracking
AP12 accepted vs candidate authority
AP13 deprecation / supersession
AP14 knowledge-change blast radius
AP15 human review / acceptance
```

This neighborhood describes the methodology of maintaining the methodological universe itself.

---

## First vertical-slice program

The first deep construction cycle intentionally spans six structurally different neighborhoods:

| Slice | Main coverage nodes | Why it pressure-tests the representation |
| --- | --- | --- |
| Validation | E1-E35 plus linked A/B/F/H/P/Q/R nodes | Questions, hard boundaries, method alternatives, claim validity, sequencing |
| Missing Data | C1-C12 plus linked B/E/F/S nodes | Branching concern, project context, strategy alternatives, claim limitations |
| Feature Selection | H1-H20 plus linked E/F/G/P/V nodes | Method taxonomy, pipeline boundaries, comparison logic, interpretability |
| Tree Ensembles | N1-N26 plus linked I/P/Q/R/V nodes | Model mechanisms, reusable concepts, method relations, configuration semantics |
| Imbalance / Metrics / Calibration | Q1-Q15 and R1-R24 | Cross-cutting decision semantics, metrics, probability quality, thresholding |
| Time Series | W1-W42 plus linked E/T/U/X nodes | Specialized mathematical concepts, dependencies, diagnostics, forecasting |

All six begin at `C0` in this map. The first pressure test will move them toward C1-C5 selectively rather than declaring the entire slice complete at once.

---

## Cross-cutting concepts that should likely become canonical early

These concepts recur across many neighborhoods and are strong candidates for early independent identity:

```text
intended use
unit of observation
population
sampling frame
prediction moment
prediction horizon
generalization regime
feature availability time
information legitimacy
data leakage
overfitting
underfitting
bias-variance tradeoff
regularization
sampling variability
distribution shift
class prevalence
probability calibration
threshold
error cost
uncertainty
model capacity
validation boundary
final-test protection
```

This is a candidate list for decomposition, not an accepted asset registry.

---

## Coverage-map update rule

Update this map when:

```text
a major methodological neighborhood is discovered missing
a neighborhood is decomposed enough to change coverage depth
a vertical slice expands materially
a project exposes a meaningful coverage gap
a previously broad node must be split for navigability
```

Do not update it merely because one narrative paragraph or one minor method was added.

The map should remain broad enough to navigate and concise enough that coverage gaps remain visible.

---

## Immediate next movement

```text
COVERAGE MAP C0
    -> register source bundles for six VS1 slices
    -> decompose candidate concepts/assets/components
    -> attach proposition-level provenance
    -> identify relations/rules
    -> create behavioral cases
    -> record representation defects
    -> revise construction architecture before broad bulk acceptance
```

The next milestone is not "finish the map." The map is an evolving view over the construction program.
