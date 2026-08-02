# Engineering Practice Roadmap

> A structured collection of short engineering challenges and larger systems projects for building production-oriented capability.

## Contents

- [Philosophy](#philosophy)
- [Group 1: Engineering Challenges](#group-1-engineering-challenges)
  - [A. Data Science and Machine Learning](#a-data-science--machine-learning)
    - [A1. Foundational Algorithms](#a1-foundational-algorithms-rebuild-verify-compare)
    - [A2. Specialized Library Laboratories](#a2-specialized-library-laboratories)
    - [A3. Applied Problem Families](#a3-applied-problem-families-and-typical-solution-methods)
    - [A4. Language and Runtime Implementations](#a4-language-and-runtime-implementations)
  - [B. Programming](#b-programming)
    - [B1. Fundamental CS Problems](#b1-fundamental-cs-through-concrete-problems)
    - [B2. Core Components From Scratch](#b2-core-components-from-scratch)
    - [B3. Language and Framework Laboratories](#b3-language-and-framework-laboratories)
    - [B4. Application Problem Families](#b4-application-problem-families)
    - [B5. Architecture and Distributed Systems](#b5-architecture-and-distributed-system-problems)
    - [B6. Security and Trust Boundaries](#b6-security-and-trust-boundary-problems)
    - [B7. Maintenance, Quality, and Performance](#b7-maintenance-quality-and-performance-problems)
  - [C. Infrastructure](#c-infrastructure)
    - [C1. Runtime and Containers](#c1-runtime-and-container-problems)
    - [C2. Networking and Traffic Management](#c2-networking-and-traffic-management-problems)
    - [C3. CI/CD and Release Engineering](#c3-cicd-and-release-engineering-problems)
    - [C4. Infrastructure as Code and Configuration](#c4-infrastructure-as-code-and-configuration-problems)
    - [C5. Observability and Incident Response](#c5-observability-and-incident-response-problems)
    - [C6. Stateful Infrastructure and Recovery](#c6-stateful-infrastructure-and-recovery-problems)
    - [C7. Orchestration, Capacity, and Resilience](#c7-orchestration-capacity-and-resilience-problems)
    - [C8. Infrastructure Security and Governance](#c8-infrastructure-security-and-governance-problems)
  - [D. Mathematical Foundations and Computational Verification](#d-mathematical-foundations-and-computational-verification)
    - [D1. Linear Algebra and Geometry](#d1-linear-algebra-and-geometry)
    - [D2. Calculus and Numerical Analysis](#d2-calculus-and-numerical-analysis)
    - [D3. Probability and Statistics](#d3-probability-and-statistics)
    - [D4. Optimization and Operations Research](#d4-optimization-and-operations-research)
    - [D5. Discrete Mathematics and Theoretical CS](#d5-discrete-mathematics-and-theoretical-computer-science)
    - [D6. Information Theory, Signals, and Transforms](#d6-information-theory-signals-and-transforms)
    - [D7. Dynamical Systems, Stochastic Processes, and Control](#d7-dynamical-systems-stochastic-processes-and-control)
    - [D8. Numerical Reliability and Mathematical Verification](#d8-numerical-reliability-and-mathematical-verification)
    - [Mathematical Verification Ladder](#mathematical-verification-ladder)
    - [Selective Reimplementation Checklist](#selective-reimplementation-checklist)
    - [Boundary with the Engineering Sections](#boundary-with-the-engineering-sections)
- [Group 2: Integrated Systems Programs](#group-2-integrated-systems-programs)
  - [A. Domain Programs](#a-domain-programs)
    - [Marketing Intelligence as a Component Ecosystem](#marketing-intelligence-as-a-component-ecosystem)
    - [Job Opportunity Intelligence as a Component Ecosystem](#job-opportunity-intelligence-as-a-component-ecosystem)
    - [Learning and Practice as a Component Ecosystem](#learning-and-practice-as-a-component-ecosystem)
    - [Feasible Data Starting Points](#feasible-data-starting-points)
  - [B. Capability Systems](#b-capability-systems)
  - [C. Platform Programs](#c-platform-programs)
  - [D. Simulation and Scale Laboratories](#d-simulation-and-scale-laboratories)
  - [Ways to Deepen Any Program](#ways-to-deepen-any-program)

---

## Philosophy

Improve through two complementary modes:

- **Group 1 — Engineering Challenges:** Short projects (1 day to ~3 weeks) that focus on mastering a concept or technology.
- **Group 2 — Systems Projects:** Larger integrations (1 month to 6+ months) that combine multiple disciplines into production-like systems.

Difficulty should come not only from the algorithm itself, but also from engineering constraints such as unfamiliar languages, deployment environments, performance requirements, scale, interoperability, and reliability.

---

## Group 1: Engineering Challenges

> **Typical duration:** 1 day to ~3 weeks per challenge.

### A. Data Science / Machine Learning

Each practice row uses one dataset or one explicitly defined synthetic workload. Letter suffixes keep related dataset-specific variants under the same conceptual challenge.

| Track | Practice mode | Purpose |
|---|---|---|
| **A1** | Rebuild algorithms | Learn mechanics; compare with production libraries. |
| **A2** | Compare specialized tools | Learn capabilities, tradeoffs, and failure modes. |
| **A3** | Solve problem families | Choose baselines, validation, metrics, and deployment constraints. |
| **A4** | Implement across languages/runtimes | Prove model parity, portability, and performance outside notebooks. |

#### A1. Foundational Algorithms: Rebuild, Verify, Compare

Build the smallest correct version; use mature libraries as the benchmark.

| Challenge and scenario | Implement | Dataset-specific constraints and checks | Dataset |
|---|---|---|---|
| **A1.1a Interpretable house-value regression:** explain regional median values with linear effects | OLS via normal equation and QR/SVD; gradient descent; L1/L2 | Account for spatial correlation, feature scaling, skew, and the capped target; compare random and geographic holdouts; match scikit-learn/statsmodels | [California Housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) |
| **A1.1b Interpretable campaign-response classification:** estimate whether a client subscribes | Logistic loss; gradient descent; L1/L2; probability calibration | Encode categoricals; handle imbalance; exclude call duration when predicting before a call ends; respect campaign chronology; match scikit-learn/statsmodels | [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) |
| **A1.2a Explainable income classification:** build an inspectable applicant rule tree | CART classification splits; stopping; pruning; missing/categorical handling | Treat `?` values explicitly; test class imbalance, demographic slices, repeated values, and depth; hand-check early splits; match scikit-learn | [Adult](https://archive.ics.uci.edu/dataset/2/adult) |
| **A1.2b Explainable quality prediction:** predict an ordinal wine score with a regression tree | CART regression loss; stopping; pruning | Respect the concentrated integer target and rare extreme scores; compare regression with discretized classification; match scikit-learn predictions | [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) |
| **A1.3 Reduce unstable land-cover predictions:** classify forest cover with bagged trees | Bootstrap sampling; feature subsampling; OOB score; parallel trees; permutation importance | Handle multiclass imbalance and mixed continuous/binary indicators; compare OOB and held-out scores; test seeds and correlated soil features | [Covertype](https://archive.ics.uci.edu/dataset/31/covertype) |
| **A1.4 Fit weak physical signals stage by stage:** distinguish simulated particle events | Residual trees; learning rate; subsampling; early stopping; logistic loss | Stream or subsample the large numeric table; track stage loss, calibration, memory, and learning-rate/tree-count tradeoffs; compare boosting libraries | [HIGGS](https://archive.ics.uci.edu/dataset/280/higgs) |
| **A1.5a Classify wines by nearby chemical profiles:** implement exact low-dimensional k-NN | Brute-force k-NN; distance metrics; weighting; KD-tree or ball-tree | Standardize features with different units; test ties, leave-one-out behavior, distance weighting, and irrelevant features; match scikit-learn | [Wine](https://archive.ics.uci.edu/dataset/109/wine) |
| **A1.5b Retrieve visually similar clothing images:** compare exact and approximate neighbors | Brute-force distance search; batching; dimensionality reduction; HNSW/IVF comparison | Flatten consistently; separate train/query sets; measure recall@K, latency, and memory as dimension/index settings change | [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) |
| **A1.6a Classify discussion topics from sparse word counts:** rebuild Naive Bayes | Multinomial/Bernoulli Naive Bayes; smoothing; log likelihoods; TF-IDF comparison | Prevent header/signature leakage; handle zero counts, underflow, unknown terms, and similar topic groups; compare logistic regression | [20 Newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html) |
| **A1.6b Classify review sentiment with limited compute:** compare count-event assumptions | Multinomial/Bernoulli Naive Bayes; smoothing; n-grams; log-space scoring | Preserve the provided train/test split; control vocabulary and review-length effects; test negation, unknown terms, calibration, and class balance | [IMDb](https://ai.stanford.edu/~amaas/data/sentiment/) |
| **A1.7 Discover purchasing profiles without labels:** compare hard and probabilistic clusters | k-means++; Lloyd's algorithm; empty-cluster recovery; EM; soft assignment | Scale highly skewed spending columns; inspect outliers and channel/region context; test seed stability and covariance failure; match scikit-learn | [Wholesale Customers](https://archive.ics.uci.edu/dataset/292/wholesale+customers) |
| **A1.8 Learn digit boundaries from arrays only:** train a small neural classifier | Dense layers; activations; cross-entropy; backprop; SGD/Adam; dropout; checkpoints | Normalize pixels consistently; perform numerical gradient checks; overfit a tiny batch; inspect per-digit confusion; match PyTorch/JAX/TensorFlow | [MNIST](https://www.openml.org/d/554) |
| **A1.9 Separate controlled classes with maximum margin:** expose linear and kernel behavior | Linear hinge-loss solver; soft margin; kernels; simplified SMO | Generate overlapping, nonlinear, imbalanced, duplicated, and differently scaled points with known geometry; check KKT conditions and support vectors | Synthetic 2-D margin dataset with recorded generator and seed |
| **A1.10 Decode hidden activities from sensor windows:** infer a constrained state sequence | Forward/backward; Viterbi; Baum–Welch; log-space probabilities | Split by subject; preserve sequence order; define transitions between activities; test missing windows and underflow; compare with a mature HMM library | [UCI HAR](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones) |
| **A1.11 Rank unseen movies from sparse interactions:** learn latent preferences | Matrix factorization; factorization machines; SGD/ALS; implicit-feedback variant | Use temporal or leave-last-out evaluation; prevent seen-item recommendations; test negative sampling, regularization, cold users/items, and ranking metrics | [MovieLens](https://grouplens.org/datasets/movielens/) |

#### A2. Specialized Library Laboratories

Use identical splits, preprocessing, metrics, and compute budgets.

| Laboratory and scenario | Compare | Dataset-specific constraints and checks | Dataset |
|---|---|---|---|
| **A2.1a Choose a boosting library for mixed demographic data** | XGBoost, LightGBM, CatBoost | Hold preprocessing, splits, and compute fixed; compare native categorical handling, missing values, calibration, demographic slices, export parity, and latency | [Adult](https://archive.ics.uci.edu/dataset/2/adult) |
| **A2.1b Choose a boosting library for a large numeric classifier** | XGBoost, LightGBM, CatBoost | Stream or sample consistently; compare histogram settings, CPU/GPU memory, training time, early stopping, calibration, and inference throughput | [HIGGS](https://archive.ics.uci.edu/dataset/280/higgs) |
| **A2.2 Tune a multiclass model within one hour** | Random search, successive halving, Optuna/Ray Tune; AutoGluon, FLAML, or H2O | Use one search space and fixed budget; preserve the multiclass metric; test pruning, resumption, seeds, memory, and validation overfitting | [Covertype](https://archive.ics.uci.edu/dataset/31/covertype) |
| **A2.3 Select 500 card transactions for daily review** | Under/oversampling, SMOTE, balanced ensembles, class weights, focal loss | Split chronologically; resample only inside training folds; calibrate after sampling; compare precision@500, recall, and expected cost under prevalence shift | [Credit Card Fraud](https://www.openml.org/d/1597) |
| **A2.4a Choose a toolkit for many competition time series** | StatsForecast, Prophet, MLForecast/sktime, Darts/NeuralForecast | Use the provided frequencies/horizons; compare seasonal-naive baselines, rolling evaluation, missing values, global/local models, interval coverage, and runtime | [M4](https://github.com/Mcompetitions/M4-methods/tree/master/Dataset) |
| **A2.4b Forecast related electricity-consumption series** | StatsForecast, MLForecast/sktime, Darts/NeuralForecast | Preserve timestamps and meter identities; handle missing intervals, daily/weekly seasonality, aggregation, global models, and cold meters through rolling backtests | [Electricity Load](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014) |
| **A2.5a Choose an image-classification training and edge stack** | OpenCV, torchvision/KerasCV, timm, Albumentations | Hold split and augmentation policy fixed; compare transfer learning, mixed precision, export parity, calibration, memory, and edge latency | [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) |
| **A2.5b Choose an object-detection training and inference stack** | torchvision/KerasCV, Albumentations, YOLO, OpenCV deployment | Use one COCO-format subset; hold resizing and augmentations fixed; compare mAP, NMS behavior, small objects, export parity, memory, and latency | [COCO](https://cocodataset.org/) subset |
| **A2.5c Choose an image-segmentation stack for pet boundaries** | torchvision/KerasCV, segmentation-model libraries, Albumentations, OpenCV | Preserve masks during resizing/augmentation; compare IoU/Dice, boundary quality, mixed precision, export parity, and edge memory | [Oxford-IIIT Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/) |
| **A2.6 Choose an NLP stack for news-topic classification** | spaCy, Transformers, TF-IDF, sentence-embedding classifiers | Match text cleanup, split, truncation, batching, and metric; compare calibration, confusion among related topics, quantization, throughput, and memory | [AG News](https://huggingface.co/datasets/fancyzhx/ag_news) |
| **A2.7a Extract fields from visually structured forms** | Tesseract, PaddleOCR, EasyOCR, docTR, layout-aware models or cloud OCR | Hold rendering/preprocessing fixed; preserve word boxes; compare OCR, key-value extraction, reading order, confidence, and CPU/GPU throughput | [FUNSD](https://guillaumejaume.github.io/FUNSD/) |
| **A2.7b Recognize handwritten lines** | Tesseract, PaddleOCR, EasyOCR, docTR, handwriting recognizers | Split by writer where possible; normalize image height consistently; compare CER/WER, blank handling, language models, confidence, and throughput | [IAM Handwriting](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) |
| **A2.8a Select a vector engine for semantic passage retrieval** | FAISS, pgvector, Qdrant/Milvus, Elasticsearch/OpenSearch | Use identical embeddings and queries; compare exact/HNSW/IVF recall, latency, memory, persistence, deletes, and index rebuilds | [BEIR](https://github.com/beir-cellar/beir) corpus from one selected task |
| **A2.8b Select a vector engine for filtered, mutable retrieval** | FAISS, pgvector, Qdrant/Milvus, Elasticsearch/OpenSearch | Generate one versioned corpus with categorical/range filters; measure filtered recall, hot-filter skew, updates, deletes, compaction, replication, and migration | Synthetic filtered vector corpus with recorded generator and seed |
| **A2.9 Explain and monitor an income model under controlled shifts** | SHAP/permutation importance; Pandera/Great Expectations; Evidently/custom metrics | Create shifted copies from one source; test schema violations, missing-category changes, correlated explanations, demographic slices, reference windows, and alert false positives | [Adult](https://archive.ics.uci.edu/dataset/2/adult) plus versioned transformations |
| **A2.10 Process one regional street-network extract without spatial leakage** | GeoPandas/Shapely, PyProj, DuckDB Spatial/PostGIS; optional raster overlay | Preserve source CRS and identifiers; repair invalid geometry; compare spatial indexes/joins, projection distortion, boundary cases, and geographic holdouts | One regional [OpenStreetMap extract](https://download.geofabrik.de/) |
| **A2.11a Choose an environmental-sound classification stack** | FFmpeg/TorchCodec, librosa, torchaudio transforms, audio classifiers | Standardize sample rate/channels and fold usage; compare spectrogram/MFCC pipelines, augmentation, clip leakage, calibration, and CPU/GPU latency | [UrbanSound8K](https://urbansounddataset.weebly.com/urbansound8k.html) |
| **A2.11b Choose a keyword-spotting and streaming stack** | FFmpeg/TorchCodec, librosa/torchaudio, Transformers or small streaming models | Split by speaker; preserve unknown/silence classes; test noise augmentation, window stride, false activations, streaming state, and real-time latency | [Speech Commands](https://www.tensorflow.org/datasets/catalog/speech_commands) |
| **A2.11c Choose an automatic-speech-recognition stack** | FFmpeg/TorchCodec, torchaudio transforms, Transformers, SpeechBrain | Preserve speaker-disjoint splits and transcripts; compare resampling, decoding, WER, batching, long audio, CPU/GPU memory, and real-time factor | [LibriSpeech](https://www.openslr.org/12) |
| **A2.11d Choose a music-source-separation stack** | FFmpeg/TorchCodec, librosa/torchaudio, separation libraries | Respect official track splits; align channels/sample rates; compare SI-SDR, artifacts, chunk overlap, full-song memory, and real-time factor | [MUSDB18](https://sigsep.github.io/datasets/musdb.html) |
| **A2.12 Fit uncertain group effects in a small hierarchical model** | PyMC, Stan, NumPyro | Match centered/non-centered formulations, priors, and likelihood; compare MCMC/VI, ESS, divergences, shrinkage, and posterior predictive fit | Eight Schools |
| **A2.13 Learn from a changing event stream under bounded memory** | River vs incremental and periodically retrained scikit-learn models | Use progressive validation in source order; measure drift-detector alarms, recovery, update latency, memory, and performance across known regime changes | [Electricity](https://www.openml.org/d/151) |
| **A2.14 Classify new papers in a citation graph at scale** | PyTorch Geometric, DGL, and non-neural graph baselines | Use the official split; preserve graph direction/features; compare neighbor sampling, batching, inductive evaluation, memory, and full-batch parity on a subset | [OGBN-Arxiv](https://ogb.stanford.edu/docs/nodeprop/#ogbn-arxiv) |
| **A2.15a Add regression intervals to house-value predictions** | MAPIE, split conformal, quantile regression, ordinary residual intervals | Use a geographic or justified random split; compare marginal/regional coverage, interval width, capped targets, shift, and calibration-set size | [California Housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) |
| **A2.15b Add prediction sets and abstention to income classification** | MAPIE, calibrated probabilities, conformal sets, selective prediction | Handle imbalance and demographic slices; compare coverage, set size, calibration, abstention rate, and behavior on rare categories | [Adult](https://archive.ics.uci.edu/dataset/2/adult) |
| **A2.16 Process taxi trips larger than memory and survive skewed joins** | Polars, DuckDB, Dask, Spark, Ray | Apply identical cleaning and aggregations; preserve timestamp/location types; test partition skew, spill, lazy plans, worker failure, and result parity | [NYC Taxi](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) |
| **A2.17a Serve one image classifier through several runtimes** | Framework-native inference, ONNX Runtime, TensorRT, OpenVINO | Export one trained model; preserve image preprocessing; compare top-class/logit parity, quantization loss, batching, warm-up, p95/p99 latency, and memory | [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) with a ResNet-style model |
| **A2.17b Serve one text classifier through several runtimes** | Framework-native inference, ONNX Runtime, TensorRT, OpenVINO | Freeze tokenizer/version and truncation; compare logit parity, dynamic sequence lengths, quantization, batching, warm-up, throughput, and memory | [AG News](https://huggingface.co/datasets/fancyzhx/ag_news) with a small transformer |
| **A2.17c Serve one boosted-tree model through several runtimes** | Framework-native inference, ONNX Runtime, Treelite or equivalent compiled runtime | Freeze schema/category mapping; compare probabilities, missing values, malformed rows, startup, single-row/batch latency, throughput, and binary size | [Adult](https://archive.ics.uci.edu/dataset/2/adult) with a boosted-tree model |

#### A3. Applied Problem Families and Typical Solution Methods

Start with a cheap baseline. Match validation to future use; add complexity only when it improves the decision.

| Problem and scenario | Methods | Dataset-specific decision constraints and metrics | Dataset |
|---|---|---|---|
| **A3.1a Predict campaign subscription from mixed customer data** | Rules; logistic regression; trees; forests; boosting; calibrated ensembles | Exclude post-outcome call duration for pre-call use; encode categoricals; respect chronology; compare calibration, recall, and cost-based thresholds | [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) |
| **A3.1b Predict regional house values from census attributes** | Mean/linear baselines; trees; forests; boosting; calibrated ensembles | Use spatially aware validation; inspect capped targets, skew, geographic transfer, residual slices, confidence, and absolute error | [California Housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) |
| **A3.2 Select 500 transactions for daily fraud review** | Rules; class weights; sampling/SMOTE; balanced ensembles; focal loss; calibrated thresholds | Split chronologically; account for anonymized features and extreme imbalance; compare precision@500, recall, calibration, and expected loss | [Credit Card Fraud](https://www.openml.org/d/1597) |
| **A3.3 Forecast bicycle demand for staffing and capacity** | Seasonal naive; ETS; SARIMAX; Prophet; lagged boosting; global regression | Split by time; use weather/calendar values only when known at prediction time; evaluate peaks, holidays, count error, and interval coverage | [Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) |
| **A3.4 Alert on time-series anomalies without flooding operators** | Rules; robust z-scores; seasonal residuals; isolation methods; autoencoders; change-point detection | Follow each series' labels and cadence; group adjacent alerts; compare event precision/recall, delay, threshold stability, and alert volume | [Numenta Anomaly Benchmark](https://github.com/numenta/NAB) |
| **A3.5 Create actionable customer segments from annual spending** | RFM-style rules; k-means/k-medoids; GMM; hierarchical clustering; DBSCAN/HDBSCAN | Transform skewed monetary variables; inspect outliers and channel/region context; compare stability, minimum size, interpretability, and simple-rule baselines | [Wholesale Customers](https://archive.ics.uci.edu/dataset/292/wholesale+customers) |
| **A3.6 Rank unseen movies for each user** | Popularity/recency; k-NN; matrix factorization; implicit models; two-tower retrieval; hybrid ranking | Use temporal or leave-last-out splits; filter seen items; handle sparse/cold users; compare Recall/NDCG, diversity, coverage, and popularity bias | [MovieLens](https://grouplens.org/datasets/movielens/) |
| **A3.7 Return relevant passages within a latency budget** | BM25; boosts/filters; embedding retrieval; cross-encoder; pairwise/listwise ranking | Respect query/passage judgments; build hard negatives without test leakage; compare MRR/Recall@K, query slices, index size, and p95 latency | [MS MARCO](https://microsoft.github.io/msmarco/) passage ranking |
| **A3.8a Route news text to a topic with human review for uncertainty** | Rules; TF-IDF plus linear model; embeddings; transformer fine-tuning | Preserve the official split; inspect related-topic confusion, calibration, short texts, truncation, abstention, and review capacity | [AG News](https://huggingface.co/datasets/fancyzhx/ag_news) |
| **A3.8b Extract named entities with human review for uncertainty** | Rules; CRF baseline; transformer token classification; schema-bound LLM | Preserve token/span alignment; handle BIO transitions, ambiguous mentions, rare entity types, span F1, calibration, and review capacity | [CoNLL-2003](https://www.clips.uantwerpen.be/conll2003/ner/) |
| **A3.9a Classify images into object categories** | CNN/ViT classification; transfer learning; calibrated prediction | Use the fixed classes and split; test augmentation leakage, per-class confusion, calibration, corruption robustness, model size, and edge latency | [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) |
| **A3.9b Detect and localize objects in natural scenes** | YOLO; Faster R-CNN; DETR-style detection | Preserve COCO annotations/evaluation; handle small and crowded objects, resizing, NMS, mAP by size, and inference latency | [COCO](https://cocodataset.org/) subset |
| **A3.9c Segment pet foreground and boundaries** | U-Net; DeepLab; Mask R-CNN-style segmentation | Transform images and masks together; handle trimap/boundary labels, varied backgrounds, IoU/Dice, and boundary quality | [Oxford-IIIT Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/) |
| **A3.9d Verify whether two face images show the same identity** | Face alignment; embedding/metric learning; calibrated similarity score | Follow the pair protocol; control identity leakage; compare ROC, EER, TAR at low FAR, image-quality slices, and threshold stability | [LFW](http://vis-www.cs.umass.edu/lfw/) |
| **A3.10a Convert noisy forms into validated key-value fields** | Cleanup/deskew; OCR; layout modeling; key-value extraction; validation rules | Preserve word boxes and entity links; evaluate OCR separately from fields; test reading order, rotation, confidence, and review routing | [FUNSD](https://guillaumejaume.github.io/FUNSD/) |
| **A3.10b Convert handwriting into reviewable text** | Line detection; normalization; handwriting recognition; language-model decoding | Split by writer; compare CER/WER, blank/space handling, confidence, long lines, and review thresholds | [IAM Handwriting](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) |
| **A3.11 Compare lexical, dense, and hybrid retrieval on one judged corpus** | BM25; bi-encoder; hybrid retrieval; expansion; reranking; ANN | Select one benchmark task and keep its corpus/queries/qrels fixed; compare Recall/MRR/NDCG, hard negatives, index freshness, and latency/recall | One [BEIR](https://github.com/beir-cellar/beir) task |
| **A3.12 Answer multi-hop questions with citations and abstention** | Chunk/retrieve baseline; query rewrite; hybrid search; reranking; parent-child retrieval; routing | Preserve supporting-fact annotations; evaluate retrieval, answer, and citation support separately; add unanswerable variants; measure cost and latency | [HotpotQA](https://hotpotqa.github.io/) |
| **A3.13a Automate bounded real-world tool tasks only when it beats fixed orchestration** | Deterministic workflow; single-agent tools; planner/executor; verification; multi-agent variant | Use the published task split and permitted tools; measure task/partial success, retries, trace quality, safety, reproducibility, cost, and recovery | [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) |
| **A3.13b Repair repository issues with verifiable tests** | Fixed workflow; retrieval plus patching; planning; test-driven verification | Isolate repositories; prevent test-set leakage; compare resolution rate, invalid patches, test time, retries, tool cost, and reproducibility | [SWE-bench](https://www.swebench.com/) |
| **A3.14 Estimate the effect of job training on earnings** | Experiment baseline; adjustment; matching/weighting; causal forests; S/T/X/R learners | State the estimand; inspect overlap and balance; avoid post-treatment variables; compare uncertainty, sensitivity, and placebo checks | [LaLonde/NSW](https://users.nber.org/~rdehejia/data/nswdata2.html) |
| **A3.15 Estimate censored survival from clinical covariates** | Kaplan–Meier; log-rank; Cox; AFT; survival forests; competing-risk extensions | Respect censoring and follow-up time; test proportional hazards; avoid future leakage; compare concordance, horizon calibration, and subgroup behavior | [METABRIC](https://www.cbioportal.org/study/summary?id=brca_metabric) |
| **A3.16a Classify environmental sounds** | Spectral baseline; CNN/transformer audio classifier | Use predefined folds; avoid overlapping-source leakage; compare macro F1, calibration, noise robustness, clip duration, and real-time factor | [UrbanSound8K](https://urbansounddataset.weebly.com/urbansound8k.html) |
| **A3.16b Detect spoken keywords continuously** | MFCC/CNN baseline; temporal convolution; transformer; streaming decoder | Split by speaker; preserve unknown/silence categories; test false activations, noise/device shift, streaming delay, and real-time factor | [Speech Commands](https://www.tensorflow.org/datasets/catalog/speech_commands) |
| **A3.16c Detect overlapping sound events** | Frame/clip classifier; weakly supervised detection; transformer | Respect clip-level labels and ontology; handle imbalance and overlapping events; compare macro mAP, event metrics, and threshold calibration | [AudioSet](https://research.google.com/audioset/) subset |
| **A3.16d Transcribe read speech** | CTC baseline; encoder-decoder or pretrained ASR; language-model decoding | Preserve speaker-disjoint splits; normalize transcripts consistently; compare WER by speaker/length, long-audio memory, noise robustness, and real-time factor | [LibriSpeech](https://www.openslr.org/12) |
| **A3.16e Separate music sources** | Spectral masking; waveform or spectrogram networks | Respect official song splits; align channels/sample rates; compare SI-SDR, vocal/accompaniment artifacts, chunk boundaries, memory, and real-time factor | [MUSDB18](https://sigsep.github.io/datasets/musdb.html) |
| **A3.16f Verify speakers across recording sessions** | Speaker embeddings; metric learning; score normalization | Use identity/session-disjoint trials; prevent clip overlap; compare EER, minDCF, noise/language robustness, enrollment duration, and latency | [VoxCeleb](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/) |
| **A3.17a Detect faces before downstream biometric processing** | Classical cascade baseline; single-shot and multi-scale detectors | Preserve detection annotations; evaluate hard/small/occluded faces, precision-recall, missed-face propagation, and edge latency | [WIDER FACE](http://shuoyang1213.me/WIDERFACE/) |
| **A3.17b Estimate facial landmarks for alignment** | Shape-regression baseline; heatmap or coordinate network | Respect face-level splits; handle pose, occlusion, annotation conventions, normalized landmark error, and downstream alignment effects | [300-W](https://ibug.doc.ic.ac.uk/resources/300-W/) |
| **A3.17c Estimate apparent age with uncertainty** | Ordinal regression; classification-to-expectation; direct regression | Split by identity where metadata allows; handle noisy labels and age imbalance; compare MAE, calibration, age slices, and consent/licensing constraints | [UTKFace](https://susanqq.github.io/UTKFace/) |
| **A3.17d Detect presentation attacks before verification** | Texture/motion baselines; CNN/transformer PAD; challenge-response variant | Split by identity and attack medium; compare APCER/BPCER, unseen attacks, camera shift, threshold stability, and latency | [CelebA-Spoof](https://github.com/Davidzhangyuanhan/CelebA-Spoof) |
| **A3.17e Perform consent-based 1:1 face verification** | Aligned face embeddings; metric learning; calibrated similarity threshold | Follow pair protocols; prevent identity leakage; compare FAR/FRR/EER and TAR at low FAR across image-quality slices | [LFW](http://vis-www.cs.umass.edu/lfw/) |
| **A3.17f Perform a bounded 1:N identification experiment** | Gallery/probe embeddings; nearest-neighbor search; open-set thresholding | Build identity-disjoint development/test protocols; report rank-K and false identification; vary gallery size; document consent, retention, and non-deployment scope | [LFW](http://vis-www.cs.umass.edu/lfw/) |
| **A3.17g Audit face-model performance across demographic groups** | Fixed detector, embedding, or age model; slice metrics; threshold analysis | Do not infer unsupported attributes; follow labels/licence; compare error and calibration slices, sample-size uncertainty, and threshold tradeoffs | [FairFace](https://github.com/joojs/fairface) |
| **A3.18a Return house-value intervals instead of point estimates alone** | Quantile regression; residual/bootstrap intervals; conformal intervals | Use geographic holdouts; report marginal/regional coverage, interval width, capped-target effects, calibration size, and shift behavior | [California Housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) |
| **A3.18b Return income-classification sets or abstain** | Calibrated probabilities; conformal sets; selective prediction | Handle imbalance and rare categories; compare coverage, set size, calibration by demographic slice, abstention rate, and abstention cost | [Adult](https://archive.ics.uci.edu/dataset/2/adult) |
| **A3.19 Update predictions continuously as electricity behavior changes** | Incremental linear/tree models; sliding windows; ensembles; drift detectors; retraining policies | Preserve event order; use prequential metrics; inspect recurring regimes, delayed labels, false alarms, memory, update latency, and recovery | [Electricity](https://www.openml.org/d/151) |
| **A3.20a Classify new papers in a growing citation network** | Graph heuristics; embeddings; GCN/GAT/GraphSAGE | Use the official split and graph direction; control neighborhood leakage; compare sampling bias, inductive nodes, memory, and graph shift over publication time | [OGBN-Arxiv](https://ogb.stanford.edu/docs/nodeprop/#ogbn-arxiv) |
| **A3.20b Predict future collaboration links** | Common-neighbor baselines; graph embeddings; GNN link prediction | Use temporal edge splits; generate negatives without leakage; compare Hits@K, neighborhood sampling, cold nodes, and evolving graph structure | [OGBL-Collab](https://ogb.stanford.edu/docs/linkprop/#ogbl-collab) |
| **A3.21a Learn text topics while minimizing annotation** | Uncertainty/diversity sampling; pseudo-labeling; labeling functions; label model | Start from a small labeled pool; track performance per label; inspect selection bias, annotator disagreement, rare topics, and confirmation bias | [20 Newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html) |
| **A3.21b Improve image classification from few labels** | Uncertainty/diversity sampling; consistency training; pseudo-labeling; semi-supervised baselines | Fix labeled/unlabeled splits; compare accuracy per label, class coverage, augmentation sensitivity, confirmation bias, and calibration | [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) |
| **A3.22 Assign taxonomy-consistent legal topics to documents** | Binary relevance; classifier chains; label embeddings; hierarchy-aware loss; constrained decoding | Preserve multilabel targets and hierarchy; compare micro/macro/sample F1, precision@K, rare labels, hierarchy violations, and calibration | EUR-Lex multilabel benchmark corpus |
| **A3.23 Evaluate offer policies from logged bandit feedback** | Random policy; epsilon-greedy; UCB; Thompson sampling; contextual bandits | Respect logged propensities and context; compare off-policy estimators, support mismatch, delayed rewards, estimator variance, and policy safety | [Open Bandit Dataset](https://research.zozo.com/data.html) |
| **A3.24a Retrieve images from text and text from images** | Dual encoders; contrastive learning; late/early fusion; cross-attention reranking | Use image-caption groups; prevent duplicate-image leakage; compare bidirectional Recall@K, hard negatives, missing text, and compute cost | [Flickr30k](https://shannon.cs.illinois.edu/DenotationGraph/) |
| **A3.24b Retrieve audio from textual descriptions** | Audio/text encoders; contrastive learning; cross-attention reranking | Split by audio clip/source; inspect multiple valid captions, acoustic overlap, bidirectional Recall@K, noisy/missing text, and inference cost | [AudioCaps](https://audiocaps.github.io/) |
| **A3.25a Predict demand hotspots across a city** | Spatial/temporal baselines; grid aggregation; hotspot detection; spatial regression | Preserve timestamps and zone geometry; use spatial/temporal holdouts; inspect autocorrelation, boundary effects, peak demand, and map uncertainty | [NYC Taxi](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) |
| **A3.25b Detect mapped objects from satellite imagery** | Raster tiling; CNN/transformer detection or segmentation; spatial postprocessing | Split geographically; align imagery/labels; handle resolution, boundary objects, imbalance, geographic transfer, IoU/mAP, and map uncertainty | [SpaceNet](https://spacenet.ai/datasets/) selected challenge |
| **A3.26 Train a handwriting model across simulated clients without centralizing data** | Federated averaging; secure-aggregation simulation; differential privacy; local/on-device learning | Preserve writer-based client partitions; handle non-IID labels, client imbalance/dropout, privacy budget, membership inference, communication, and stragglers | [FEMNIST/LEAF](https://leaf.cmu.edu/) |
| **A3.27a Evaluate synthetic tabular data for downstream income modeling** | Parametric simulation; resampling; GAN/VAE/diffusion or tabular synthesizers; constraint-based generation | Compare fidelity and downstream utility by slice; test impossible combinations, memorization, membership leakage, rare categories, and bias amplification | [Adult](https://archive.ics.uci.edu/dataset/2/adult) |
| **A3.27b Evaluate synthetic rare-event data for fraud modeling** | Conditional sampling; class-aware tabular synthesizers; privacy-preserving generation | Preserve a real-only test set; compare rare-case coverage, ranking utility, calibration, memorization/privacy leakage, and shifted prevalence | [Credit Card Fraud](https://www.openml.org/d/1597) |

#### A4. Language and Runtime Implementations

| Runtime scenario | Implement | Dataset-specific parity and performance constraints | Dataset or workload |
|---|---|---|---|
| **A4.1 Train a digit model in Python and run it in native services and a browser** | Export ONNX; run with Python, C++, C#, Java, and JavaScript | Freeze pixel normalization, layout, labels, and golden images; define logit tolerance; test unsupported operators, malformed tensors, warm-up, p95 latency, and memory | [MNIST](https://www.openml.org/d/554) |
| **A4.2 Run income-model inference in Rust without a Python runtime** | Load and score a linear or tree model with typed schema, zero-copy data where useful, and optional SIMD | Freeze categorical/null mapping; match probabilities and thresholds; reject malformed rows/models; test concurrency, allocation, startup, throughput, and binary size | [Adult](https://archive.ics.uci.edu/dataset/2/adult) |
| **A4.3 Score a live fraud stream with bounded Go workers** | Event ingestion, online features, batching, scorer, bounded goroutine pipeline | Generate labeled events with IDs and event time; preserve documented ordering; handle duplicates, backpressure, cancellation, worker failure, graceful shutdown, and p99 latency | Synthetic fraud stream with recorded schema, generator, and seed |
| **A4.4 Reproduce Python demand features and scores entirely in SQL** | Point-in-time feature queries and linear/tree scoring in DuckDB or PostgreSQL | Preserve timestamp semantics; match lag/rolling rows and predictions; handle nulls, duplicates, late observations, query plans, and memory | [Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) |
| **A4.5 Process taxi trips too large for one machine process on the JVM** | Feature preparation and training with Java/Scala and Spark | Match a local reference sample; preserve timestamp/location types; test partitioning, skew, serialization, retries, reproducibility, executor memory, and scaling efficiency | [NYC Taxi](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) |
| **A4.6 Run a digit model privately and offline in a browser** | TypeScript plus ONNX Runtime Web using WASM/WebGPU; local preprocessing and model caching | Freeze image resizing/normalization; match server logits/classes; test offline reload, malformed input, browser support, startup, inference latency, and memory | [MNIST](https://www.openml.org/d/554) |
| **A4.7 Accelerate dense matrix multiplication on a CPU** | Naive, transposed, blocked, threaded, and optional SIMD C/C++ implementations | Match a high-precision reference; test square/tall/skinny shapes, alignment, cache boundaries, thread scaling, numeric stability, and regressions | Generated matrix-pair workload with recorded shapes and seed |
| **A4.8 Accelerate dense matrix multiplication on a GPU** | CUDA or Triton kernel with tiling, shared memory, and mixed precision where justified | Match CPU/reference tolerance; test memory access, occupancy, warm-up, shape sensitivity, transfer cost, non-multiple tile sizes, and edge cases | The same generated matrix-pair workload used by A4.7 |
| **A4.9 Load one versioned income-model package in three languages** | Define a neutral schema for model, preprocessing, labels, metadata, and checksums; implement independent readers | Package linear/tree variants trained on the same data; test compatibility, unknown fields, corruption, missing metadata, golden predictions, and deterministic serialization | [Adult](https://archive.ics.uci.edu/dataset/2/adult) |
| **A4.10 Reproduce a campaign-response model and service in R and Python** | Fit with tidymodels/mlr3; package in R; expose through Plumber; implement a Python reference | Freeze split and categorical mapping; exclude duration for pre-call use; match coefficients/probabilities within tolerance; test restoration, invalid requests, startup, and latency | [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) |

---

### B. Programming

Each row below is a complete problem. B1 pairs one primary data structure or algorithm with one workload; B2 pairs one cohesive component with one explicit contract. Later tracks may combine several mechanisms when the integration itself is the problem.

| Track | Problem type | Purpose |
|---|---|---|
| **B1** | Fundamental CS through concrete problems | Apply data structures and algorithms inside executable, measurable programs. |
| **B2** | Core components from scratch | Understand parsers, protocols, scheduling, storage, and runtime mechanics. |
| **B3** | Language and framework laboratories | Implement the same bounded behavior in different ecosystems. |
| **B4** | Application problem families | Build common user-facing and business workflows. |
| **B5** | Architecture and distributed systems | Handle state, communication, coordination, and partial failure. |
| **B6** | Security and trust boundaries | Build against an explicit threat model. |
| **B7** | Maintenance, quality, and performance | Improve existing systems safely and measurably. |

#### B1. Fundamental CS Through Concrete Problems

| Challenge and scenario | Implement | Workload-specific constraints and checks | Input or workload |
|---|---|---|---|
| **B1.1a Store sessions with chained hashing** | Hash table with separate chaining; insert, lookup, update, delete, and resize | Force collisions and duplicate keys; test long chains, adversarial hashes, load-factor changes, failed allocation, map parity, and expected operation cost | Generated one-million-session trace with fixed key distribution, operation mix, and seed |
| **B1.1b Store sessions with open-addressed hashing** | Hash table with linear, quadratic, or double-hash probing; tombstones and resize | Test full probe cycles, tombstone reuse, clustered hashes, high load, deletion correctness, map parity, and probe counts | The same generated session trace used by B1.1a |
| **B1.2a Store an append-heavy event sequence** | Dynamic array with indexed access, append, insert/delete, growth, and optional shrinking | Check size/capacity invariants; test zero capacity, boundary indexes, repeated growth/shrink cycles, failed allocation, and standard-vector parity | Generated append/read/edit trace with fixed burst pattern and seed |
| **B1.2b Keep only the latest 100,000 events** | Fixed-capacity circular deque with front/back operations and defined overwrite behavior | Test wraparound, empty/full transitions, capacity one, long-running indices, overwrite order, and standard-deque parity | Generated event-buffer trace with fixed capacity, bursts, and reads |
| **B1.3a Evaluate nested arithmetic expressions** | Operand/operator stacks with tokenization, precedence, associativity, and parentheses | Reject invalid tokens and mismatched delimiters; bound nesting; test unary operators and precedence; compare with a reference evaluator | Versioned valid/invalid expression corpus plus generated expressions |
| **B1.3b Maintain undo and redo history** | Two-stack command history with execute, undo, redo, and bounded retention | Failed commands must not alter history; new commands clear redo; test empty operations, retention eviction, and state reconstruction | Deterministic editor-command trace with expected state after every operation |
| **B1.4 Schedule delayed jobs by deadline** | Binary min-heap with insert, peek, remove, cancellation, and deadline update | Preserve heap invariants; handle equal/past deadlines, cancelled roots, repeated updates, empty queues, and fake-clock advancement | Generated one-million-job trace with fixed deadline distribution and seed |
| **B1.5a Evict least-recently-used product entries** | LRU cache using a hash table and doubly linked list; optional TTL | Require average constant-time access; test update recency, expiry, oversized values, capacity zero/one, and list/map invariants | Versioned Zipf-like product-request trace with sizes and timestamps |
| **B1.5b Evict least-frequently-used product entries** | LFU cache using a hash table and frequency buckets; deterministic tie-breaking | Test frequency updates, recency ties, expiry, counter growth, capacity zero/one, and bucket/map invariants | The same versioned product-request trace used by B1.5a |
| **B1.6a Suggest products from typed prefixes** | Trie with insertion, deletion, prefix lookup, and bounded ranked suggestions | Normalize Unicode consistently; handle duplicates, empty prefixes, deleted terms, deep keys, ranking updates, and sorted-list parity | One versioned product-name and popularity corpus |
| **B1.6b Match the most specific route pattern** | Prefix/radix trie with static, parameter, and wildcard segments | Define route precedence; handle ambiguous patterns, deletion, trailing separators, deep routes, and linear-scan parity | One versioned route-pattern and request-path corpus |
| **B1.7 Filter previously visited URLs probabilistically** | Bloom filter with configurable capacity/error rate, double hashing, and serialization | Verify no false negatives for inserted keys; measure predicted/observed false positives; test overcapacity, duplicates, corruption, and parameter mismatch | Generated URL stream with known inserted and unseen partitions |
| **B1.8 Sort a 20 GB log with 512 MB of memory** | External merge sort with sorted runs, bounded buffers, temporary files, and k-way merge | Preserve every valid record and duplicate; separate malformed timestamps; verify ordering, memory bound, interruption cleanup, and fan-in behavior | One generated 20 GB log with recorded schema, distribution, and seed |
| **B1.9a Find exact Top-K terms with a heap** | Full frequency map plus bounded min-heap | Define tie order; test empty, uniform, Zipfian, and adversarial streams; compare with full sorting; measure memory and runtime across K | One generated token stream with recorded frequency distribution and seed |
| **B1.9b Find exact Top-K terms with selection** | Full frequency map plus quickselect on term-count pairs | Handle duplicate counts and worst-case pivots; verify the Top-K boundary against sorting; compare runtime and mutation cost | The same generated token stream used by B1.9a |
| **B1.9c Estimate heavy hitters with bounded memory** | Misra–Gries, Space-Saving, or Count-Min-based heavy-hitter method | State error guarantees; test distribution shift and adversarial order; compare estimated/exact counts, recall@K, and fixed memory | The same generated token stream used by B1.9a |
| **B1.10a Detect reservation conflicts by ordered scanning** | Sort/merge intervals and scan for overlaps | Define touching and zero-duration behavior; normalize timezones; test containment, duplicates, cancellations, and brute-force parity | Generated reservation interval corpus with expected conflicts |
| **B1.10b Query changing reservations with an interval tree** | Interval tree with insert, delete, and overlap query | Preserve ordering/max-end invariants; test boundaries, containment, repeated endpoints, deletions, and scan parity | Versioned reservation update/query trace derived from B1.10a |
| **B1.11a Find one signature with KMP** | Prefix-function construction and streaming KMP matching | Define empty-pattern behavior; test overlaps, long repeated prefixes, byte/chunk boundaries, and naive-search parity | One versioned byte-log and single-signature corpus |
| **B1.11b Find thousands of signatures with Aho–Corasick** | Trie, failure links, output sets, and streaming multi-pattern matching | Handle shared prefixes, duplicate signatures, overlaps, empty patterns, byte/chunk boundaries, and naive multi-search parity | One versioned byte-log and signature-set corpus |
| **B1.12 Provide typo-tolerant term matching** | Levenshtein distance with full and memory-reduced dynamic programming; optional edit reconstruction | Handle empty and Unicode strings, bounded distance, long inputs, early exit, and reference-library parity | One versioned query/candidate pair corpus with expected distances |
| **B1.13 Resolve build dependencies** | Deterministic topological sort with explicit cycle-path reporting | Handle disconnected graphs, duplicate/self edges, missing nodes, multiple valid orders, and cycle certificates; verify every edge order | Generated dependency-graph corpus containing DAGs and cycles |
| **B1.14a Find shortest courier routes with Dijkstra** | Binary-heap Dijkstra with predecessor/path reconstruction | Require nonnegative weights; handle unreachable nodes, equal routes, zero-weight edges, stale heap entries, overflow, and reference parity | One versioned sparse weighted road-style graph and query set |
| **B1.14b Reduce route exploration with A\*** | A* with an admissible geographic or grid heuristic and path reconstruction | Match Dijkstra's optimal cost; test inconsistent/zero heuristics, blocked goals, equal routes, and expanded-node count | One generated blocked-grid corpus with fixed start/goal pairs |
| **B1.15 Group linked accounts incrementally** | Disjoint-set union with path compression and union by rank/size | Handle repeated/self links, new entities, large components, deterministic representatives where promised, and traversal parity | Generated account-link event trace with expected components |
| **B1.16a Assign one worker to one job** | Maximum bipartite matching with augmenting paths | Enforce compatibility edges; handle impossible assignments, ties, duplicates, and empty partitions; compare with exhaustive small cases | Generated worker/job compatibility graph corpus |
| **B1.16b Allocate capacitated workers through max flow** | Residual graph and augmenting-path max-flow algorithm | Preserve capacity/flow conservation; handle zero capacity and disconnected networks; verify max-flow/min-cut equality | Generated capacitated assignment-network corpus |
| **B1.17 Search a local document collection** | Inverted index with tokenization, postings, Boolean intersection, BM25 scoring, updates, and deletes | Define Unicode/token rules; test repeated terms, empty/hostile queries, persistence, ranking judgments, index size, and query latency | One versioned document corpus with judged queries |
| **B1.18a Index ordered records with a B+ tree** | Page-oriented B+ tree with lookup, insert, split, range scan, and optional delete/merge | Preserve occupancy/order/leaf-link invariants; test duplicate keys, partial pages, checksums, interrupted writes, and SQLite parity | Generated ordered key/value operation trace with crash points |
| **B1.18b Index write-heavy records with an LSM tree** | Memtable, immutable sorted runs, tombstones, lookup, range scan, flush, and compaction | Test overlapping runs, deletes, partial flush/compaction, checksums, bounded memory, and read/write amplification | The same generated key/value trace used by B1.18a |
| **B1.19 Redistribute cache keys as servers change** | Consistent-hash ring with virtual nodes, weighted members, replication, and membership updates | Test joins/leaves/failures, collisions, uneven weights, empty rings, replica overlap, hot keys, balance, and key movement | Generated key and membership-change trace with fixed hash seed |
| **B1.20a Query nearby map points with a quadtree** | Quadtree insertion, deletion, range search, and nearest-neighbor search | Define boundary ownership; test duplicate coordinates, clustered/uniform points, node overflow, empty regions, and brute-force parity | Generated 2-D point and query corpus with fixed spatial distributions |
| **B1.20b Query nearby rectangles with an R-tree** | Simplified R-tree insertion, node split, deletion, range search, and nearest-neighbor search | Preserve bounding boxes; test overlap, degenerate rectangles, split quality, empty regions, and brute-force parity | Generated rectangle and query corpus with fixed spatial distributions |
| **B1.21a Compress log bytes with Huffman coding** | Frequency table, tree, canonical codes, bit packing, versioned header, and decoder | Verify prefix freedom and exact round trips; handle empty/single-symbol input, corruption, truncation, and incompressible data | One versioned byte-log corpus with compressible and random partitions |
| **B1.21b Compress repetitive logs with an LZ-style dictionary** | Sliding-window matching, token encoding, bit packing, versioned header, and decoder | Verify exact round trips; test window boundaries, overlapping matches, invalid back-references, truncation, and incompressible data | The same versioned byte-log corpus used by B1.21a |

##### Connected challenge sequences

These are optional progressions; every referenced problem remains independently specified above.

1. **Log and search system:** B1.1a or B1.1b hashing → B1.8 external sorting → B1.7 Bloom filter → B1.11a or B1.11b matching → B1.17 inverted index → B1.21a or B1.21b compression.
2. **Job and resource scheduler:** B1.2b deque → B1.4 heap → B1.13 dependency graph → B1.10a or B1.10b interval conflicts → B1.16a or B1.16b assignment → B1.18a or B1.18b persistent index.
3. **Distributed cache:** B1.5a or B1.5b local cache → B5.2 service caching → B1.19 consistent hashing → B5.6 distributed rate limiting → B5.11 tenant isolation.

#### B2. Core Components From Scratch

| Component and scenario | Implemented contract | Component-specific constraints and checks | Reference inputs or workload |
|---|---|---|---|
| **B2.1a Parse a small configuration language** | Lexer and parser that produce a typed syntax tree from one published grammar | Report line/column errors; reject malformed nesting; define comments, escapes, precedence, and duplicate fields; cap depth; fuzz without hangs; compare with a parser library | One versioned grammar plus valid, invalid, deeply nested, and generated documents |
| **B2.1b Execute a small expression language** | Variables, values, arithmetic, conditions, functions, environments, and runtime errors over a defined syntax tree | Define evaluation order, scope, numeric behavior, recursion/resource limits, and error propagation; compare expected values and failures with a reference evaluator | One versioned program corpus with expected results, state changes, and runtime failures |
| **B2.2 Exchange versioned binary records** | Tagged schema, encoder, decoder, optional fields, collections, unknown-field behavior, and checksums | Bound lengths/nesting; reject truncation, corruption, invalid types, and oversized input; verify round trips, deterministic encoding, and backward/forward compatibility with an independent reader | One schema-evolution sequence and generated message corpus |
| **B2.3 Serve a bounded HTTP/1.1 subset** | Request parsing, routing, headers, query/body access, middleware, response writing, keep-alive, timeouts, and graceful shutdown | Publish the supported subset; limit headers/body/connections; handle partial reads, malformed requests, disconnects, slow clients, and exhaustion; compare with a standard server | One versioned HTTP conformance corpus plus slow, malformed, and load client traces |
| **B2.4 Execute tasks through a bounded thread pool** | Submission, bounded queue, workers, futures/results, cancellation, priorities if retained, and orderly shutdown | Prevent lost tasks and unbounded growth; handle exceptions, saturation, worker failure, cancellation races, nested submission, and shutdown states; verify with controlled scheduling and stress | One deterministic task trace plus seeded concurrency and saturation variants |
| **B2.5 Run persistent delayed and recurring jobs** | Durable job state, monotonic deadlines, recurrence, retries, cancellation, missed-run policy, and dispatch | Recover after injected crash points; define delivery guarantees; handle clock changes, equal deadlines, overruns, long jobs, and cancellation races; compare state with a reference model | One fake-clock job history containing bursts, retries, cancellations, overruns, and restarts |
| **B2.6 Store key/value records in one local file** | Put, get, delete, recovery, checksums, atomic batches, indexing, and compaction using one documented storage design | Handle partial writes, corruption, tombstones, large values, concurrent readers, restart, and interrupted compaction; verify against a model and compare selected behavior with SQLite | One generated operation history with recorded seed and injected crash/corruption points |
| **B2.7 Resolve object dependencies and lifecycles** | Constructor/value registration, dependency resolution, singleton/request/transient scopes, ownership, and cleanup | Detect missing/duplicate bindings and cycles; define constructor failure, scope ownership, thread safety, disposal order, and invalid cross-scope use; compare with a mature container | One generated dependency-graph corpus containing valid, missing, cyclic, failing, and scoped cases |
| **B2.8 Render an escaped template language** | Variables, conditions, loops, includes, filters, reusable templates, and context-aware escaping | Reject malformed syntax; define missing values; prevent unsafe evaluation, path traversal, include cycles, and unbounded output; fuzz and compare supported behavior with an established engine | One versioned template/context corpus with expected output, errors, and injection cases |

#### B3. Language and Framework Laboratories

| Laboratory and scenario | Compare | Workload-specific constraints and checks | Reference application or workload |
|---|---|---|---|
| **B3.1 Implement one inventory API across server frameworks** | FastAPI, ASP.NET Core, Go, and Node.js implementations of the same contract | Preserve products, stock, atomic reservations, pagination, and migrations; reject invalid quantities; test duplicate requests, concurrent reservations, stale updates, database restart, contract parity, tail latency, memory, and deployment size | One seeded catalog/database plus a versioned API contract and request trace |
| **B3.2 Implement one streaming converter across CLI ecosystems** | Python, Rust, and Go CLIs with the same subcommands, pipes, progress, and exit codes | Stream files larger than memory; handle malformed rows, broken pipes, encoding errors, cancellation, and interrupted output; compare golden results, startup, throughput, memory, and binary size | One versioned CSV/JSON corpus containing valid, malformed, mixed-encoding, and large inputs |
| **B3.3 Implement one order repository through several data-access approaches** | SQLAlchemy, Django ORM, Entity Framework, and raw SQL | Preserve one transaction contract; test rollback, concurrent updates, N+1 behavior, nulls, migration failure, and connection loss; inspect generated SQL and compare correctness/latency | One relational order schema plus a seeded transaction and query trace |
| **B3.4a Process many concurrent media downloads** | Threads, async runtimes, goroutines, and bounded worker implementations | Bound connections and memory; handle cancellation, timeouts, slow peers, backpressure, partial files, and retries; verify byte parity and compare throughput/tail latency | One replayable HTTP service and versioned download trace |
| **B3.4b Transform media using all CPU cores** | Threads, processes, goroutines/native extensions, and distributed workers | Preserve output parity; bound memory; account for serialization, startup, oversubscription, cancellation, worker failure, and task duplication | One versioned image-transformation corpus and operation trace |
| **B3.5 Compare testing approaches on one faulty library** | Example-based, property-based, mutation, and fuzz testing | Cover malformed input, numeric boundaries, invariants, timeouts, and nondeterminism; keep budgets fixed; compare seeded defect detection, mutation survival, runtime, and maintenance cost | One validation/calculation library with an input corpus and seeded defect set |
| **B3.6 Publish one library across package ecosystems** | Python package, Rust crate, npm package, and NuGet package with equivalent public behavior | Preserve API semantics; test dependency/version conflicts, unsupported runtimes, reproducible builds, deprecation, and one deliberate breaking change across real consumers | One versioned validation-library contract plus small consumer projects in each ecosystem |
| **B3.7 Expose one order-query capability through several protocols** | REST/JSON, gRPC/Protobuf, and GraphQL | Preserve query semantics; handle schema evolution, invalid requests, pagination, partial fields, deadlines, large responses, cancellation, and compatibility; compare payload and latency | One seeded order database, versioned query schema, and request corpus |
| **B3.8 Build one accessible issue tracker through several web approaches** | Server rendering, SPA, and progressive enhancement | Preserve behavior across loading/error/empty states, validation, refresh, slow networks, keyboard use, and disabled JavaScript where promised; compare accessibility, bundle size, startup, and runtime | One seeded issue/project fixture plus browser and accessibility interaction traces |

#### B4. Application Problem Families

| Problem and scenario | Required behavior | Scenario-specific constraints and checks | Actors, data, or workload |
|---|---|---|---|
| **B4.1 Manage a complete user-account lifecycle** | Registration, verified contact, login, logout, password reset, session listing/revocation, token rotation, and audit history | Prevent enumeration, session fixation, replay, brute force, token leakage, and unsafe password storage; verify every lifecycle transition and global session revocation | One multi-user account-event trace containing successful, failed, expired, replayed, and revoked operations |
| **B4.2 Authorize resources across users, roles, and tenants** | Ownership plus RBAC or ABAC enforced at every server-side entry point | Deny IDOR, privilege escalation, cross-tenant access, stale permissions, and client-only checks; verify an explicit allow/deny policy matrix and audit events | One tenant/resource/role fixture and adversarial access-request matrix |
| **B4.3 Process document-conversion jobs asynchronously** | Submit, report progress, retry, cancel, schedule, and inspect dead letters | Document delivery semantics; handle duplicates, poison input, worker crash, queue saturation, cancellation races, and idempotency; verify recovery and bounded backlog | One generated document-job stream with seeded failures, duplicates, delays, and cancellations |
| **B4.4 Consume payment webhooks reliably** | Verify signatures, persist events, process idempotently, replay failures, and reconcile remote/local state | Handle duplicates, gaps, reordering, delay, secret rotation, invalid signatures, and crash points; verify final state against a provider-side model | One versioned sandbox payment-event stream with expected account/order states |
| **B4.5 Synchronize records from a changing external API** | Incrementally copy and map paginated, rate-limited records into a local database | Resume partial runs; handle updates/deletes, schema changes, expiring credentials, throttling, inconsistent pages, and repeat runs; reconcile source and destination | One mock CRM API with versioned schemas, pages, mutations, limits, and injected failures |
| **B4.6 Process untrusted uploaded documents** | Upload, validate, scan, transform, track progress, download results, quarantine, and expire files | Block traversal, MIME spoofing, oversized/archive-bomb input, collisions, corruption, and processor failure; verify isolation, cleanup, and state transitions | One versioned benign/malicious file corpus and upload-operation trace |
| **B4.7 Deliver authenticated real-time notifications** | WebSocket or SSE subscriptions, persistence, acknowledgement, authorization, and reconnect recovery | Bound slow consumers; handle disconnects, missed/duplicate events, fan-out spikes, revoked access, and restart; verify replay and per-client ordering guarantees | One multi-client subscription/event trace with reconnects, revocation, and load bursts |
| **B4.8 Coordinate an order and sandbox payment** | Reserve inventory; authorize/capture; fulfill, cancel, refund, reconcile, and expose audit history | Prevent double charge and overselling; handle timeouts, duplicate webhooks, partial failure, concurrent orders, and invalid transitions; verify state-machine invariants | One seeded catalog plus sandbox-provider responses and concurrent order-event histories |
| **B4.9 Search one changing document collection** | Ingest/update/delete; fields, filters, highlighting, typo handling, ranking, pagination, and live reindexing | Handle empty/hostile queries, stale updates, duplicates, index failure, and zero-result cases; verify judged relevance, freshness, and reindex parity | One versioned document corpus with updates/deletes and judged queries |
| **B4.10 Edit shared documents from multiple clients** | Shared content, presence, concurrent edits, history, offline work, and reconnect | Resolve or expose conflicts; handle missed/duplicate operations, slow clients, offline edits, restart, and permission changes; verify convergence and history recovery | One deterministic multi-client operation trace with controlled network faults |
| **B4.11 Book capacity through expiring holds** | Availability, expiring holds, confirmation, cancellation, capacity management, and waitlist | Prevent double booking; handle concurrent holds, payment timeout, expiry races, timezones, cancellation, and promotion; verify capacity and audit invariants | One venue/resource calendar with fake-clock and concurrent booking traces |
| **B4.12 Import and export an evolving external schema** | Map schemas, validate, preview, execute resumably, and produce per-record success/error status | Handle duplicate identifiers, invalid references, encoding/schema changes, partial failure, retries, and files larger than memory; verify reconciliation and repeated-run behavior | One versioned external schema and generated record corpus with expected mappings and failures |

#### B5. Architecture and Distributed-System Problems

| Pattern and scenario | Implement or compare | Topology-specific failures and checks | Reference topology and workload |
|---|---|---|---|
| **B5.1 Host third-party extensions behind a stable plugin API** | Discovery, installation, configuration, enable/disable, versioning, lifecycle, permissions, quotas, and unloading | Isolate plugin failures; handle incompatible versions, dependency conflicts, host upgrades, malicious behavior, resource exhaustion, and permission revocation; verify lifecycle and compatibility | One host API plus versioned benign, incompatible, failing, and malicious plugin corpus |
| **B5.2 Cache a read-heavy product catalog** | Cache-aside reads, invalidation, TTL, stampede control, and a documented consistency model | Handle misses, stale values, eviction, cache outage, key collisions, concurrent writes, and hot keys; measure hit/staleness, latency, load, and recovery against uncached behavior | One seeded catalog plus versioned read/write request trace and cache-failure schedule |
| **B5.3 Compare message brokers on one job-delivery workflow** | RabbitMQ, Kafka, and Redis Streams producers/consumers using each system's documented semantics | Do not invent a common guarantee; record ordering, acknowledgement, retry, replay, priority, and dead-letter support; inject duplicates, poison jobs, consumer crash, partitions, and backlog | One versioned job-event stream, consumer topology, and failure schedule shared across brokers |
| **B5.4 Route three services through an API gateway** | Authentication, request IDs, quotas, rate limits, route/response transformation, and upstream health | Handle slow/down upstreams, retry amplification, oversized requests, configuration errors, partial gateway failure, and rolling backend changes; verify route/security policy and latency | One synthetic three-service topology plus normal, hostile, slow, and failing request traces |
| **B5.5 Maintain an order projection from versioned events** | Durable event log, versioned schemas, idempotent handlers, projections, replay, and rebuild | Handle duplicates, reordering, gaps, incompatible schemas, poison events, handler crash, and partial rebuild; verify projection invariants against a reference reducer | One versioned order-event history with expected projections and injected faults |
| **B5.6a Enforce distributed token-bucket limits** | Per-user/tenant/endpoint token buckets across several service instances | Bound clock skew and races; handle hot keys, store outage, bursts, refill precision, and fail-open/closed policy; compare accepted requests with a sequential model | One generated multi-tenant request trace, three limiter instances, and store-failure schedule |
| **B5.6b Enforce distributed sliding-window limits** | Exact or approximate sliding-window counters across several service instances | Bound clock/bucket error, races, hot keys, store outage, memory growth, and boundary bursts; compare acceptance error, memory, and latency with an exact model | The same generated request trace and topology used by B5.6a |
| **B5.7a Protect calls with a circuit breaker** | Timeouts, bounded retries, closed/open/half-open states, fallback, and recovery probes | Prevent retry storms; handle half-open races, dependency flapping, slow success, false recovery, and metric-window boundaries; verify state transitions and downstream load | One fault-injecting dependency with a deterministic latency/error timeline and steady caller workload |
| **B5.7b Isolate dependency pressure with bulkheads** | Separate concurrency limits, bounded queues, rejection, and resource pools for dependency classes | Prevent one slow class exhausting others; handle queue buildup, starvation, cancellation, capacity misallocation, and recovery; compare isolation and useful throughput | One service with fast, slow, and failing dependency classes plus a mixed request trace |
| **B5.8 Lease a singleton scheduled job safely** | Distributed lease, ownership token, renewal, release, and fencing | Handle process pause/crash, lease expiry, delayed messages, clock uncertainty, store failover, and stale owners; verify fencing and document the safety boundary | One multi-worker timeline corpus with controlled pauses, expiry, partitions, and ownership changes |
| **B5.9 Publish committed order events through an outbox** | Domain transaction plus outbox row, relay, publication marker, idempotent consumer, lag/replay handling | Inject publisher crash before/after send, duplicate delivery, backlog, database failover, and schema change; verify no committed event is lost and duplicates are harmless | One relational order/outbox schema plus versioned transactions and crash-point trace |
| **B5.10a Coordinate booking steps with an orchestrated saga** | Central state machine issuing commands, awaiting replies, timing out, compensating, and exposing operator state | Handle duplicate commands/replies, step timeout, failed compensation, irrecoverable state, orchestrator restart, and manual intervention; verify legal transitions | One booking workflow topology plus deterministic success/failure/compensation histories |
| **B5.10b Coordinate booking steps with a choreographed saga** | Services reacting to versioned events with local transactions, idempotency, compensation, and correlation | Handle duplicate/reordered/missing events, cyclic reactions, failed compensation, schema change, and invisible global state; reconstruct and verify workflow history | The same booking steps and failure histories used by B5.10a, expressed as events |
| **B5.11 Isolate tenants across shared application resources** | Tenant-aware data, caches, jobs, rate limits, configuration, audit, administration, and quotas | Prevent cross-tenant queries/IDs, cache leaks, missing background context, noisy neighbors, and export leakage; verify isolation at every boundary and per-tenant accounting | One synthetic tenant corpus with varied sizes, permissions, jobs, queries, and adversarial identifiers |
| **B5.12a Discover live service instances through leases** | Instance registration, lease renewal, metadata, health status, expiry, and watches | Handle stale entries, process pause, duplicate identity, flapping health, delayed renewals, registry outage, and rolling deployment; verify membership against a timeline model | One registry plus simulated instances and deterministic join/renew/fail/recover histories |
| **B5.12b Balance traffic across changing service instances** | Round-robin, least-loaded, or weighted routing with passive/active health and connection draining | Handle uneven work, slow nodes, flapping health, stale discovery, instance churn, sticky sessions where promised, and retry amplification; verify distribution/failover | One simulated backend pool plus weighted request costs and health/change timeline |

#### B6. Security and Trust-Boundary Problems

| Trust-boundary scenario | Protect or implement | Threat-specific constraints and checks | Adversarial corpus or workload |
|---|---|---|---|
| **B6.1 Accept untrusted uploaded files** | Safe naming, content validation, quarantine, scanning, isolated processing, expiry, and cleanup | Block traversal, MIME spoofing, executable content, archive bombs, oversized files, collisions, malicious metadata, and cleanup escape; verify rejection and isolation decisions | One versioned benign/malicious file corpus plus upload and expiry trace |
| **B6.2 Audit authorization in a vulnerable multi-tenant API** | Find, exploit, correct, and regression-test ownership, role, attribute, and tenant checks | Cover IDOR, privilege escalation, mass assignment, missing server checks, confused deputy behavior, stale permissions, and cross-tenant access; verify an allow/deny matrix | One deliberately vulnerable API with seeded users, tenants, resources, roles, and adversarial requests |
| **B6.3 Run untrusted plugins in a capability sandbox** | Declared capabilities, isolated storage, CPU/memory/time quotas, revocation, package verification, and audit | Prevent unrestricted file/network/process access, resource exhaustion, host escape, confused deputy use, and package tampering; verify denial and cleanup | One permission manifest format plus benign, overreaching, exhausting, and escape-attempt plugin corpus |
| **B6.4 Handle application secrets without leaking them** | Approved providers, least-privilege access, redaction, cache expiry, rotation, and audit metadata | Prevent source/image/log/error/trace leakage, unsafe fallback, stale credentials, broad permissions, accidental serialization, and rotation outage; scan all observable channels | One sample service with seeded secrets, provider failures, log/error paths, and rotation timeline |
| **B6.5 Authenticate requests between two services** | Canonical method/path/body/time/nonce representation, keyed signature, verification, replay defense, and key rotation | Reject altered bodies, replay, skew abuse, encoding/canonicalization differences, unknown/expired keys, and downgrade attempts; require independent implementations to agree | One published request-vector corpus containing valid, malformed, replayed, modified, and rotated-key cases |
| **B6.6 Defend a public query API against abuse** | Authentication, quotas, adaptive limits, pagination/cost bounds, safe errors, detection, and response controls | Resist credential stuffing, enumeration, scraping, quota evasion, expensive queries, and distributed bursts; measure false positives and graceful degradation | One normal/abusive client simulator with identities, queries, distributed bursts, and expected policy decisions |
| **B6.7 Parse an untrusted binary format within strict bounds** | Length-delimited parser with bounded input, nesting, allocations, decompression, and processing time | Handle malformed lengths, integer overflow, deep nesting, bombs, ambiguous encodings, unknown fields, and fuzz cases; verify termination and resource ceilings | One versioned format plus valid, corrupt, truncated, extreme, and generated fuzz corpus |
| **B6.8 Maintain a tamper-evident audit history** | Append-only records, actor/action/target/result/time/correlation fields, chaining or signatures, verification, access, and retention | Detect deletion, reordering, modification, and truncation; redact sensitive fields; handle clock disorder, high volume, key rotation, and expiry; verify tampering location | One generated audit stream plus deletion, reorder, mutation, truncation, clock-skew, and retention cases |

#### B7. Maintenance, Quality, and Performance Problems

| Maintenance scenario | Diagnose or change | Preservation and verification constraints | Starting artifact or workload |
|---|---|---|---|
| **B7.1 Characterize an untested order application before changing it** | Discover current behavior and dependencies, add characterization tests, then change one discount workflow | Preserve external behavior unless explicitly corrected; capture hidden file/database/time dependencies, nondeterminism, and error behavior; demonstrate the tests detect unintended changes | One seeded legacy order application with no tests and one requested discount-rule change |
| **B7.2 Migrate one web application across a major framework version** | Inventory deprecations, update code/configuration/dependencies, preserve deployment behavior, and prepare rollback | Handle removed APIs, changed defaults, dependency conflicts, configuration differences, stored sessions/data, and mixed deployment states; run old/new contract tests | One version-pinned web application, database fixture, request corpus, and source/target framework versions |
| **B7.3 Change one large database schema without downtime** | Apply expand/migrate/contract steps compatible with old/new application versions and resumable backfill | Avoid long locks and data loss; handle invalid legacy rows, partial backfill, restart, concurrent writes, deployment reversal, and rollback; verify row invariants and lock timing | One large seeded table, old/new application builds, and concurrent read/write trace |
| **B7.4 Evolve one API while old clients remain active** | Introduce a breaking resource-model change through versioning or compatibility translation and a retirement path | Handle mixed clients, stored old payloads, incompatible validation, retries, rollback, and telemetry; verify both client contracts throughout migration | One API, two generated clients, versioned payload corpus, and adoption timeline |
| **B7.5 Diagnose one slow product-search endpoint** | Reproduce, profile, identify the bottleneck, implement a measured improvement, and add a regression threshold | Preserve result ordering/content; distinguish cold/warm state; include realistic data, caching, contention, downstream limits, and repeated measurements | One seeded search service, database/index, query mix, load profile, and known bottleneck |
| **B7.6 Fix retained memory in a long-running worker** | Reproduce growth, inspect retained objects/resources, correct ownership/cleanup, and add a memory regression test | Distinguish leak from caches and fragmentation; test long runs, cancellation, exceptions, retries, and concurrency; compare stable-state memory after the fix | One deliberately leaking document worker and repeated job/error/cancellation trace |
| **B7.7 Fix one reproducible lost-update race** | Control scheduling, expose the violated invariant, implement a fix, and stress/model-test it | Preserve useful concurrency; verify balances and operation history; test retries and failures; do not replace the defect with unexplained global serialization | One seeded account-transfer service and deterministic concurrent operation schedule |
| **B7.8 Replace one abandoned parsing dependency** | Characterize behavior, add an adapter, migrate callers and stored formats, compare performance, and remove the dependency | Handle semantic/error differences, transitive dependencies, unsupported formats, security fixes, partial migration, and rollback; preserve the declared contract | One application, pinned abandoned parser, valid/malformed compatibility corpus, and replacement candidate |
| **B7.9 Retrofit tests around one risky order workflow** | Map behavior/risk, introduce seams and fixtures, add contract/integration/unit tests, and demonstrate caught defects | Avoid tests coupled only to internals or broad snapshots; control time, randomness, external payment calls, and slow fixtures; prioritize behavior over line coverage | One untested order application plus seeded historical failures and candidate mutants |
| **B7.10 Exercise one service under infrastructure faults** | Inject dependency latency/errors, process crash, disk exhaustion, and partial network failure; observe, mitigate, fix, and repeat | Keep experiments bounded; verify detection, graceful degradation, recovery, data integrity, cleanup, and absence of retry amplification | One seeded order service, steady transaction trace, fault schedule, and expected invariants |
| **B7.11a Support one application on two operating systems** | Remove or isolate platform assumptions in paths, permissions, processes, networking, time, encoding, and packaging | Preserve behavior; test case sensitivity, separators, line endings, signals, locale/timezone, unavailable OS features, install/upgrade, and CI reproducibility | One application and file/process/network corpus executed on two declared operating systems |
| **B7.11b Support one numeric tool on two CPU architectures** | Build, package, and verify the same tool and file format across declared architectures | Handle endianness, alignment, word size, SIMD availability, floating-point variation, native dependencies, and cross-compilation; define numeric tolerance | One numeric CLI/library, binary fixtures, golden calculations, and two declared CPU architectures |
| **B7.11c Support one application across two database versions** | Preserve schema, queries, migrations, backups, and deployment behavior across a declared upgrade path | Handle changed defaults/types/plans/features, extension availability, mixed application versions, upgrade order, rollback, and restored backups; compare contracts and query plans | One database-backed application, seeded dataset, query/migration corpus, and source/target database versions |
| **B7.12 Extract one domain inside a modular monolith** | Place one domain behind an internal API with clear dependencies, transaction ownership, and schema ownership while retaining one deployment | Prevent cycles, shared-table leakage, duplicated rules, accidental network assumptions, and migration dead ends; preserve external behavior and compare coupling before/after | One seeded monolith with an intentionally tangled billing or inventory domain and dependency tests |

---

### C. Infrastructure

Each row is a standalone operational problem. It defines its own system, workload, failure cases, and checks; no shared application or deployment standard is assumed. Within each track, common problems come first and difficulty generally increases.

| Track | Category | Typical problems |
|---|---|---|
| **C1** | Runtime and containers | Images, local environments, process lifecycle, and persistent storage |
| **C2** | Networking and traffic management | DNS, TLS, reverse proxies, load balancing, and network policy |
| **C3** | CI/CD and release engineering | Builds, artifacts, migrations, deployment strategies, and rollback |
| **C4** | Infrastructure as code and configuration | Provisioning, convergence, environment promotion, and drift |
| **C5** | Observability and incident response | Metrics, logs, traces, SLOs, alerts, and investigation |
| **C6** | Stateful infrastructure and recovery | Backups, PITR, replication, storage failure, and disaster recovery |
| **C7** | Orchestration, capacity, and resilience | Kubernetes, autoscaling, load testing, scheduling, and fault injection |
| **C8** | Infrastructure security and governance | Secrets, IAM, supply-chain controls, patching, policy, and cost |

#### C1. Runtime and Container Problems

| ID and operational scenario | Required behavior | Failures and constraints | Workload and checks |
|---|---|---|---|
| **C1.1 Containerize a web API** | Build and run the service with configuration, health checks, graceful shutdown, and a fixed application port | Run as non-root; exclude source secrets; handle signals correctly; keep the image reproducible | Fresh-clone build, HTTP requests, termination during traffic, image inspection |
| **C1.2 Run an API and PostgreSQL locally** | Start both services, initialize the schema, persist data, and expose readiness checks through Compose or an equivalent tool | Survive restarts; avoid startup races; separate configuration from secrets; fail clearly when the database is unavailable | Create/read fixture, stop/start cycle, volume inspection, unavailable-database test |
| **C1.3 Produce a small production image** | Use multi-stage builds, pinned dependencies, minimal runtime files, and architecture-aware artifacts | Preserve debugging information where required; avoid package-manager caches, build tools, and writable application files | Compare cold build, cached build, image size, startup time, and vulnerability scan |
| **C1.4 Operate a bounded worker process** | Consume jobs, report health, stop gracefully, and respect CPU, memory, file, and process limits | Handle a killed worker, stuck job, memory exhaustion, temporary filesystem exhaustion, and duplicate delivery | Synthetic jobs, resource limits, forced termination, restart and duplicate-processing checks |

#### C2. Networking and Traffic-Management Problems

| ID and operational scenario | Required behavior | Failures and constraints | Workload and checks |
|---|---|---|---|
| **C2.1 Put three API instances behind a TLS reverse proxy** | Terminate TLS, balance requests, preserve request metadata, and remove unhealthy instances | Handle slow instances, uploads, WebSockets, certificate renewal, and graceful backend shutdown | Load generator, synthetic slow backend, certificate-expiry rehearsal, routing distribution |
| **C2.2 Publish a service through DNS** | Configure records, validate resolution, change the destination, and retire the old endpoint | Account for TTLs, negative caching, partial propagation, resolver differences, and rollback | Local or delegated test zone, repeated queries from multiple resolvers, timed cutover |
| **C2.3 Route traffic by host and path** | Send multiple applications through one edge while preserving authentication, headers, and client addresses | Reject ambiguous routes and header spoofing; bound request size and timeout; return useful upstream errors | Synthetic upstreams, route matrix, hostile headers, timeout and unavailable-route tests |
| **C2.4 Balance stateful and stateless traffic** | Compare round-robin, least-connections, hashing, and explicit session storage | Handle uneven request cost, instance churn, hot keys, retry duplication, and unhealthy nodes | Skewed sessions, instance add/remove events, distribution and recovery measurements |
| **C2.5 Isolate application tiers** | Permit only required flows among edge, application, database, administration, and monitoring components | Deny lateral movement and unintended egress without breaking DNS, updates, or observability | Connectivity matrix, allowed/denied probes, compromised-service simulation, policy audit |

#### C3. CI/CD and Release-Engineering Problems

| ID and operational scenario | Required behavior | Failures and constraints | Workload and checks |
|---|---|---|---|
| **C3.1 Build and test every proposed change** | Restore dependencies, lint, test, package, cache safe work, and report failures | Prevent cache poisoning and secret exposure; support clean runners and deterministic dependency resolution | Passing/failing commits, cold and warm runs, altered lockfile, test-report inspection |
| **C3.2 Publish a versioned artifact once** | Create an immutable package or image, attach source/version metadata, and promote the same artifact between environments | Reject duplicate or mutable versions; preserve provenance; prevent credentials from entering artifacts | Tagged and untagged commits, artifact checksum, metadata inspection, promotion rehearsal |
| **C3.3 Deploy an API with a database migration** | Run compatibility checks, apply an expand/migrate/contract change, verify health, and roll back the application | Handle failed tests, interrupted migration, mixed application versions, failed health checks, and concurrent release attempts | Disposable environment, seeded database, forced failure at each stage, rollback checks |
| **C3.4 Perform a zero-downtime rolling release** | Replace instances gradually while preserving availability and draining in-flight work | Detect crash loops; respect readiness; avoid serving incompatible versions; stop rollout on regression | Continuous traffic, long requests, unhealthy release, error-rate and availability timeline |
| **C3.5 Compare blue-green and canary releases** | Shift traffic in controlled steps, evaluate release health, and return safely to the previous version | Bound false promotion from noisy metrics; handle sticky sessions, asynchronous jobs, and schema compatibility | Stable and defective releases, synthetic business metric, automatic/manual rollback rehearsal |

#### C4. Infrastructure-as-Code and Configuration Problems

| ID and operational scenario | Required behavior | Failures and constraints | Workload and checks |
|---|---|---|---|
| **C4.1 Provision one disposable application environment** | Create network, compute, database, identities, and outputs from declarative configuration | Pin providers; avoid plaintext secrets; make repeated plans empty; destroy only owned resources | Isolated test account or local cloud emulator, first/second plan comparison, ownership labels |
| **C4.2 Reuse infrastructure across development and production** | Extract modules while keeping environment-specific sizes, domains, access, and retention policies explicit | Prevent accidental production defaults, hidden module coupling, broad permissions, and state collisions | Two isolated environments, configuration matrix, plan review, cross-environment access probes |
| **C4.3 Detect and reconcile configuration drift** | Identify a manual resource change and either import, accept, or revert it deliberately | Preserve externally managed attributes; distinguish harmless from dangerous drift; avoid destructive replacement | Controlled console change, saved plans, state backup, reconciliation and replacement test |
| **C4.4 Configure a small server fleet convergently** | Install packages, create users, configure a service, rotate configuration, and restart only when necessary | Support repeated runs, partial failure, unreachable hosts, version differences, and secrets | Fresh and partially configured hosts, two consecutive runs, check mode, failed-host recovery |
| **C4.5 Change shared infrastructure safely** | Preview dependency effects, serialize conflicting changes, gate destructive actions, and recover state | Handle stale plans, concurrent runs, locked or lost state, provider failure, and partial application | Competing changes, forced interruption, remote-state recovery, dependency and blast-radius review |

#### C5. Observability and Incident-Response Problems

| ID and operational scenario | Required behavior | Failures and constraints | Workload and checks |
|---|---|---|---|
| **C5.1 Monitor a single HTTP service** | Expose request rate, errors, latency, saturation, build version, and dependency health | Bound label cardinality; distinguish application failure from scrape failure; avoid averages hiding tail latency | Normal, slow, erroring, and saturated traffic; dashboard and alert-value inspection |
| **C5.2 Trace one request across three services** | Propagate trace and correlation context through HTTP, messaging, logs, and database spans | Handle retries, asynchronous boundaries, missing context, sampling, sensitive attributes, and clock differences | Known request path, retry and queue scenarios, trace completeness and search checks |
| **C5.3 Diagnose intermittent checkout latency** | Use metrics, structured logs, profiles, and traces to identify the responsible component | Limit telemetry volume and cardinality; account for sampling and coincidental correlated failures | Load generator, injected database/network/CPU delays, expected bottleneck timeline |
| **C5.4 Define and alert on a service-level objective** | Select a user-visible indicator, calculate error-budget consumption, and page on meaningful burn | Avoid alerting on harmless internal symptoms; handle low traffic, missing data, maintenance, and brief spikes | Generated good/bad requests, slow burn and fast burn, alert timing and false-positive review |
| **C5.5 Run an incident from detection through review** | Triage, assign roles, mitigate, communicate, recover, and produce follow-up actions | Work with incomplete evidence; preserve a timeline; avoid destructive diagnosis; verify recovery | Injected production-like failure, stale runbook clue, status updates, recurrence test |
| **C5.6 Operate telemetry at high volume** | Apply sampling, aggregation, retention, indexing, and access controls while preserving diagnostic value | Bound ingestion and storage cost; handle backpressure, collector loss, high-cardinality fields, and sensitive data | Generated logs/metrics/traces, collector outage, cost and query-latency comparison |

#### C6. Stateful Infrastructure and Recovery Problems

| ID and operational scenario | Required behavior | Failures and constraints | Workload and checks |
|---|---|---|---|
| **C6.1 Back up and restore a small database** | Create automated backups, retain them, restore into a clean instance, and verify application data | Encrypt backups; separate credentials; detect incomplete copies; do not treat backup creation as proof of recovery | Seeded records, checksums and row invariants, expired backup, timed restore |
| **C6.2 Recover to the moment before an accidental deletion** | Combine base backups and transaction logs to restore to a selected timestamp | Meet stated RPO/RTO; handle missing or corrupt archive segments; avoid overwriting the source | Generated transaction history, deletion event, multiple recovery targets, timed rehearsal |
| **C6.3 Fail over a replicated database** | Promote a replica, redirect clients, prevent split brain, and rejoin or rebuild the former primary | Account for replication lag, client retries, stale reads, network partition, and lost acknowledgements | Continuous writes, primary termination, partition simulation, acknowledged-write comparison |
| **C6.4 Recover from storage exhaustion or corruption** | Detect the condition, stop unsafe writes, expand or replace storage, and validate recovered state | Preserve forensic evidence; handle partial files, full transaction logs, unavailable snapshots, and slow copying | Bounded test volume, forced disk-full event, corrupted blocks/files, integrity verification |
| **C6.5 Restore a service in a second environment** | Recreate infrastructure, restore state, change routing, validate dependencies, and return to normal operation | Use explicit RPO/RTO; handle stale infrastructure code, missing secrets, external dependencies, and DNS delay | Region/account-like isolation, backup copy, dependency checklist, full timed exercise |

#### C7. Orchestration, Capacity, and Resilience Problems

| ID and operational scenario | Required behavior | Failures and constraints | Workload and checks |
|---|---|---|---|
| **C7.1 Deploy an API and worker to Kubernetes** | Define workloads, services, configuration, health probes, resource requests/limits, and controlled updates | Handle bad configuration, crash loops, graceful shutdown, unavailable dependency, and rollback | Local cluster, synthetic jobs and HTTP traffic, pod deletion, rollout status and recovery |
| **C7.2 Load-test an API to find its first bottleneck** | Generate realistic traffic, measure throughput and latency, locate saturation, and confirm one improvement | Separate client from server limits; control warm-up, data distribution, caching, think time, and coordinated omission | Read/write mixes, cold/warm runs, resource profiles, repeatable before/after comparison |
| **C7.3 Autoscale a service under bursty traffic** | Scale from demand while maintaining a latency or queue-delay target | Handle cold starts, noisy metrics, downstream saturation, oscillation, and delayed scale-down | Steady, burst, spike, and recovery workloads; replica count, p95 latency, errors, queue depth |
| **C7.4 Schedule mixed workloads on a constrained cluster** | Place latency-sensitive services, batch jobs, and specialized hardware workloads using explicit priorities | Avoid starvation and unsafe eviction; handle resource fragmentation, affinity rules, and node loss | Synthetic workloads, one unavailable node, pending-work timeline, utilization and eviction review |
| **C7.5 Test resilience to infrastructure failures** | Inject process, node, network, dependency, and storage faults and verify bounded degradation and recovery | Keep experiments scoped; stop on unsafe conditions; prevent retry storms and hidden data loss | Fault schedule, steady traffic, service-level indicators, recovery and invariant checks |
| **C7.6 Capacity-plan a growing service** | Forecast resource demand, determine safe headroom, and compare scaling or architecture options | Include peaks, growth uncertainty, quotas, redundancy, downstream limits, and cost discontinuities | Historical or generated demand, benchmark curves, failure headroom, sensitivity scenarios |

#### C8. Infrastructure Security and Governance Problems

| ID and operational scenario | Required behavior | Failures and constraints | Workload and checks |
|---|---|---|---|
| **C8.1 Rotate a database credential without downtime** | Issue a new credential, update consumers, revoke the old one, and record the operation | Prevent secret logging, stale workers, broad permissions, and indefinite dual credentials | Multiple service instances, deliberately stale client, leak scan, connection monitoring |
| **C8.2 Give a deployment pipeline least privilege** | Permit artifact publication and deployment only to declared environments and resources | Prevent privilege escalation, untrusted-fork secrets, lateral access, confused deputy behavior, and persistent credentials | Allowed/denied action matrix, pull-request and protected-branch runs, audit-log review |
| **C8.3 Secure the container supply chain** | Pin dependencies, generate an SBOM, scan artifacts, sign releases, and verify policy before deployment | Handle vulnerable base images, compromised tags, expired keys, unavailable scanners, and approved exceptions | Clean/vulnerable/tampered images, signature verification, exception expiry, provenance inspection |
| **C8.4 Patch a running server or node fleet** | Inventory versions, stage an update, preserve capacity, reboot where required, and verify service health | Handle incompatible packages, failed nodes, limited redundancy, rollback, and emergency exposure | Mixed-version fleet, canary node, forced patch failure, version and availability checks |
| **C8.5 Enforce infrastructure policy automatically** | Reject public storage, unrestricted ingress, missing encryption, unowned resources, and prohibited regions | Distinguish deny, warn, and exception cases; test nested modules and existing resources | Compliant/noncompliant plans, time-bounded exception, policy-unit and integration cases |
| **C8.6 Reduce infrastructure cost without violating reliability targets** | Attribute cost, find waste, evaluate rightsizing or scheduling, and verify savings after change | Preserve SLOs, redundancy, recovery objectives, contractual commitments, and peak capacity | Billing export or generated costs, utilization series, peak load test, before/after cost and SLO review |

---

### D. Mathematical Foundations and Computational Verification

Mathematics supports the problems in A, B, and C rather than forming a separate catalog of applications. The goal is to understand each concept, derive its central results, verify them computationally, and reimplement only the mechanisms that expose important ideas.

For each concept family:

1. Learn the definitions, assumptions, and central results.
2. Derive at least one important identity or algorithm.
3. Verify small cases manually or symbolically.
4. Reimplement a compact reference method where useful.
5. Compare it with a trusted tool and test adversarial cases.
6. Connect it to concrete work in A, B, or C.

| Track | Concept family | Strongest connections |
|---|---|---|
| **D1** | Linear algebra and geometry | ML, graphics, search, optimization, and scientific computing |
| **D2** | Calculus and numerical analysis | Optimization, simulation, scientific software, and model training |
| **D3** | Probability and statistics | ML, experimentation, forecasting, reliability, and monitoring |
| **D4** | Optimization and operations research | Model training, scheduling, routing, allocation, and capacity planning |
| **D5** | Discrete mathematics and theoretical CS | Algorithms, databases, languages, distributed systems, and security |
| **D6** | Information theory, signals, and transforms | ML, compression, communications, audio, vision, and observability |
| **D7** | Dynamical systems, stochastic processes, and control | Forecasting, queues, autoscaling, reliability, and sensor systems |
| **D8** | Numerical reliability and mathematical verification | Every numerical result in A, B, and C |

#### D1. Linear Algebra and Geometry

| Concept family | Theory to understand | Connections to A/B/C | Programmatic verification | Reimplement | Tools |
|---|---|---|---|---|---|
| **D1.1 Vectors, norms, and similarity** | Vector operations; inner products; norm axioms; angles; metric properties; cosine similarity | **A:** k-NN, embeddings, clustering; **B:** vector search; **C:** telemetry comparison | Check norm/metric axioms; compare geometric identities; test zero and nearly parallel vectors | Vector operations, common norms, cosine and distance functions | NumPy, SymPy, Hypothesis |
| **D1.2 Vector spaces, basis, and projections** | Span; independence; basis; dimension; orthogonality; subspaces; projections | **A:** regression, feature spaces; **B:** graphics; **C:** dimensional telemetry analysis | Verify basis rank, projection idempotence, orthogonality, and coordinate reconstruction | Gram–Schmidt and orthogonal projection | NumPy, SciPy, SymPy |
| **D1.3 Linear systems and conditioning** | Rank; null space; existence and uniqueness; conditioning; perturbation sensitivity | **A:** regression; **B:** numerical libraries; **C:** capacity and estimation models | Measure residual and forward error; perturb inputs; compare well- and ill-conditioned systems | Gaussian elimination with partial pivoting and triangular solves | NumPy, SciPy, mpmath |
| **D1.4 Matrix decompositions and least squares** | LU, QR, Cholesky; normal equations; orthogonal least squares | **A:** linear models; **B:** scientific components; **C:** parameter estimation | Reconstruct matrices; verify orthogonality/triangularity; compare residuals and stability | Householder QR and Cholesky decomposition | NumPy, SciPy |
| **D1.5 Eigenvalues, SVD, and low-rank structure** | Eigenvectors; spectral theorem; singular values; rank approximation; pseudoinverse | **A:** PCA, recommenders, spectral methods; **B:** compression and search | Check eigen equations, orthogonality, reconstruction, explained energy, and sign ambiguity | Power iteration and truncated SVD for small matrices | NumPy, SciPy, randomized linear-algebra tools |
| **D1.6 Sparse and structured linear algebra** | COO/CSR/CSC; sparsity; fill-in; iterative methods; preconditioning; tensor products | **A:** graphs and text; **B:** indexes; **C:** dependency and network models | Compare sparse/dense parity; plot residual convergence; measure memory and fill-in | CSR matrix-vector multiplication and conjugate gradient | SciPy Sparse, SuiteSparse, PyTorch/JAX sparse tools |
| **D1.7 Geometry and coordinate transformations** | Affine/projective transforms; rotations; homogeneous coordinates; distances; intersections | **A:** vision and geospatial ML; **B:** graphics and spatial indexes; **C:** maps and topology | Test inverse/composition identities, rotation invariants, degeneracy, and coordinate round trips | 2-D/3-D transforms and robust orientation tests | NumPy, Shapely, GeoPandas, symbolic algebra |

#### D2. Calculus and Numerical Analysis

| Concept family | Theory to understand | Connections to A/B/C | Programmatic verification | Reimplement | Tools |
|---|---|---|---|---|---|
| **D2.1 Derivatives and local approximation** | Limits; continuity; derivatives; gradients; Jacobians; Hessians; Taylor expansion | **A:** training and sensitivity; **B:** numerical APIs; **C:** response curves | Compare analytic, finite-difference, complex-step, and automatic derivatives; verify Taylor error order | Central differences and multivariable gradient/Jacobian | SymPy, NumPy, JAX/PyTorch |
| **D2.2 Multivariable and constrained calculus** | Directional derivatives; chain rule; implicit differentiation; Lagrange multipliers | **A:** constrained learning; **B:** geometry; **C:** resource tradeoffs | Check directional derivatives and stationarity; visualize feasible surfaces; compare symbolic results | Lagrange-multiplier solver for small systems | SymPy, SciPy, JAX |
| **D2.3 Root finding and fixed points** | Bracketing; convergence order; contraction mappings; Newton, secant, and bisection methods | **A:** calibration; **B:** numerical software; **C:** equilibrium calculations | Verify residuals and convergence rates; test flat derivatives, multiple roots, and bad initial values | Bisection, secant, Newton, and stopping rules | SciPy, SymPy, mpmath |
| **D2.4 Interpolation and approximation** | Polynomial interpolation; splines; approximation error; Runge phenomenon | **A:** feature construction; **B:** graphics; **C:** sensor and capacity curves | Recover known polynomials; measure interpolation error; test irregular points, noise, and extrapolation | Barycentric interpolation and cubic splines | NumPy, SciPy, SymPy |
| **D2.5 Numerical integration** | Quadrature; truncation error; adaptive rules; multidimensional integration | **A:** probability calculations; **B:** scientific software; **C:** accumulated utilization | Compare with analytic integrals; verify convergence order; test singular, peaked, and oscillatory functions | Trapezoid, Simpson, and adaptive quadrature | SciPy, SymPy, mpmath |
| **D2.6 Differential equations** | Initial/boundary-value problems; stability; stiffness; local/global error | **A:** continuous-time models; **B:** simulation software; **C:** system dynamics | Compare with analytic solutions; test conserved quantities, step sensitivity, stiffness, and event handling | Euler, midpoint, and Runge–Kutta integrators | SciPy, SymPy, JAX differential-equation tools |
| **D2.7 Automatic differentiation** | Dual numbers; computation graphs; forward/reverse accumulation; higher derivatives | **A:** neural networks and optimization; **B:** differentiable software | Compare against symbolic and numerical derivatives; test branching, reused variables, and nondifferentiable points | Dual numbers and a small reverse-mode graph | JAX, PyTorch, SymPy |

#### D3. Probability and Statistics

| Concept family | Theory to understand | Connections to A/B/C | Programmatic verification | Reimplement | Tools |
|---|---|---|---|---|---|
| **D3.1 Probability, conditioning, and independence** | Events; axioms; conditional probability; Bayes' rule; independence; total probability | **A:** probabilistic models; **B:** randomized algorithms; **C:** failure diagnosis | Enumerate finite spaces; simulate conditional frequencies; construct counterexamples to intuitive claims | Finite probability engine and Bayes calculator | Python/Julia/R, SymPy Stats, NumPy |
| **D3.2 Random variables and distributions** | PMF/PDF/CDF; expectation; variance; covariance; transformations; common families | **A:** loss and uncertainty; **B:** randomized tests; **C:** arrivals and failures | Compare samples with theoretical moments/CDFs; apply probability-integral-transform checks | Inverse-CDF and rejection samplers for selected distributions | NumPy, SciPy, R |
| **D3.3 Limit theorems and concentration** | Laws of large numbers; central limit theorem; concentration bounds; asymptotics | **A:** sampling and evaluation; **B:** randomized algorithms; **C:** aggregate traffic | Simulate convergence; compare finite-sample tails with bounds; vary dependence and tail weight | Running estimates and standardized-sum simulation | NumPy, SciPy, plotting tools |
| **D3.4 Estimation and likelihood** | Bias; variance; consistency; efficiency; sufficient statistics; maximum likelihood | **A:** model fitting; **B:** telemetry summaries; **C:** parameter estimation | Generate known truth; measure estimator bias/variance and likelihood curvature over repetitions | Common estimators and one-dimensional MLE | SciPy, statsmodels, SymPy |
| **D3.5 Intervals, tests, and experimental design** | Confidence intervals; hypothesis tests; power; effect size; multiple testing; sequential analysis | **A:** evaluation and causal work; **B:** product experiments; **C:** operational experiments | Measure coverage, false-positive rate, and power; test optional stopping and assumption violations | Bootstrap interval, permutation test, and power simulation | SciPy, statsmodels, R |
| **D3.6 Regression and dependence** | Linear/GLM assumptions; covariance; correlation; confounding; residual analysis | **A:** prediction and causality; **B:** performance modeling; **C:** capacity analysis | Recover synthetic coefficients; inspect residuals; introduce collinearity, heteroscedasticity, and confounding | OLS and logistic likelihood with uncertainty estimates | NumPy, statsmodels, scikit-learn |
| **D3.7 Bayesian inference** | Priors; likelihood; posterior; conjugacy; hierarchical models; posterior prediction | **A:** probabilistic ML; **B:** decision software; **C:** reliability inference | Compare analytic and sampled posteriors; use prior/posterior predictive checks and simulation-based calibration | Grid posterior, conjugate update, Metropolis–Hastings, and Gibbs sampler | PyMC, Stan, NumPyro, ArviZ |
| **D3.8 Monte Carlo and resampling** | Monte Carlo error; importance sampling; variance reduction; bootstrap; MCMC diagnostics | **A:** uncertainty; **B:** randomized systems; **C:** risk and capacity simulation | Compare with analytic truth; plot error versus samples; check ESS, autocorrelation, and reproducibility | Bootstrap, importance sampling, and basic MCMC | NumPy, SciPy, ArviZ |
| **D3.9 Time, survival, and rare events** | Stationarity; autocorrelation; censoring; hazards; extremes; rare-event probability | **A:** forecasting and anomaly detection; **B:** event systems; **C:** reliability and incidents | Simulate known processes; verify coverage/calibration; test censoring, drift, and tail misspecification | Autocorrelation, Kaplan–Meier, and rare-event simulation | statsmodels, lifelines, SciPy |

#### D4. Optimization and Operations Research

| Concept family | Theory to understand | Connections to A/B/C | Programmatic verification | Reimplement | Tools |
|---|---|---|---|---|---|
| **D4.1 Convexity and optimality** | Convex sets/functions; subgradients; local/global optima; smoothness; strong convexity | **A:** loss functions; **B:** algorithm choice; **C:** resource planning | Plot slices; test convexity inequalities numerically; check gradients, Hessians, and known minima | Convexity checks for simple functions | SymPy, NumPy, CVXPY |
| **D4.2 First- and second-order optimization** | Gradient descent; momentum; stochastic gradients; Newton and quasi-Newton methods | **A:** model training; **B:** numerical libraries; **C:** parameter tuning | Plot objective/gradient norms; compare convergence rates; vary scaling, noise, and initialization | Gradient descent, Newton, BFGS, and line search | SciPy Optimize, JAX/PyTorch |
| **D4.3 Constraints, duality, and KKT conditions** | Equality/inequality constraints; Lagrangians; duality; complementary slackness | **A:** constrained models; **B:** policy engines; **C:** capacity limits | Independently check feasibility, KKT conditions, complementary slackness, and duality gap | Projected gradient and small equality-constrained solver | CVXPY, SciPy, SymPy |
| **D4.4 Linear and integer optimization** | Linear programs; simplex/interior-point ideas; integrality; relaxations; branch and bound | **A:** decision models; **B:** schedulers; **C:** placement and capacity | Compare with exhaustive search on small cases; check feasibility, objective bounds, and infeasibility | Small simplex or branch-and-bound demonstration | OR-Tools, CVXPY, HiGHS |
| **D4.5 Networks, flows, and matching** | Shortest paths; max-flow/min-cut; min-cost flow; bipartite and stable matching | **A:** graph ML baselines; **B:** routing and scheduling; **C:** network planning | Check flow conservation and cut equality; compare small graphs with enumeration | Dijkstra, max-flow, and bipartite matching | NetworkX, OR-Tools |
| **D4.6 Dynamic, online, and sequential decisions** | Bellman equations; dynamic programming; bandits; regret; model-predictive decisions | **A:** reinforcement/bandit learning; **B:** schedulers; **C:** autoscaling | Compare small cases with exhaustive search; verify Bellman consistency; simulate regret | Tabular dynamic programming and basic bandit policies | NumPy, OR-Tools, Gymnasium-style environments |
| **D4.7 Robust and multi-objective decisions** | Sensitivity; uncertainty sets; Pareto fronts; scalarization; risk-aware objectives | **A:** robust learning; **B:** product tradeoffs; **C:** reliability/cost planning | Perturb inputs; plot Pareto fronts; verify dominance and feasibility across scenarios | Sensitivity analysis and weighted-objective search | CVXPY, SciPy, pymoo |

#### D5. Discrete Mathematics and Theoretical Computer Science

| Concept family | Theory to understand | Connections to A/B/C | Programmatic verification | Reimplement | Tools |
|---|---|---|---|---|---|
| **D5.1 Logic and proof methods** | Propositions; predicates; implication; induction; contradiction; invariants | **A:** model assumptions; **B:** program correctness; **C:** operational invariants | Truth-table enumeration; bounded counterexample search; property checks | Formula evaluator and invariant checker for a small state machine | SymPy Logic, Z3, property-based testing |
| **D5.2 Sets, relations, and functions** | Equivalence/order relations; mappings; closure; lattices; partial orders | **A:** labels and partitions; **B:** schemas and permissions; **C:** dependency ordering | Check reflexivity/symmetry/transitivity and order properties on finite structures | Relation-property and transitive-closure utilities | Python sets, NetworkX, Z3 |
| **D5.3 Counting and combinatorics** | Permutations; combinations; inclusion–exclusion; pigeonhole principle; generating functions | **A:** sampling spaces; **B:** test combinations; **C:** configuration explosion | Compare formulas with enumeration; generate counterexamples; study asymptotic growth | Combination generator and exact counters | Python itertools, SymPy Combinatorics |
| **D5.4 Recurrences and complexity** | Recurrence solving; asymptotic notation; amortized and expected analysis; lower bounds | **A:** algorithm scaling; **B:** data structures; **C:** load growth | Fit empirical growth; count operations; compare recurrence solutions with measurements | Instrumented recurrence and amortized-cost simulations | SymPy, benchmarking/profiling tools |
| **D5.5 Graphs and trees** | Connectivity; traversal; trees; DAGs; cuts; coloring; planarity; spectral properties | **A:** graph learning; **B:** indexes and dependencies; **C:** service/network topology | Check invariants and certificates; compare small cases with enumeration or trusted libraries | BFS/DFS, topological sort, union-find, and selected graph certificates | NetworkX, graph generators, Graphviz |
| **D5.6 Automata, grammars, and computation** | Finite automata; regular/context-free languages; parsing; computability; decidability | **A:** sequence models; **B:** parsers and protocols; **C:** configuration validation | Generate accepted/rejected strings; compare parser and recognizer; test ambiguity and state reachability | DFA/NFA simulator and small parser | parser generators, automata libraries, model checkers |
| **D5.7 Hashing, coding, and modular arithmetic** | Universal hashing; collision probability; error-detecting codes; primes; congruences | **A:** feature hashing; **B:** hash tables/compression/security; **C:** integrity checks | Measure collision distribution and avalanche behavior; inject bit errors; compare exact modular identities | Universal hash, Bloom-filter math, checksum/code demonstration | Python integers, SymPy Number Theory, statistical tests |
| **D5.8 Models of concurrency and distribution** | Partial orders; happens-before; safety/liveness; consensus models; impossibility boundaries | **B:** locks, queues, replication; **C:** failover and orchestration | Enumerate bounded schedules; search invariant violations; simulate delay, loss, duplication, and partitions | Small state-machine and interleaving explorer | TLA+/PlusCal, Alloy, Spin, Jepsen-style histories |

#### D6. Information Theory, Signals, and Transforms

| Concept family | Theory to understand | Connections to A/B/C | Programmatic verification | Reimplement | Tools |
|---|---|---|---|---|---|
| **D6.1 Entropy and information** | Entropy; conditional entropy; cross-entropy; KL divergence; mutual information | **A:** losses and feature selection; **B:** compression; **C:** telemetry volume | Check non-negativity and identities; estimate from known distributions; expose estimator bias | Discrete entropy, cross-entropy, KL, and mutual information | NumPy, SciPy, SymPy |
| **D6.2 Coding and compression limits** | Prefix codes; source coding; redundancy; rate-distortion ideas | **A:** representation learning; **B:** Huffman/LZ; **C:** log and trace compression | Verify prefix-free decoding; compare empirical bits with entropy; test skewed sources | Huffman coding and simple dictionary compression | bit-level libraries, compression tools |
| **D6.3 Sampling, quantization, and aliasing** | Sampling theorem; reconstruction; quantization error; dynamic range | **A:** audio/vision; **B:** media processing; **C:** metric collection | Sweep sample rate and bit depth; measure reconstruction error; demonstrate alias frequencies | Sampler, quantizer, and sinc-style reconstruction | NumPy, SciPy Signal, audio/image tools |
| **D6.4 Convolution and correlation** | Linear systems; kernels; convolution theorem; autocorrelation/cross-correlation | **A:** CNNs and time series; **B:** signal/image code; **C:** lag analysis | Compare direct and transform implementations; test impulse response and boundary modes | Direct 1-D/2-D convolution and correlation | NumPy, SciPy Signal, PyTorch |
| **D6.5 Fourier and time-frequency analysis** | Fourier series; DFT/FFT; spectra; windows; leakage; wavelets | **A:** audio, vision, forecasting; **B:** compression; **C:** periodic telemetry | Verify inverse reconstruction and Parseval's identity; test leakage, aliasing, and resolution | DFT, radix-2 FFT, and basic spectral estimator | NumPy FFT, SciPy Signal, PyWavelets |
| **D6.6 Noise, filtering, and reconstruction** | Signal-to-noise ratio; linear filters; regularization; spectral filtering; sparse reconstruction | **A:** denoising and anomaly detection; **B:** media tools; **C:** noisy sensors | Add controlled noise; compare frequency response and reconstruction error; test boundary effects | Moving-average/FIR filter and regularized reconstruction | SciPy Signal, CVXPY, audio/image datasets |

#### D7. Dynamical Systems, Stochastic Processes, and Control

| Concept family | Theory to understand | Connections to A/B/C | Programmatic verification | Reimplement | Tools |
|---|---|---|---|---|---|
| **D7.1 Difference equations and state evolution** | Discrete-time systems; recurrence dynamics; equilibria; growth and decay | **A:** forecasting; **B:** stateful workflows; **C:** resource evolution | Compare closed forms and simulation; locate equilibria; vary parameters and initial conditions | Difference-equation simulator | NumPy, SymPy, plotting tools |
| **D7.2 Stability and continuous dynamics** | Phase space; linearization; eigenvalue stability; oscillation; nonlinear behavior | **A:** continuous models; **B:** simulation; **C:** feedback behavior | Plot phase portraits; perturb equilibria; test conservation and solver sensitivity | Small phase-plane and stability analyzer | SciPy Integrate, SymPy, control libraries |
| **D7.3 Markov chains and hidden states** | Transition matrices; stationary distributions; recurrence; absorption; hidden Markov models | **A:** sequences; **B:** state machines; **C:** health-state models | Verify stochastic matrices; compare analytic stationary/absorption results with simulation | Markov simulator, forward algorithm, and Viterbi decoder | NumPy, SciPy, probabilistic libraries |
| **D7.4 Arrivals, queues, and renewal processes** | Poisson processes; interarrival/service models; Little's Law; M/M/1 and M/M/c; renewal theory | **A:** event modeling; **B:** workers/queues; **C:** capacity and latency | Compare simulated and theoretical utilization/waiting time; test bursts and non-Poisson arrivals | Discrete-event M/M/1 and M/M/c simulation | SimPy, NumPy, SciPy |
| **D7.5 State estimation and filtering** | State-space models; observability; Kalman, extended, and particle filters | **A:** tracking and forecasting; **B:** sensor software; **C:** operational estimation | Simulate known trajectories; check covariance calibration, missing observations, and nonlinear failure | Linear Kalman filter | FilterPy, NumPy, SciPy |
| **D7.6 Feedback, reliability, and repair** | Feedback loops; stability margins; reliability blocks; hazards; repair/availability models | **A:** online systems; **B:** retry/control behavior; **C:** autoscaling and resilience | Simulate step responses and failures; compare reliability formulas; test delay and feedback oscillation | PID controller and series/parallel reliability calculator | python-control, SimPy, SciPy |

#### D8. Numerical Reliability and Mathematical Verification

| Concept family | Theory to understand | Connections to A/B/C | Programmatic verification | Reimplement | Tools |
|---|---|---|---|---|---|
| **D8.1 Floating-point representation** | Radix; precision; rounding; machine epsilon; special values; non-associativity | Every numerical calculation | Inspect encodings; find adjacent values; reproduce overflow, underflow, cancellation, and order effects | Minimal floating-point experiments and ULP distance | Python `float`, NumPy, language/runtime numeric tools |
| **D8.2 Conditioning and algorithmic stability** | Problem conditioning; forward/backward error; stable reformulation; perturbation theory | Linear algebra, optimization, simulation, and statistics | Perturb inputs; measure residual/forward error; compare formulations on ill-conditioned cases | Condition estimates and residual-based checks | NumPy, SciPy, mpmath |
| **D8.3 Stable reductions and probability calculations** | Error accumulation; compensated/pairwise summation; log-domain arithmetic | **A:** losses/probabilities; **B:** aggregation; **C:** telemetry summaries | Compare input orders and precisions against high-precision references | Kahan/pairwise sum, log-sum-exp, stable softmax | NumPy, mpmath, decimal libraries |
| **D8.4 Exact, interval, and arbitrary-precision computation** | Rational arithmetic; interval containment; precision selection; validated numerics | **A:** reference checks; **B:** financial/geometry code; **C:** integrity calculations | Cross-check floats; prove containment; increase precision until stable; report indeterminate cases | Rational and interval demonstrations | fractions/decimal, mpmath, interval libraries |
| **D8.5 Randomness and reproducibility** | PRNG state; streams; seed derivation; independence; deterministic parallelism | **A:** training/sampling; **B:** tests; **C:** simulations | Replay runs; change worker counts; test duplicated streams and distribution quality | Explicit random-stream manager and replayable simulation | NumPy random generators, statistical test suites |
| **D8.6 Convergence and complexity experiments** | Empirical error order; asymptotic cost; constants; stopping criteria | Algorithm selection throughout A, B, and C | Sweep size/step/iterations; fit slopes; separate warm-up, compilation, transfer, and execution | Benchmark and convergence harness | pytest-benchmark, profilers, plotting tools |
| **D8.7 Property-based and adversarial verification** | Invariants; metamorphic relations; boundary analysis; counterexamples | Correctness throughout A, B, and C | Generate structured cases; compare trusted implementations; shrink failures; violate assumptions deliberately | Reusable numeric strategies, tolerant comparisons, and invariant checks | Hypothesis/QuickCheck, SymPy, Z3, trusted numerical libraries |

#### Mathematical Verification Ladder

Use the methods that fit the concept; not every method applies to every result.

| Method | What it establishes |
|---|---|
| **1. Hand-checkable cases** | Tiny examples agree with manual calculation or exhaustive enumeration |
| **2. Algebraic invariants** | Properties such as normalization, conservation, feasibility, symmetry, orthogonality, or reconstruction hold |
| **3. Symbolic verification** | Expressions, derivatives, identities, or recurrences simplify to the expected result |
| **4. Differential testing** | Independent implementations or trusted libraries agree within a justified tolerance |
| **5. High-precision reference** | Floating-point results agree with exact, interval, or higher-precision calculations |
| **6. Simulation with known truth** | Estimators, intervals, or inference procedures recover generated parameters at expected rates |
| **7. Convergence experiment** | Error decreases at the predicted rate as samples, iterations, or resolution increase |
| **8. Property-based testing** | Identities and metamorphic relations hold over broad generated inputs |
| **9. Adversarial cases** | Degenerate, ill-conditioned, extreme, or near-boundary inputs fail safely or remain accurate |
| **10. Assumption violations** | The consequences of dependence, drift, outliers, nonconvexity, or model misspecification are understood |

#### Selective Reimplementation Checklist

Reimplement compact mechanisms that reveal the mathematics. Use production libraries for broad capability, then compare them against the reference implementation.

| Family | High-value implementations |
|---|---|
| **Linear algebra** | Gaussian elimination with pivoting, Householder QR, power iteration, sparse matrix-vector multiplication |
| **Calculus and numerical analysis** | Finite differences, Newton/bisection, adaptive quadrature, Runge–Kutta, small autodiff engine |
| **Probability and statistics** | Distribution samplers, bootstrap, maximum likelihood, Metropolis–Hastings, Gibbs sampling |
| **Optimization** | Gradient descent, Newton/BFGS, projected gradient, small simplex or branch-and-bound demonstration |
| **Discrete mathematics** | Graph traversals, union-find, shortest path, max-flow, automaton simulator, bounded state explorer |
| **Signals and control** | DFT/FFT, convolution, spectral estimator, Kalman filter, PID controller |
| **Numerical reliability** | Kahan/pairwise summation, log-sum-exp, stable softmax, gradient checker, interval demonstration |

#### Boundary with the Engineering Sections

| Section | Primary question |
|---|---|
| **D — Mathematics** | Why does the method work, when does it fail, and how can its result be verified? |
| **A — Data Science / ML** | How is the method used to build and evaluate a data or ML capability? |
| **B — Software Development** | How is the behavior implemented as reliable, maintainable software? |
| **C — Infrastructure** | How are systems that depend on it deployed, operated, scaled, and recovered? |

---

## Group 2: Integrated Systems Programs

These programs connect many independently useful parts into larger systems. 

---

### A. Domain Programs

Domain programs provide the users, data, workflows, and reasons for connecting technical components.

The ecosystem notes below are reminders, not prescribed architectures. Components and boundaries should emerge during project development.

| Program | Main problem | Possible parts | Example progress signals |
|---|---|---|---|
| **Marketing Intelligence Platform** | Turn changing market information into timely, trustworthy research, statistics, reports, and alerts | Scraping/APIs, source versioning, entity resolution, NLP, search, statistics, reports, alerts, agents, API/UI | Entity/source coverage, freshness, change-detection quality, alert precision, supported claims, report time/cost |
| **Job Opportunity Intelligence Platform** | Collect active vacancies and help users discover suitable opportunities through CV upload, free-text intent, filters, saved searches, and subscriptions | Compliant connectors, vacancy versioning, normalization, deduplication, CV parsing, taxonomy mapping, hybrid search, ranking, explanations, alerts, feedback, API/UI | Source coverage, freshness, active-status accuracy, duplicate rate, hard-filter compliance, ranking relevance, alert precision, time to discovery |
| **GIS/Open-Data Intelligence Platform** | Integrate spatial and public data to support geographic search, monitoring, analysis, and decisions | Spatial ETL, validation, geocoding, PostGIS/DuckDB Spatial, tiles, search, change detection, forecasting, maps | Geographic/attribute coverage, geometry validity, freshness, spatial correctness, query latency, analyst task time |
| **Document Intelligence Platform** | Turn documents into validated, searchable, structured, and actionable information | Upload, OCR, layout analysis, extraction, validation, review queues, search, workflow, audit | Field accuracy, CER/WER, review rate, document throughput, retrieval quality, unsupported extraction rate |
| **Learning and Practice Platform** | Turn learning material into trustworthy practice and adapt future study using review results | PDF/EPUB/HTML ingestion, OCR, concept extraction, flashcards, cloze and language exercises, evidence checks, review, scheduling, Anki export | Card acceptance/edit rate, source support, duplicate/ambiguity rate, time per accepted card, retention, review burden |
| **Game or Simulated-World Platform** | Create a controllable data-generating environment containing users, agents, events, economies, and decisions | Simulation/game loop, agents, events, marketplace, matchmaking, inventories, telemetry, search, recommendation, abuse detection | Simulation invariants, agent performance, economy stability, discovery quality, fairness, latency, resource use |

#### Marketing Intelligence as a Component Ecosystem

| Reminder | Essentials |
|---|---|
| **Core loop** | Sources → versioned history → entity resolution → analysis/search → reports and alerts |
| **Useful signals** | Coverage, freshness, change-detection quality, alert precision, supported claims, report time/cost |
| **Watch for** | Source changes, duplicates, weak provenance, unsupported claims, stale information, and noisy alerts |

#### Job Opportunity Intelligence as a Component Ecosystem

| Reminder | Essentials |
|---|---|
| **Core loop** | Permitted sources → normalized/versioned active vacancies → CV, text, or filters → retrieval/ranking → explanations → saved searches and alerts |
| **Interaction modes** | CV upload with editable extraction, free-text intent, hard filters, combined search, and immediate or periodic subscriptions |
| **Useful signals** | Freshness, active-status accuracy, duplicate rate, filter violations, ranking relevance, explanation correctness, alert precision, time to discovery |
| **Watch for** | Source terms and breakage, stale/reposted or fraudulent ads, ambiguous fields, CV privacy, ranking bias, unsupported inferences, and notification spam |

#### Learning and Practice as a Component Ecosystem

| Reminder | Essentials |
|---|---|
| **Core loop** | Learning material → extraction and concepts → cards/cloze/exercises → verification and review → Anki or built-in practice → learning feedback |
| **Modes** | Knowledge study through definitions, formulas, diagrams, and comparisons; language practice through vocabulary, grammar, cloze, listening, and pronunciation |
| **Useful signals** | Acceptance/edit rate, source support, duplicate/ambiguity rate, time per accepted item, retention, recurring errors, and review burden |
| **Watch for** | Educationally weak or ambiguous items, missing context, OCR/formula errors, excessive card volume, copyright/DRM limits, and personal-data exposure |

#### Feasible Data Starting Points

- Marketing or media intelligence can use regularly updated sources such as [GDELT](https://www.gdeltproject.org/data.html?source=post_page---------------------------), subject to source quality and licensing checks.
- Job-opportunity work can begin with permitted APIs/feeds, public research data, or a replayable synthetic vacancy corpus; preserve source provenance and expiry while avoiding collection that violates access terms.
- GIS work can begin with regional [OpenStreetMap extracts](https://wiki.openstreetmap.org/wiki/Extracts) rather than planet-scale processing.
- Learning work can begin with owned, licensed, or public-domain PDFs and EPUBs, personal notes, open course material, subtitles, and transcripts; preserve page/section references and avoid bypassing DRM.
- A game, marketplace, logistics simulation, or agent tournament can generate controlled events, interactions, graphs, transactions, and rare cases.

---

### B. Capability Systems

These can be standalone studies, but often become more meaningful when attached to a domain program.

| Capability | Main question | Possible host programs | Example progress signals |
|---|---|---|---|
| **Search and retrieval** | Can the system return the most useful available information while keeping the index fresh and responsive? | Marketing, job vacancies, documents, GIS, research, games | Recall/MRR/NDCG, zero-result rate, freshness, latency, indexing throughput, cost |
| **Recommendation and ranking** | Can the system rank useful items for a user or context while maintaining coverage and freshness? | Vacancies, products, content, locations, research sources, game items | Recall/NDCG, coverage, diversity, novelty, cold-start quality, freshness, latency |
| **Alerting and workflow automation** | Can meaningful changes trigger timely action without overwhelming users? | Marketing, job vacancies, GIS, simulated equipment, marketplaces, infrastructure | Detection delay, alert precision, missed-event rate, acknowledgement time, automation success |
| **Agentic research and analysis** | Can bounded research or analysis tasks be completed correctly, reproducibly, and with appropriate human involvement? | Marketing, GIS, documents, data exploration | Task completion, supported claims, calculation correctness, intervention rate, recovery, cost/latency |
| **OCR and information extraction** | Can unstructured documents become trustworthy structured records? | Documents, CVs, finance, public records, maps | Recognition/field accuracy, review rate, throughput, confidence calibration, schema validity |
| **Forecasting, anomaly, and failure-risk estimation** | Can future behavior, unusual events, or failure likelihood be estimated early enough to support action? | Simulated equipment, infrastructure, finance, games | Forecast error, interval coverage, calibration, event precision/recall, detection delay, alert volume |
| **Risk, fraud, and abuse detection** | Can suspicious accounts, events, transactions, or relationships be prioritized within a limited review capacity? | Games, synthetic marketplaces, payment simulations, identity/account systems | Precision at review capacity, expected loss, calibration, investigation time, drift, false-positive burden |

Search and recommendation may start inside a domain program. They can become standalone systems when the corpus or catalog, evaluation data, update behavior, permissions, traffic, or availability requirements make that separation useful.

Useful data ladders include:

- [BEIR](https://github.com/beir-cellar/beir) for retrieval evaluation across different domains; generated documents and traffic can separately test systems scale.
- [MovieLens](https://grouplens.org/datasets/movielens/) for recommendation experiments ranging from small development data to larger and synthetic variants.

Without real user interaction, offline recommendation results and simulated feedback should be presented as such rather than treated as direct evidence of user value.

---

### C. Platform Programs

Platform programs provide reusable foundations. They need not be built in this order, and a substantial component may first emerge inside a domain program.

| Program | Main purpose | Natural signs that it is useful |
|---|---|---|
| **Data Acquisition Framework** | Reusable scraping, API ingestion, scheduling, checkpointing, versioning, and validation | Several sources share lifecycle concerns; failures need consistent recovery and visibility |
| **Data Platform** | Collection, processing, storage, cataloging, quality, lineage, and data access | Multiple workflows need dependable historical and current data rather than isolated files |
| **MLOps Platform** | Experiments, datasets, models, evaluation, deployment, and monitoring | Several models repeat lifecycle work or require consistent comparison and promotion |
| **Feature Platform** | Reusable batch and online features with freshness and point-in-time correctness | Multiple models share features or require consistent training/serving values |
| **Lakehouse** | Large historical tables, schema evolution, partitioning, and distributed analytics | Data volume, history, concurrency, or processing patterns exceed simpler storage approaches |
| **Enterprise AI Platform** | Shared model access, permissions, governance, quotas, auditing, and tenant isolation | Multiple teams or applications require common controls and observable resource use |
| **Autonomous Analysis Platform** | Bounded automated analysis, model experimentation, verification, and human approval | A collection of recurring, evaluable tasks exists and tool behavior can be constrained |

These programs may evolve loosely:

```text
Reusable acquisition
  → shared data capabilities
    → model and feature capabilities
      → larger-scale storage and processing
        → shared governance and bounded automation
```

This is an extension path, not a prescribed architecture. A reusable platform is easier to evaluate when it has concrete consumers, but even one demanding consumer may justify focused platform work.

“Autonomous Data Scientist” is better treated as a possible direction within bounded autonomous analysis. Start with identifiable task families, datasets, tools, verification methods, and approval points rather than assuming unrestricted autonomy.

---

### D. Simulation and Scale Laboratories

These programs investigate architecture, scale, feedback, or failure behavior under controlled conditions. They may use components from any domain or platform program.

| Laboratory | Questions to explore | Suitable data or workload |
|---|---|---|
| **Distributed Search** | Partitioning, replication, routing, index updates, rebalancing, failure recovery, and tail latency | Judged corpus for relevance plus generated/replayed volume for systems behavior |
| **Distributed Recommendation** | Candidate generation, partitioned embeddings, freshness, batching, caching, and degraded operation | Public interactions, simulated users, expanded catalog, replayed requests |
| **Stream Processing and Recovery** | Ordering, event time, watermarks, checkpoints, duplicates, backpressure, and replay | Generated or replayed event streams with injected late, duplicate, and missing events |
| **Lakehouse Tables and Queries** | Partitioning, compaction, schema evolution, concurrent writes, metadata scale, and query planning | Generated tables plus smaller semantically meaningful datasets |
| **Feature Consistency** | Point-in-time joins, offline/online parity, freshness, backfills, and leakage | Versioned event and entity histories with known expected features |
| **Multi-Tenant Data Systems** | Isolation, quotas, noisy neighbors, tenant-specific configuration, and cost attribution | Synthetic tenants with varied data size, query patterns, and permissions |
| **Multi-Region Failure Exercise** | Replication lag, routing, recovery objectives, split brain, and reconciliation | Continuous generated transactions and controlled network/process failures |
| **Equipment Monitoring and Maintenance Simulation** | Sensor generation, degradation, failure, maintenance effects, alert capacity, streaming, and recovery | Simulated equipment states, noisy telemetry, injected faults, work orders, and known failure causes |
| **Transaction Risk and Abuse Simulation** | Account behavior, transactions, collusion, compromise, disputes, investigation, delayed labels, and adversarial adaptation | Synthetic marketplace or payment rules that generate normal and abusive behavior with known ground truth |
| **Game Economy and Agent Simulation** | Feedback loops, economies, agents, ranking, experimentation, and behavioral drift | Rules and agents that generate users, items, interactions, transactions, events, and ground truth |

The system does not need to claim that its domain requires internet scale. It can state explicitly that distribution, consistency, throughput, cost, or recovery is the subject of the experiment.

### Ways to Deepen Any Program

- Add a new data source, user workflow, consumer, or domain.
- Replace a manual step with observable, recoverable automation.
- Compare a high-level platform with a minimal implementation.
- Introduce delayed, duplicated, missing, corrupt, or adversarial data.
- Establish realistic latency, throughput, freshness, recovery, or cost budgets.
- Add authentication, authorization, encryption, auditing, and secret management where relevant.
- Exercise backup, restore, rollback, graceful degradation, and disaster recovery.
- Improve metrics, logs, traces, dashboards, runbooks, and incident diagnosis.
- Test an unfamiliar language, runtime, deployment environment, or operating constraint.
- Extract a reusable component, connect an existing one, or simplify an unnecessary abstraction.

> Start wherever the data and interest make sense. Build useful parts, connect them where the connection teaches something, assess current shortcomings, and expand only in directions that add value or answer a deliberate engineering question.
