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
  - [Purpose and Ways to Use the Programs](#purpose-and-ways-to-use-the-programs)
  - [Rough Maturity Guide](#rough-maturity-guide)
  - [Project Compass](#project-compass)
  - [Data and Scale Modes](#data-and-scale-modes)
  - [Open-Ended Progress Measures](#open-ended-progress-measures)
  - [A. Domain Programs](#a-domain-programs)
    - [Marketing Intelligence as a Component Ecosystem](#marketing-intelligence-as-a-component-ecosystem)
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

| Track | Practice mode | Purpose |
|---|---|---|
| **A1** | Rebuild algorithms | Learn mechanics; compare with production libraries. |
| **A2** | Compare specialized tools | Learn capabilities, tradeoffs, and failure modes. |
| **A3** | Solve problem families | Choose baselines, validation, metrics, and deployment constraints. |
| **A4** | Implement across languages/runtimes | Prove model parity, portability, and performance outside notebooks. |

#### A1. Foundational Algorithms: Rebuild, Verify, Compare

Build the smallest correct version; use mature libraries as the benchmark.

| Challenge and scenario | Implement | Constraints and checks | Datasets |
|---|---|---|---|
| **A1.1 Interpretable tabular prediction:** estimate house values and conversion probabilities | OLS via normal equation and QR/SVD; gradient descent; logistic loss; L1/L2 | Recover synthetic coefficients; check gradients; test collinearity, scaling, outliers, and separation; match scikit-learn/statsmodels | [California Housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html), [Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset), [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) |
| **A1.2 Explainable rule prediction:** classify applicants and predict quality using inspectable trees | CART splits; classification/regression loss; stopping; pruning; missing/categorical values | Hand-check splits; test constant/repeated features, missing values, and depth; match scikit-learn predictions | [Adult](https://archive.ics.uci.edu/dataset/2/adult), [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality), synthetic XOR |
| **A1.3 Reduce unstable tree predictions:** classify land cover with bagged trees | Bootstrap samples; feature subsampling; OOB score; parallel trees; permutation importance | Measure variance and OOB/test agreement; test seeding, correlated features, and imbalance; compare `RandomForest`/`ExtraTrees` | [Covertype](https://archive.ics.uci.edu/dataset/31/covertype), Adult, synthetic nonlinear data |
| **A1.4 Fit difficult tabular relationships:** improve residual errors stage by stage | Residual trees; learning rate; subsampling; early stopping; regression and logistic loss | Track stage loss and overfitting; vary learning rate/tree count; compare scikit-learn and boosting-library behavior | [HIGGS](https://archive.ics.uci.edu/dataset/280/higgs), Adult, California Housing |
| **A1.5 Retrieve similar records:** classify small data and search high-dimensional neighbors | Brute-force k-NN; distance metrics; weighting; KD-tree or ball-tree | Test ties, scaling, irrelevant dimensions, latency, and memory; compare exact and FAISS/HNSW search | [Wine](https://archive.ics.uci.edu/dataset/109/wine), [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist), synthetic vectors |
| **A1.6 Classify sparse text with limited compute:** predict topics or sentiment from token counts | Gaussian, multinomial, and Bernoulli Naive Bayes; smoothing; log likelihoods; TF-IDF | Test zero counts, underflow, unknown terms, imbalance, and calibration; compare logistic regression | [20 Newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html), [IMDb](https://ai.stanford.edu/~amaas/data/sentiment/) |
| **A1.7 Discover customer groups without labels:** compare hard and probabilistic clusters | k-means++; Lloyd's algorithm; empty-cluster recovery; EM; soft assignment | Test initialization, scaling, non-spherical clusters, local minima, and covariance failure; match scikit-learn | [Wholesale Customers](https://archive.ics.uci.edu/dataset/292/wholesale+customers), Wine, synthetic blobs/moons/rings |
| **A1.8 Learn nonlinear image boundaries from arrays only:** train a small neural classifier | Dense layers; activations; cross-entropy; backprop; SGD/Adam; dropout; checkpoints | Numerical gradient checks; overfit a tiny batch; test exploding/vanishing gradients; match PyTorch/JAX/TensorFlow | [MNIST](https://www.openml.org/d/554), Fashion-MNIST, synthetic 2-D data |
| **A1.9 Separate classes with maximum margin:** compare linear and kernel boundaries | Linear hinge-loss solver; soft margin; kernels; simplified SMO | Check KKT conditions, margins, scaling, support-vector count, and kernel cost; match `LinearSVC`/`SVC` | Synthetic margins, [Wine](https://archive.ics.uci.edu/dataset/109/wine), Fashion-MNIST subset |
| **A1.10 Decode hidden activity states:** infer a state sequence from noisy observations | Forward/backward; Viterbi; Baum–Welch; log-space probabilities | Check likelihood monotonicity, decoding on known sequences, missing observations, and underflow; compare hmmlearn/pomegranate | Synthetic state sequences, [UCI HAR](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones), speech/activity sequences |
| **A1.11 Rank sparse user–item interactions:** learn preferences with pairwise features | Matrix factorization; factorization machines; SGD/ALS; implicit feedback | Test sparse updates, regularization, ranking, negative sampling, and cold start; compare implicit/LightFM | [MovieLens](https://grouplens.org/datasets/movielens/), [Amazon Reviews](https://amazon-reviews-2023.github.io/) |

#### A2. Specialized Library Laboratories

Use identical splits, preprocessing, metrics, and compute budgets.

| Laboratory and scenario | Compare | Constraints and checks | Datasets |
|---|---|---|---|
| **A2.1 Choose a boosting library for mixed tabular data under limited memory** | XGBoost, LightGBM, CatBoost | Identical splits and compute limits; categoricals, missing/sparse values, constraints, calibration, CPU/GPU, export parity, latency | Adult, HIGGS, California Housing, synthetic high-cardinality categoricals |
| **A2.2 Tune models within a fixed one-hour budget** | Random search, successive halving, Optuna/Ray Tune; AutoGluon, FLAML, or H2O | Same search space/budget; nested validation, pruning, resumption, reproducibility, and leaderboard overfitting | Adult, Bank Marketing, Covertype |
| **A2.3 Select 500 rare cases for daily review** | Under/oversampling, SMOTE, balanced ensembles, class weights, focal loss | Resample only inside CV; calibrate probabilities; compare precision@500, recall, and expected cost under prevalence shift | [Credit Card Fraud](https://www.openml.org/d/1597), [Mammography](https://www.openml.org/d/310), synthetic rare events |
| **A2.4 Choose a forecasting toolkit for hundreds of related series** | statsmodels/StatsForecast, Prophet, MLForecast/sktime, Darts/NeuralForecast | Missing intervals, known exogenous data, hierarchies, interval coverage, rolling backtests, intermittency, cold start | [M4](https://github.com/Mcompetitions/M4-methods/tree/master/Dataset), [Electricity Load](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014), intermittent demand |
| **A2.5 Choose a vision stack for training and edge inference** | OpenCV, torchvision/KerasCV, timm, Albumentations, YOLO | Identical splits; transfer learning, augmentation, NMS, mixed precision, export parity, memory, edge latency | [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html), [Oxford Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/), [COCO](https://cocodataset.org/) subset |
| **A2.6 Choose an NLP stack for a domain classifier and semantic encoder** | spaCy, Transformers, Sentence Transformers, TF-IDF | Tokenization/truncation parity, batching, domain/language shift, quantization, calibration, throughput, memory | 20 Newsgroups, IMDb, [AG News](https://huggingface.co/datasets/fancyzhx/ag_news), labeled domain corpus |
| **A2.7 Extract text and fields from noisy documents** | Tesseract, PaddleOCR, EasyOCR, docTR or cloud OCR | Hold preprocessing constant; test rotation, layout, tables, handwriting, languages, confidence, CPU/GPU throughput | [IAM](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database), [FUNSD](https://guillaumejaume.github.io/FUNSD/), corrupted receipts |
| **A2.8 Select a vector engine for filtered semantic retrieval** | FAISS, pgvector, Qdrant/Milvus, Elasticsearch/OpenSearch | Exact vs HNSW/IVF; recall/latency/memory, filters, updates/deletes, persistence, replication, embedding migration | [ANN Benchmarks](https://ann-benchmarks.com/), [BEIR](https://github.com/beir-cellar/beir), synthetic vectors |
| **A2.9 Explain and monitor a model as data changes** | SHAP/permutation importance; Pandera/Great Expectations; Evidently/custom metrics | Correlated features, explanation stability, schema drift, delayed labels, reference windows, alert false positives, sensitive fields | Adult, California Housing, synthetically shifted copies |
| **A2.10 Process regional vector and raster data without spatial leakage** | GeoPandas/Shapely, Rasterio/rioxarray, PyProj, DuckDB Spatial/PostGIS | CRS, spatial joins, invalid geometry, raster alignment, indexes, projection distortion, spatial holdouts | [Natural Earth](https://www.naturalearthdata.com/), [OSM extracts](https://download.geofabrik.de/), land-cover tiles |
| **A2.11 Choose an audio stack for classification, ASR, and separation** | FFmpeg/TorchCodec; librosa; torchaudio transforms; Transformers; SpeechBrain | Resampling/channel parity, spectrograms/MFCCs, augmentation, batching, streaming, export, CPU/GPU latency | [UrbanSound8K](https://urbansounddataset.weebly.com/urbansound8k.html), [Speech Commands](https://www.tensorflow.org/datasets/catalog/speech_commands), [LibriSpeech](https://www.openslr.org/12), [MUSDB18](https://sigsep.github.io/datasets/musdb.html) |
| **A2.12 Fit a hierarchical model with uncertain group effects** | PyMC, Stan, NumPyro | Match priors/likelihoods; compare MCMC and VI; diagnose convergence, ESS, divergences, and posterior predictive fit | Eight Schools, radon-style hierarchy, synthetic mixtures |
| **A2.13 Learn from a changing event stream under bounded memory** | River vs incremental and retrained scikit-learn models | Progressive validation, abrupt/gradual drift, delayed labels, memory, update latency, detector false alarms, recovery | [Electricity](https://www.openml.org/d/151), synthetic drift streams |
| **A2.14 Predict links or node labels in a graph too large for full-batch training** | PyTorch Geometric, DGL, NetworkX/non-neural baseline | Temporal splits, message passing, sampling, batching, inductive nodes, explainability, memory/scaling | Cora/Citeseer, [Open Graph Benchmark](https://ogb.stanford.edu/), MovieLens graph |
| **A2.15 Add prediction intervals or sets to an existing model** | MAPIE vs calibrated probabilities, quantile regression, ordinary intervals | Marginal/group coverage, interval width, exchangeability, shift, calibration-set size, abstention rate | California Housing, Adult, M4 |
| **A2.16 Process data larger than memory and survive skewed joins** | Polars, DuckDB, Dask, Spark, Ray | Same transformations; bounded memory, lazy execution, partitioning, skew, spill, worker failure, correctness parity | [NYC Taxi](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), ClickBench, generated scale tests |
| **A2.17 Choose a runtime for low-latency model serving** | Framework-native inference, ONNX Runtime, TensorRT, OpenVINO | Prediction/export parity, dynamic shapes, quantization loss, batching, warm-up, throughput, p95/p99 latency, memory | ResNet, small transformer, boosted trees |

#### A3. Applied Problem Families and Typical Solution Methods

Start with a cheap baseline. Match validation to future use; add complexity only when it improves the decision.

| Problem and scenario | Methods | Decision constraints and metrics | Datasets |
|---|---|---|---|
| **A3.1 Predict a customer outcome or numeric value from mixed business data** | Rules/mean; linear models; trees; forests; boosting; calibrated ensembles | Missingness, categoricals, leakage, group/time splits, calibration, confidence, cost-based thresholds | Adult, Bank Marketing, California Housing, Bike Sharing, Wine Quality |
| **A3.2 Select 500 transactions from 100,000 for daily fraud review** | Rules; class weights; sampling/SMOTE; balanced ensembles; focal loss; calibrated thresholds | Time splits, delayed/noisy labels, precision@500, recall, calibration, expected loss, segment and prevalence drift | Credit Card Fraud, Mammography, synthetic drifting fraud |
| **A3.3 Plan inventory or staffing several periods ahead** | Seasonal naive; ETS; ARIMA/SARIMAX; Prophet; lagged boosting; global neural models | Rolling origin, interval coverage, available exogenous data, holidays, intermittency, hierarchy reconciliation | M4, Electricity Load, Bike Sharing, retail sales |
| **A3.4 Alert operators to sensor failures without flooding them** | Rules; robust z-scores; seasonal residuals; isolation forest; LOF; one-class SVM; autoencoders; change-point methods | Event-level precision/recall, alert grouping, seasonality, detection delay, threshold stability, daily alert capacity | [NAB](https://github.com/numenta/NAB), [NASA C-MAPSS](https://data.nasa.gov/dataset/c-mapss-aircraft-engine-simulator-data/xaut-bemq/about_data), synthetic sensor faults |
| **A3.5 Create customer segments that lead to different actions** | RFM rules; k-means/k-medoids; GMM; hierarchical clustering; DBSCAN/HDBSCAN | Scaling, mixed types, seed and temporal stability, minimum segment size, interpretability, actionability vs simple rules | Wholesale Customers, retail transactions, synthetic customer data |
| **A3.6 Rank a small set of relevant items for each user** | Popularity/recency; k-NN; matrix factorization; implicit models; two-tower retrieval; hybrid ranking | Temporal splits, negative sampling, cold start, seen-item filtering, diversity, coverage, feedback loops | [MovieLens](https://grouplens.org/datasets/movielens/), [Amazon Reviews](https://amazon-reviews-2023.github.io/), synthetic catalog |
| **A3.7 Return the best documents for a query within a latency budget** | BM25; boosts/filters; embedding retrieval; cross-encoder; pairwise/listwise ranking | NDCG/MRR/Recall@K, query slices, position bias, hard negatives, index freshness, p95 latency | BEIR, [MS MARCO](https://microsoft.github.io/msmarco/), judged domain corpus |
| **A3.8 Route text and extract named fields with human review for uncertainty** | Rules; TF-IDF plus linear model; embeddings; transformer fine-tuning; token classification; schema-bound LLM | Label agreement, long documents, rare labels, span metrics, calibration, domain/language shift, review capacity | AG News, 20 Newsgroups, IMDb, [CoNLL-2003](https://www.clips.uantwerpen.be/conll2003/ner/) |
| **A3.9 Progress from image labels to object verification in one visual domain** | CNN/ViT classification; YOLO/Faster R-CNN detection; U-Net/Mask R-CNN segmentation; embedding/metric-learning verification | Duplicate/subject leakage; class metrics; mAP; IoU/Dice; verification ROC; camera shift; edge latency | CIFAR-10; COCO; Oxford Pet/Cityscapes; LFW |
| **A3.10 Convert noisy forms, receipts, or handwriting into validated fields** | Cleanup/deskew; detection and recognition; layout; key-value extraction; tables; validation rules | CER/WER, field exact match, reading order, rotations, handwriting/languages, confidence, privacy | IAM, FUNSD, [RVL-CDIP](https://adamharley.com/rvl-cdip/), corrupted receipts |
| **A3.11 Search an internal corpus using human-judged queries** | BM25; bi-encoder; hybrid retrieval; expansion; filters; reranking; ANN | Hard negatives, Recall@K/MRR/NDCG, query slices, multilingual queries, stale/deleted documents, migration, latency/recall | BEIR, MS MARCO, versioned domain corpus |
| **A3.12 Answer questions over controlled documents with citations and abstention** | Chunk/retrieve baseline; query rewrite; hybrid search; reranking; parent-child; HyDE; routing | Evaluate ingestion, retrieval, and answers separately; citation support, unanswerable questions, permissions, injection, cost, latency | BEIR, [Natural Questions](https://ai.google.com/research/NaturalQuestions/), [HotpotQA](https://hotpotqa.github.io/), versioned documents |
| **A3.13 Automate a bounded tool-use workflow only when it beats fixed orchestration** | Deterministic workflow; single-agent tools; planner/executor; verification; multi-agent variant | Task success/partial credit, tool errors, retries, budgets, trace quality, safety, recovery, reproducibility, cost | Synthetic tasks, [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA), [SWE-bench](https://www.swebench.com/) |
| **A3.14 Estimate which customers benefit from an intervention** | Experiment baseline; adjustment; matching/weighting; difference-in-differences; causal forests; S/T/X/R learners | Define estimand/causal graph; overlap, balance, post-treatment leakage, uncertainty, sensitivity/placebo tests | [LaLonde/NSW](https://users.nber.org/~rdehejia/data/nswdata2.html), [IHDP](https://www.fredjo.com/), synthetic known effects |
| **A3.15 Estimate time until failure, churn, or another censored event** | Kaplan–Meier; log-rank; Cox; AFT; survival forests; competing risks | Censoring, time-varying features, PH assumption, concordance, horizon calibration, future leakage | [METABRIC](https://www.cbioportal.org/study/summary?id=brca_metabric), Rossi, synthetic failures |
| **A3.16 Progress from sound classification to speech and speaker tasks** | Audio/music classification; keyword spotting; event detection; ASR; enhancement/separation; speaker verification | Speaker/device/session-disjoint splits, clip leakage, macro F1/mAP, WER, SI-SDR, EER, noise robustness, real-time factor | UrbanSound8K/GTZAN; Speech Commands; DCASE/AudioSet; LibriSpeech/Common Voice; MUSDB18/DNS Challenge |
| **A3.17 Evaluate consent-based facial and biometric tasks** | Face detection/landmarks; age estimation; liveness/PAD; 1:1 verification; 1:N identification | Identity-disjoint splits, age MAE, FAR/FRR/EER, TAR@FAR, demographic slices, spoofing, consent, retention, licenses | [WIDER FACE](http://shuoyang1213.me/WIDERFACE/), [300-W](https://ibug.doc.ic.ac.uk/resources/300-W/), [UTKFace](https://susanqq.github.io/UTKFace/), [FairFace](https://github.com/joojs/fairface), [CelebA-Spoof](https://github.com/Davidzhangyuanhan/CelebA-Spoof), [LFW](http://vis-www.cs.umass.edu/lfw/) |
| **A3.18 Return prediction intervals or sets instead of unsupported certainty** | Calibrated probabilities; quantile regression; conformal intervals/sets; selective prediction | Coverage and width, calibration by slice, exchangeability, distribution shift, calibration size, abstention cost | California Housing, Adult, M4 |
| **A3.19 Update predictions continuously as behavior changes** | Incremental linear/tree models; sliding windows; ensembles; drift detectors; retraining policies | Prequential metrics, delayed labels, abrupt/gradual/recurring drift, false alarms, memory, update latency | Electricity, click streams, synthetic drift |
| **A3.20 Detect suspicious links or classify new entities in a network** | Graph heuristics; embeddings; GCN/GAT/GraphSAGE; link prediction; graph classification | Temporal edge splits, negative sampling, neighborhood leakage, inductive nodes, sampling bias, graph shift | Cora/Citeseer, OGB, molecular or transaction graphs |
| **A3.21 Reach useful quality when labels are expensive** | Uncertainty/diversity sampling; pseudo-labeling; consistency training; labeling functions; label models | Performance per label, annotator disagreement, selection bias, confirmation bias, rare-class coverage | 20 Newsgroups, CIFAR-10, synthetic rare classes |
| **A3.22 Assign multiple taxonomy-consistent labels to each item** | Binary relevance; classifier chains; label embeddings; hierarchy-aware loss; constrained decoding | Micro/macro/sample F1, precision@K, rare labels, hierarchy violations, calibration | Bibtex/EUR-Lex, Open Images subset, product taxonomy |
| **A3.23 Choose offers while learning from delayed user feedback** | Random policy; epsilon-greedy; UCB; Thompson sampling; linear/neural contextual bandits | Cumulative regret, exploration safety, delayed rewards, non-stationarity, logging bias, off-policy evaluation | Synthetic simulator, [Open Bandit Dataset](https://research.zozo.com/data.html) |
| **A3.24 Match or classify items using text, image, and audio together** | Early/late fusion; contrastive embeddings; cross-attention; multimodal retrieval; missing-modality fallback | Alignment leakage, modality ablation, missing/noisy inputs, retrieval metrics, calibration, compute cost | Flickr30k, VQA subset, AudioCaps, text/image catalog |
| **A3.25 Predict demand, hotspots, or land cover across space** | Spatial baselines; hotspot detection; spatial regression; routing; raster classification | Spatial/temporal holdouts, autocorrelation, CRS, boundary effects, resolution, geographic transfer, map uncertainty | NYC Taxi, OSM, SpaceNet, land-cover tiles |
| **A3.26 Train across clients without centralizing raw data** | Federated averaging; secure-aggregation simulation; differential privacy; local/on-device learning | Privacy budget, membership inference, utility loss, client imbalance/dropout, communication cost, stragglers | FEMNIST/LEAF, Adult, synthetic client partitions |
| **A3.27 Decide whether synthetic data is safe and useful enough to replace or augment real data** | Parametric simulation; resampling; GAN/VAE/diffusion or tabular synthesizers; constraint-based generation | Fidelity, downstream utility, rare-case coverage, memorization/privacy leakage, bias amplification, shift | Adult, Credit Card Fraud, time series, domain simulator |

#### A4. Language and Runtime Implementations

| Runtime scenario | Implement | Parity and performance constraints | Datasets |
|---|---|---|---|
| **A4.1 Train in Python and run the same model in native services and a browser** | Export ONNX; run with Python, C++, C#, Java, and JavaScript | Identical preprocessing/golden inputs; defined numeric tolerance; unsupported operators, malformed tensors, warm-up, p95 latency, memory | MNIST, Adult |
| **A4.2 Run tabular inference in Rust without a Python runtime** | Load and score a linear, tree, or k-NN model with typed schema, zero-copy data where useful, and optional SIMD | Match reference predictions; reject malformed models; test concurrency, allocation, startup, throughput, binary size | Adult, Fashion-MNIST features |
| **A4.3 Score a live fraud or click stream with bounded Go workers** | Event ingestion, online features, batching, scorer, bounded goroutine pipeline | Preserve documented ordering; handle duplicates, backpressure, cancellation, worker error, graceful shutdown, p95/p99 latency | Synthetic fraud stream, synthetic click stream |
| **A4.4 Reproduce Python features and scores entirely in SQL** | Point-in-time feature queries and linear/tree scoring in DuckDB or PostgreSQL | Match Python rows and predictions; handle nulls, types, time joins, duplicates, late data, query plans, memory | Bike Sharing, transaction data |
| **A4.5 Process a dataset too large for one machine process on the JVM** | Feature preparation and training with Java/Scala and Spark | Match local results; test partitioning, skew, serialization, retries, reproducibility, executor memory, scaling efficiency | NYC Taxi, HIGGS, generated large tables |
| **A4.6 Run a model privately and offline in a browser** | TypeScript plus ONNX Runtime Web using WASM/WebGPU; local preprocessing and model caching | Match server predictions; test supported browsers, offline reload, malformed input, memory, startup and inference latency | MNIST, small vision classifier, small audio classifier |
| **A4.7 Accelerate a CPU numerical bottleneck** | Matrix multiplication, convolution, softmax, or distance search in C/C++ with threading and optional SIMD | Match a high-precision reference; test shapes, alignment, cache behavior, thread scaling, numeric stability, regressions | Generated tensors |
| **A4.8 Accelerate the same operation on a GPU** | CUDA or Triton kernel with tiling, fused work where justified, and mixed precision | Match CPU/reference tolerance; test memory access, occupancy, warm-up, shape sensitivity, transfer cost, edge sizes | Generated matrices/tensors |
| **A4.9 Load one versioned model package in three languages** | Define a neutral schema for model, preprocessing, labels, metadata, and checksums; implement independent readers | Backward/forward compatibility, unknown fields, corruption, missing metadata, golden predictions, deterministic serialization | Linear model, decision tree, golden vectors |
| **A4.10 Reproduce a statistical model and service in R and Python** | Fit with tidymodels/mlr3; package in R; expose through Plumber; implement a Python reference | Match splits, preprocessing, coefficients/predictions within tolerance; test package restoration, invalid requests, startup, latency | Bank Marketing, survival data |

---

### B. Programming

Each row below is a complete problem. Its requirements, failure cases, constraints, and expected evidence are stated explicitly.

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

| ID and problem | Required implementation | Cases and constraints | Evidence and output |
|---|---|---|---|
| **B1.1 Store one million sessions** | Build hash tables using separate chaining and open addressing; support insert, lookup, update, delete, and resizing | Force collisions; test tombstones, duplicate keys, adversarial hashes, high load factors, and failed allocations | Session-store CLI/library, property tests against the standard map, collision/memory/latency comparison |
| **B1.2 Buffer the latest 100,000 events** | Build a dynamic array and circular deque with growth, shrinking, indexed access, and front/back operations | Exercise wraparound, empty/full transitions, capacity changes, invalid indexes, and allocation limits | Event-buffer program, invariant/property tests against standard collections, allocation/throughput benchmark |
| **B1.3 Evaluate expressions and support undo** | Use stacks for tokenization, operator precedence, nested expressions, command execution, undo, and redo | Reject invalid tokens and mismatched delimiters; limit nesting/history; handle failed commands without corrupting state | Interactive evaluator/editor, golden tests, generated expressions, comparison with a reference evaluator |
| **B1.4 Schedule one million delayed jobs** | Build binary min-heaps with insert, peek, remove, cancellation, and priority/deadline update | Handle equal deadlines, cancelled roots, past-due jobs, repeated updates, empty queues, and clock advancement | Scheduler simulator, heap-invariant tests, benchmark against sorted-list and library-heap implementations |
| **B1.5 Cache product metadata under a memory budget** | Implement LRU and LFU eviction using a hash table plus linked/frequency structures; support TTL | Handle updates, expiry races, oversized entries, zero capacity, concurrent access, and skewed workloads | Cache library, invariant tests, hit-rate simulations, LRU/LFU latency and memory comparison |
| **B1.6 Autocomplete products and match routes** | Build a trie with insertion, deletion, prefix search, ranked suggestions, and longest-prefix route matching | Handle Unicode normalization, duplicate terms, empty prefixes, deleted words, deep keys, and bounded result counts | Autocomplete/router API, correctness corpus, memory/latency comparison with sorted lists and hash maps |
| **B1.7 Filter previously visited URLs** | Build a Bloom filter with configurable capacity/error rate and double hashing | Insert beyond design capacity; test duplicate input, serialization, bit corruption, and incompatible parameters | Crawler prefilter, theoretical/observed false-positive report, proof of no false negatives for inserted keys |
| **B1.8 Sort a 20 GB log with 512 MB of memory** | Implement external merge sort with sorted runs, configurable buffers, temporary files, and k-way merge | Preserve duplicates; separate malformed timestamps; recover/clean up after interruption; never exceed the memory limit | Sorting CLI, ordering and record-conservation checks, resource measurements, run-size/fan-in benchmark |
| **B1.9 Find Top-K terms in a stream** | Implement full counting plus heap, quickselect on counts, and an approximate heavy-hitter algorithm | Test uniform, Zipfian, adversarial, empty, and changing streams; bound memory for the approximate method | Streaming CLI, exactness/error report, runtime/memory curves across K and stream size |
| **B1.10 Prevent overlapping reservations** | Implement sorted-interval scanning, merge/conflict detection, and an interval tree for repeated queries | Handle touching intervals, zero duration, containment, cancellation, timezone normalization, and concurrent proposals | Reservation checker, brute-force oracle tests, randomized interval corpus, query/update benchmark |
| **B1.11 Scan logs for thousands of signatures** | Implement naive matching, KMP, and Aho–Corasick with match positions and overlapping matches | Handle empty patterns, shared prefixes, Unicode/byte modes, chunk boundaries, long patterns, and duplicate signatures | Scanner CLI, shared match corpus, throughput/memory comparison across algorithms and pattern counts |
| **B1.12 Provide typo-tolerant search** | Implement Levenshtein distance with full and memory-reduced dynamic programming; reconstruct edits | Handle empty/Unicode strings, bounded distance, long inputs, transpositions as an optional extension, and early exit | Search API, brute-force/reference parity tests, edit scripts, time/memory comparison |
| **B1.13 Resolve build dependencies** | Implement DFS/BFS traversal, topological sorting, and explicit cycle-path reporting | Handle disconnected graphs, duplicate/self edges, missing nodes, multiple valid orders, and deterministic tie-breaking | Build-order CLI, generated DAG/cycle tests, correctness invariants, scaling benchmark |
| **B1.14 Route a courier through a road graph** | Implement Dijkstra and A* with path reconstruction and an admissible geographic heuristic | Handle unreachable nodes, multiple equal routes, zero-weight edges, blocked roads, stale queue entries, and large sparse graphs | Route planner, brute-force/small-graph oracle, expanded-node/runtime comparison, map visualization |
| **B1.15 Group linked accounts or devices** | Implement disjoint-set union with path compression and union by rank/size | Handle repeated/self links, incremental additions, unknown entities, large components, and deterministic representatives where required | Entity-resolution CLI, graph-traversal parity tests, amortized-performance experiment, component report |
| **B1.16 Assign workers to jobs** | Implement bipartite matching and a max-flow formulation with residual edges and augmenting paths | Enforce skills/capacities; handle impossible assignments, ties, duplicate edges, zero capacity, and changing availability | Assignment service, exhaustive oracle for small cases, capacity/matching invariants, scaling report |
| **B1.17 Search a local document collection** | Build an inverted index with tokenization, postings, Boolean intersection, TF-IDF/BM25 scoring, and snippets | Handle updates/deletes, repeated terms, stop words, empty/hostile queries, Unicode, and index persistence | Search CLI/API, judged-query set, ranking metrics, index-size/build/query benchmark |
| **B1.18 Index millions of ordered records on disk** | Implement a small B-tree/B+ tree or LSM-style index with range scans, pages/runs, splits or compaction | Recover from interrupted writes; test duplicate keys, partial pages/runs, checksums, large ranges, and bounded memory | Persistent index, format description, recovery/property tests, read/write-amplification benchmark against SQLite |
| **B1.19 Redistribute cache keys as servers change** | Implement consistent hashing with virtual nodes, weighted members, replication, and membership updates | Test node joins/leaves/failures, hash collisions, uneven weights, empty rings, replica overlap, and hot keys | Ring library/simulator, balance and key-movement report, comparison with modulo hashing |
| **B1.20 Query nearby map objects** | Implement a quadtree or simplified R-tree with insertion, range search, and nearest-neighbor queries | Handle boundary points, duplicate coordinates, clustered/uniform data, node overflow, deletions, and empty regions | Spatial-query service/visualization, brute-force oracle tests, memory/query scaling curves |
| **B1.21 Compress and recover logs exactly** | Implement Huffman coding or a simplified LZ-style compressor with bit packing and a versioned file header | Handle empty/single-symbol input, corrupt/truncated streams, invalid codes/back-references, large files, and incompressible data | Compressor CLI, round-trip/property tests, corruption corpus, compression-ratio/speed comparison with a standard tool |

##### Connected challenge sequences

These are optional progressions; every referenced problem remains independently specified above.

1. **Log and search system:** B1.1 hash table → B1.8 external sorting → B1.7 Bloom filter → B1.11 string matching → B1.17 inverted index → B1.21 compression.
2. **Job and resource scheduler:** B1.2 deque → B1.4 heap → B1.13 dependency graph → B1.10 interval conflicts → B1.16 matching → B1.18 persistent index.
3. **Distributed cache:** B1.5 local cache → B5.2 service caching → B1.19 consistent hashing → B5.6 distributed rate limiting → B5.11 tenant isolation.

##### Fully specified example: external merge sort

> Given a 20 GB log file and a 512 MB memory limit, produce a file ordered by timestamp. Implement external merge sort with configurable run size and merge fan-in. Preserve duplicate records and write malformed timestamps to a separate error file. Demonstrate that every valid input record appears exactly once, output timestamps are ordered, memory stays below the limit, and temporary files are removed after success or failure.

#### B2. Core Components From Scratch

| ID and problem | Required behavior | Failures and constraints | Evidence and output |
|---|---|---|---|
| **B2.1 Parser and interpreter** | Parse and execute a small configuration or rules language with variables, expressions, conditions, and functions | Reject invalid syntax; report line/column errors; cap recursion, memory, and execution time | Grammar, parser/evaluator, conformance tests, fuzz tests, comparison with a parser library |
| **B2.2 Serialization format** | Encode/decode typed records, optional fields, collections, and schema versions | Detect truncation, invalid lengths/types, unknown fields, incompatible versions, and oversized input | Format specification, two independent readers, round-trip/property tests, size/speed benchmark |
| **B2.3 HTTP server** | Serve routes, headers, query parameters, request bodies, middleware, keep-alive, and graceful shutdown using low-level networking | Enforce body/header/time limits; handle malformed requests, disconnects, slow clients, and connection exhaustion | Server, protocol tests, load test, packet/trace analysis, comparison with a standard server |
| **B2.4 Thread pool** | Execute submitted tasks with bounded queueing, futures/results, cancellation, priorities, and orderly shutdown | Handle task exceptions, queue saturation, worker loss, cancellation races, and submissions during shutdown | Library, deterministic concurrency tests, stress test, throughput/latency comparison |
| **B2.5 Persistent task scheduler** | Run delayed and recurring jobs with persistence, retries, cancellation, and missed-run policy | Recover after process crash; prevent duplicate execution where promised; handle clock changes and long-running jobs | Scheduler, durable store, fake-clock tests, crash/restart demonstration, operations CLI |
| **B2.6 Embedded key-value store** | Support put/get/delete, persistence, indexing, atomic batches, and compaction | Recover from interrupted writes, checksum failures, partial records, large values, and concurrent readers | Store library, on-disk format, recovery/property tests, benchmark against SQLite or another embedded store |
| **B2.7 Dependency-injection container** | Register constructors and values; resolve dependencies; support singleton/request/transient scopes and cleanup | Detect cycles, missing/duplicate bindings, constructor failure, and invalid scope use | Container, dependency-graph visualization, lifecycle tests, comparison with a mature DI library |
| **B2.8 Template engine** | Render escaped variables, conditions, loops, includes, filters, and reusable templates | Reject malformed templates; prevent unsafe evaluation, path traversal, recursive includes, and unbounded output | Engine, syntax reference, golden tests, fuzz tests, comparison with an established engine |

#### B3. Language and Framework Laboratories

| ID and problem | Required behavior | Failures and constraints | Evidence and output |
|---|---|---|---|
| **B3.1 REST API frameworks** | Implement the same inventory API in FastAPI, ASP.NET Core, Go, and Node.js with products, stock, atomic reservations, pagination, and migrations | Reject invalid quantities; handle duplicate requests, simultaneous reservations, stale updates, and database restarts | Four services, shared contract/integration suite, throughput/tail-latency/memory/deployment-size comparison |
| **B3.2 CLI ecosystems** | Build the same streaming CSV/JSON validation and conversion CLI in Python, Rust, and Go with subcommands, pipes, progress, and exit codes | Handle malformed rows, broken pipes, encoding errors, files larger than memory, and interrupted output | Installable CLIs, shared golden tests, startup/runtime/memory/binary-size comparison |
| **B3.3 Database-access approaches** | Implement the same transactional order repository with SQLAlchemy, Django ORM, Entity Framework, and raw SQL | Handle rollback, concurrent updates, N+1 queries, nullable data, migration failure, and connection loss | Repository implementations, shared integration tests, generated-SQL review, performance/complexity comparison |
| **B3.4 Concurrency models** | Process the same CPU- and I/O-mixed media workload using threads, async, processes, goroutines, and a distributed queue | Bound concurrency and memory; handle cancellation, worker failure, backpressure, timeouts, and task duplication | Implementations, correctness suite, saturation curves, profiler evidence, model-selection report |
| **B3.5 Testing ecosystems** | Test the same validation and calculation library with example-based, property-based, mutation, and fuzz testing | Include malformed input, numeric boundaries, invariants, timeouts, and nondeterministic failures | Test suites, seeded failure corpus, mutation scores, defect-detection/time-cost comparison |
| **B3.6 Package ecosystems** | Publish the same validation library as a Python package, Rust crate, npm package, and NuGet package with equivalent public behavior | Handle dependency/version conflicts, unsupported runtimes, deprecations, and a deliberately breaking change | Packages, generated docs, compatibility CI, semantic-versioning exercise, consumer examples |
| **B3.7 API protocols** | Expose the same order-query capability through REST/JSON, gRPC/Protobuf, and GraphQL | Handle schema evolution, invalid requests, pagination, partial fields, deadlines, large responses, and client cancellation | Services/clients, contract tests, payload/latency comparison, compatibility report |
| **B3.8 Web application approaches** | Build the same accessible issue tracker using server rendering, a SPA, and progressive enhancement | Support loading/error/empty states, validation, refresh, slow networks, disabled JavaScript where promised, and keyboard use | Three implementations, end-to-end/accessibility tests, bundle/startup/runtime comparison |

#### B4. Application Problem Families

| ID and problem | Required behavior | Failures and constraints | Evidence and output |
|---|---|---|---|
| **B4.1 Authentication service** | Registration, verified contact, login, logout, password reset, session listing/revocation, token rotation, and audit history | Prevent credential enumeration, session fixation, replay, brute force, token leakage, and unsafe password storage | Service and client, threat model, security/integration tests, session-revocation demonstration |
| **B4.2 Authorization system** | Enforce ownership plus RBAC or ABAC across users, administrators, resources, and tenants | Deny IDOR, privilege escalation, cross-tenant access, stale permissions, and client-side-only checks | Policy model, authorization middleware, allow/deny matrix, adversarial integration tests, audit events |
| **B4.3 Background-job system** | Submit work, report progress, retry transient failure, cancel jobs, schedule execution, and inspect dead letters | Guarantee documented at-least/at-most-once behavior; handle duplicate delivery, poison jobs, worker crash, and queue saturation | API, workers, operations view, idempotency tests, crash/recovery and load demonstrations |
| **B4.4 Webhook consumer** | Verify signatures, persist events, process idempotently, replay failures, and reconcile remote/local state | Handle duplicates, missing events, reordering, delayed delivery, secret rotation, invalid signatures, and handler crashes | Receiver, durable inbox, replay/reconciliation tools, event-history UI, failure tests |
| **B4.5 External API synchronization** | Incrementally copy and map records from a paginated, rate-limited API into a local database | Resume partial runs; handle updates/deletes, schema changes, expiring credentials, throttling, and inconsistent pages | Sync service, checkpoints, reconciliation report, mock failure server, repeatability tests |
| **B4.6 File-processing service** | Upload, validate, scan, transform, track progress, download results, and clean expired files | Reject path traversal, MIME spoofing, oversized/decompression-bomb input, duplicate names, corruption, and worker failure | API/UI, isolated processor, quarantine path, malicious-file test corpus, cleanup demonstration |
| **B4.7 Real-time notifications** | Deliver authenticated WebSocket/SSE messages with subscriptions, persistence, acknowledgement, and reconnect recovery | Bound slow consumers; handle disconnects, missed/duplicate events, fan-out spikes, revoked access, and server restart | Gateway/client, replay behavior, load test, delivery metrics, reconnect tests |
| **B4.8 Order and payment workflow** | Reserve inventory; authorize/capture payment; fulfill, cancel, refund, and expose audit history using a sandbox provider | Prevent double charge and overselling; recover from timeouts, duplicate webhooks, partial failure, and invalid transitions | Explicit state machine, service, concurrency tests, reconciliation tool, recovery demonstration |
| **B4.9 Search service** | Ingest/update/delete documents; search with fields, filters, highlighting, typo handling, ranking, and pagination | Handle empty/hostile queries, stale updates, duplicate documents, index failure, and reindexing without corrupting live search | Search API, relevance judgments, NDCG/latency tests, zero-result analysis, reindex procedure |
| **B4.10 Collaborative application** | Support shared documents, presence, concurrent edits, history, and reconnect from multiple clients | Resolve or expose conflicts; handle offline edits, missed operations, duplicate messages, slow clients, and permission changes | Multi-client app, convergence tests, network-fault simulation, history/recovery demonstration |
| **B4.11 Booking system** | Expose availability, place expiring holds, confirm/cancel bookings, manage capacity, and operate a waitlist | Prevent double booking; handle concurrent holds, payment timeout, expiry races, timezone changes, and cancellation | Service/UI, transactional model, fake-clock and concurrency tests, audit history |
| **B4.12 Import/export system** | Map external schemas, validate records, preview changes, execute resumably, and produce success/error reports | Handle duplicate identifiers, invalid references, encoding/schema changes, partial failure, retries, and very large files | Import/export tools, mapping specification, resumability tests, reconciliation report |

#### B5. Architecture and Distributed-System Problems

| ID and problem | Required behavior | Failures and constraints | Evidence and output |
|---|---|---|---|
| **B5.1 Plugin architecture** | Discover, install, configure, enable/disable, version, and unload third-party extensions through a stable API | Isolate failures; enforce permissions/quotas; handle incompatible versions, dependency conflicts, and malicious plugins | Host, SDK, sample/malicious plugins, compatibility tests, lifecycle and permission demonstrations |
| **B5.2 Caching layer** | Add cache-aside reads and invalidation to a read-heavy catalog while preserving a documented consistency model | Handle misses, stale values, stampedes, eviction, cache outage, key collisions, and write races | Implementation, hit/staleness metrics, failure tests, load/cost comparison with and without cache |
| **B5.3 Message-queue workflow** | Deliver jobs through RabbitMQ, Kafka, and Redis Streams with acknowledgements, retries, priorities where supported, and dead letters | Document ordering/delivery guarantees; handle duplicates, poison messages, consumer crash, partitions, and backlog growth | Producers/consumers, shared scenario suite, recovery/throughput comparison, operations dashboard |
| **B5.4 API gateway** | Route multiple services with authentication, request IDs, quotas, rate limits, transformations, and upstream health | Handle slow/down upstreams, retry amplification, oversized requests, configuration errors, and partial gateway failure | Gateway config/code, synthetic upstreams, security/load/failure tests, route and latency dashboard |
| **B5.5 Event-driven application** | Maintain order or inventory projections from versioned events with idempotent handlers and replay | Handle duplicates, reordering, missing events, incompatible schemas, handler crashes, poison events, and projection rebuild | Event schemas, handlers, durable log, replay tool, invariant/property tests, audit view |
| **B5.6 Distributed rate limiter** | Implement token-bucket and sliding-window limits per user, tenant, and endpoint across multiple instances | Bound clock skew, races, hot keys, store outage, burst behavior, and memory growth | Limiter service/library, reference model, concurrency/property tests, accuracy/latency benchmark |
| **B5.7 Circuit breaker and bulkhead** | Protect a service from a slow/flaky dependency using timeouts, bounded retries, breakers, concurrency limits, and fallback | Prevent retry storms; handle half-open races, dependency flapping, queue buildup, and false recovery | Resilience library/config, fault-injecting dependency, state-transition tests, impact report |
| **B5.8 Distributed lock** | Ensure one instance performs a scheduled job using leases, ownership tokens, renewal, and fencing | Handle process pause/crash, expired leases, delayed messages, clock issues, store failover, and stale owners | Lock implementation, adversarial timeline tests, duplicate-execution analysis, documented safety limits |
| **B5.9 Transactional outbox** | Commit domain changes and outbound events atomically without a distributed transaction; publish and mark events | Handle publisher crash before/after send, duplicate delivery, backlog, database failover, and event-schema change | Schema, relay, idempotent consumer, crash-point tests, lag dashboard, replay tool |
| **B5.10 Saga workflow** | Coordinate a multi-service booking or order through local transactions and explicit compensations | Handle step timeout, duplicate command, failed compensation, irrecoverable state, and operator intervention | Orchestrated/choreographed implementation, state diagram, failure matrix, recovery console |
| **B5.11 Multi-tenant system** | Isolate tenant data, caches, jobs, rate limits, configuration, and audit logs while supporting tenant administration | Prevent cross-tenant identifiers/queries, cache-key leaks, noisy neighbors, incorrect background context, and export leakage | Service, isolation test suite, per-tenant metrics/quotas, adversarial tenant tests |
| **B5.12 Service discovery and load balancing** | Register instances, renew leases, health-check endpoints, route traffic, and remove unhealthy nodes | Handle stale registrations, flapping health, uneven load, slow nodes, registry outage, and rolling deployments | Registry/balancer, simulated instances, distribution/failover tests, routing dashboard |

#### B6. Security and Trust-Boundary Problems

| ID and problem | Required behavior | Failures and constraints | Evidence and output |
|---|---|---|---|
| **B6.1 Secure file upload** | Accept permitted files, rename safely, validate content, scan, isolate processing, and expire stored objects | Block traversal, MIME spoofing, executable content, archive bombs, oversized files, collisions, and malicious metadata | Upload service, threat model, hostile corpus, security tests, quarantine/cleanup demonstration |
| **B6.2 Authorization audit** | Review and correct a deliberately vulnerable multi-user API with ownership, roles, and tenant boundaries | Find IDOR, privilege escalation, mass assignment, missing server checks, confused-deputy paths, and cross-tenant access | Findings report, exploit tests, fixes, regression suite, before/after authorization matrix |
| **B6.3 Untrusted plugin sandbox** | Run user extensions with declared capabilities, CPU/memory/time quotas, isolated storage, and revocable permissions | Prevent unrestricted file/network/process access, resource exhaustion, host escape, and package tampering | Sandbox, permission manifest, malicious plugins, escape/resource tests, audit log |
| **B6.4 Secret-handling library** | Load secrets through approved providers, redact values, rotate credentials, expire caches, and expose audit metadata | Prevent source/image/log/error leakage, unsafe fallback, stale values, broad permissions, and accidental serialization | Library, redaction/property tests, rotation demo, leak-scanning corpus, integration examples |
| **B6.5 Signed-request protocol** | Canonicalize and sign method/path/body/time/nonce; verify requests; rotate keys | Reject replay, altered bodies, clock-skew abuse, canonicalization differences, unknown keys, and downgrade attempts | Protocol specification, client/server in two languages, adversarial test vectors, rotation demonstration |
| **B6.6 Abuse-resistant public API** | Enforce quotas, adaptive rate limits, pagination bounds, cost limits, and safe error responses | Resist credential stuffing, enumeration, scraping, quota evasion, expensive queries, and distributed bursts | API, abuse simulator, detection/limit metrics, false-positive analysis, incident playbook |
| **B6.7 Secure parser** | Parse an untrusted structured format with bounded input, nesting, allocations, and processing time | Handle malformed lengths, integer overflow, deep nesting, decompression bombs, ambiguous encodings, and fuzz-generated cases | Parser, threat model, fuzz harness/corpus, resource-bound tests, vulnerability report |
| **B6.8 Tamper-evident audit log** | Record actor, action, target, result, time, and correlation data with access controls and integrity verification | Detect deletion/reordering/modification; redact sensitive fields; handle clock disorder, high volume, and retention expiry | Append-only log, verification tool, tampering tests, query interface, retention demonstration |

#### B7. Maintenance, Quality, and Performance Problems

| ID and problem | Required behavior | Failures and constraints | Evidence and output |
|---|---|---|---|
| **B7.1 Legacy characterization** | Discover and document the behavior of an untested application before changing one critical workflow | Preserve external behavior unless explicitly corrected; capture hidden file/database/time dependencies and nondeterminism | Characterization suite, dependency map, behavior report, safely implemented change |
| **B7.2 Framework migration** | Move an application across a major framework/runtime version while preserving API, data, and deployment behavior | Handle removed APIs, changed defaults, dependency conflicts, configuration differences, and rollback | Migration commits, compatibility tests, deprecation inventory, before/after deployment evidence |
| **B7.3 Database migration** | Change a large live-style schema using expand/migrate/contract steps compatible with old and new application versions | Avoid long locks and data loss; handle partial backfill, invalid legacy rows, restart, and rollback | Migration/backfill tools, compatibility tests, timing/lock report, rollback rehearsal |
| **B7.4 API versioning** | Introduce a breaking resource-model change while serving old and new clients through a defined retirement period | Handle mixed versions, stored old payloads, incompatible validation, client retries, and rollback | Versioned API/clients, contract tests, migration guide, usage telemetry, removal plan |
| **B7.5 Performance diagnosis** | Reproduce a slow endpoint or batch job, profile it, identify the bottleneck, and implement a measured improvement | Preserve correctness; test cold/warm state, realistic data, contention, downstream limits, and regression risk | Reproducible benchmark, profiles/traces, fix, before/after latency/resource results |
| **B7.6 Memory-leak investigation** | Reproduce increasing memory use, identify retained objects/resources, fix the cause, and prevent recurrence | Distinguish leak from cache/fragmentation; test long runs, cancellation, errors, and concurrency | Minimal reproducer, heap/allocation evidence, fix, soak test, memory regression gate |
| **B7.7 Concurrency-bug investigation** | Reproduce and fix a race, deadlock, starvation, lost update, or ordering bug | Make failure repeatable with controlled scheduling/load; avoid replacing it with global serialization without analysis | Reproducer, timeline, correctness invariant, fix, stress/model-based regression tests |
| **B7.8 Dependency replacement** | Replace an abandoned or unsafe dependency while preserving public behavior and stored data | Handle semantic differences, transitive dependencies, performance changes, unsupported formats, and rollback | Compatibility adapter, contract suite, migration notes, benchmark, dependency removal evidence |
| **B7.9 Test-strategy retrofit** | Add useful tests to an untested application, prioritizing high-risk behavior and seams for change | Avoid tests coupled only to internals or snapshots; address nondeterminism, external services, and slow fixtures | Risk map, test pyramid, fixtures/fakes, coverage-by-behavior report, demonstrated caught defects |
| **B7.10 Fault-injection exercise** | Inject dependency latency/errors, process crashes, disk exhaustion, and partial network failure into a service | Keep experiments bounded; verify detection, graceful degradation, recovery, data integrity, and cleanup | Fault harness, runbook, timelines/metrics, discovered weaknesses, repeated post-fix results |
| **B7.11 Compatibility challenge** | Support declared operating systems, CPU architectures, database versions, or client versions from one codebase | Handle path/encoding/time differences, endianness, unavailable features, packaging, and upgrade order | Compatibility matrix, CI jobs, portable artifacts, failure notes, supported-version policy |
| **B7.12 Modular-monolith extraction** | Separate one domain behind an internal boundary while retaining a single deployment and clear transaction ownership | Prevent cyclic dependencies, shared-table leakage, duplicate rules, accidental network coupling, and migration dead ends | Module API, dependency tests, schema ownership map, incremental refactor, complexity comparison |

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

These programs connect many independently useful parts into larger systems. A developer may build one component, connect several components, deepen a particular capability, or expand the whole program over time. The categories describe the role of a program; they are not difficulty rankings or mandatory sequences.

### Purpose and Ways to Use the Programs

- Start with a domain, capability, platform component, or scale question that has suitable data and genuine interest.
- Complete individual parts when they are useful learning units.
- Connect parts when the connection reveals assumptions, interfaces, failure modes, or operational tradeoffs.
- Reuse a component in another program when doing so tests whether it is genuinely general.
- Add distribution or scale to answer a measured constraint or a deliberate systems question.
- Revisit scope and remove complexity that no longer serves the program.

### Rough Maturity Guide

These stages are orientation points, not completion requirements. Programs may skip stages, remain at one stage, or advance unevenly across components.

| Rough stage | Typical state |
|---|---|
| **Exploration** | The problem, available data, users, and plausible approaches are being investigated |
| **Working core** | One important workflow works from beginning to end |
| **Connected system** | Several components exchange data and support a broader workflow |
| **Operational system** | Recurring execution, failures, observability, security, and recovery receive attention |
| **Expanded system** | The program supports more domains, users, data, automation, or scale |

A program may have an operational ingestion pipeline, an exploratory model, a basic interface, and an advanced search component at the same time. Maturity is a profile, not a single level.

### Project Compass

These prompts can help plan work and assess progress. They are optional lenses rather than a required specification.

| Lens | Questions to consider |
|---|---|
| **Purpose** | What broad problem is addressed? Who might use the result? What decision, action, or workflow could improve? |
| **Current scope** | Which part is being attempted now? What is deliberately excluded? Which component can stand alone? What is the smallest useful connection? |
| **Data reality** | What data is available? Is it real, collected, simulated, or generated? Is it sufficiently varied, fresh, reliable, and legally usable? |
| **System shape** | What are the inputs, transformations, stored states, interfaces, and actions? Where should human review or approval occur? |
| **Progress** | What works? What remains manual, unreliable, unverified, or difficult to reproduce? Which missing connection would add the most value? |
| **Shortcomings** | Where can incorrect data enter? Which results are hard to verify? What can fail silently? Which assumptions are weakest? |
| **Risks** | What privacy, security, licensing, cost, misuse, or misleading-output risks exist? |
| **Possible directions** | Improve the core result, add data, connect a component, strengthen evaluation, automate work, improve operations, generalize, scale, or simplify |

### Data and Scale Modes

| Data mode | Best use |
|---|---|
| **Real public data** | Domain behavior, relevance, correctness, and genuine irregularities |
| **Collected data** | Recurring workflows, freshness, change tracking, and source failures |
| **Simulation** | Feedback loops, users, agents, rare events, and controlled experiments |
| **Generated volume** | Throughput, storage, partitioning, and recovery |
| **Replayed events** | Streaming behavior, ordering, retries, and operational testing |

Keep two meanings of scale separate:

- **Semantic scale:** enough genuine diversity and interaction to support meaningful conclusions.
- **Systems scale:** enough bytes, events, requests, or partitions to test architecture.

Generated volume can test partitioning and recovery, but it does not automatically create meaningful model, search, or recommendation evaluation.

### Open-Ended Progress Measures

Each program can define a broad problem, one or two initial value measures, and optional supporting measures. These indicate direction rather than form a universal grading system.

| Dimension | Possible measures |
|---|---|
| **Usefulness** | Time saved, useful findings, successful workflows, accepted recommendations, completed decisions |
| **Data** | Coverage, freshness, duplicates, invalid records, schema failures, reproducibility, lineage |
| **Analytical quality** | Precision, recall, ranking quality, calibration, forecast error, uncertainty coverage |
| **Operations** | Availability, recovery time, failed-job rate, throughput, p95 latency, backlog |
| **Trust** | Supported claims, false alerts, audit coverage, human correction, permission violations |
| **Efficiency** | Cost per entity, document, query, prediction, event, or completed workflow |

Avoid collapsing every measure into one score. Improvement is usually multi-objective: one dimension should not improve by quietly violating important constraints in another.

---

### A. Domain Programs

Domain programs provide the users, data, workflows, and reasons for connecting technical components.

| Program | Main problem | Possible parts | Example progress signals |
|---|---|---|---|
| **Marketing Intelligence Platform** | Turn changing market information into timely, trustworthy research, statistics, reports, and alerts | Scraping/APIs, source versioning, entity resolution, NLP, search, statistics, reports, alerts, agents, API/UI | Entity/source coverage, freshness, change-detection quality, alert precision, supported claims, report time/cost |
| **GIS/Open-Data Intelligence Platform** | Integrate spatial and public data to support geographic search, monitoring, analysis, and decisions | Spatial ETL, validation, geocoding, PostGIS/DuckDB Spatial, tiles, search, change detection, forecasting, maps | Geographic/attribute coverage, geometry validity, freshness, spatial correctness, query latency, analyst task time |
| **Document Intelligence Platform** | Turn documents into validated, searchable, structured, and actionable information | Upload, OCR, layout analysis, extraction, validation, review queues, search, workflow, audit | Field accuracy, CER/WER, review rate, document throughput, retrieval quality, unsupported extraction rate |
| **Learning and Practice Platform** | Turn learning material into trustworthy practice and adapt future study using review results | PDF/EPUB/HTML ingestion, OCR, concept extraction, flashcards, cloze and language exercises, evidence checks, review, scheduling, Anki export | Card acceptance/edit rate, source support, duplicate/ambiguity rate, time per accepted card, retention, review burden |
| **Game or Simulated-World Platform** | Create a controllable data-generating environment containing users, agents, events, economies, and decisions | Simulation/game loop, agents, events, marketplace, matchmaking, inventories, telemetry, search, recommendation, abuse detection | Simulation invariants, agent performance, economy stability, discovery quality, fairness, latency, resource use |

#### Marketing Intelligence as a Component Ecosystem

One possible shape is:

```text
Sources
  → scraping and API connectors
  → raw storage and versioning
  → parsing and entity resolution
  → historical data model
  → statistics and machine learning
  → search and retrieval
  → reports and alerts
  → agentic research
  → API and user interface
  → monitoring and recovery
```

This is a map of possible relationships, not a required architecture. Work may focus on one component, one useful vertical slice, or the connections among several components.

#### Learning and Practice as a Component Ecosystem

The central loop is to convert source material into verifiable practice, collect review evidence, and use that evidence to improve later practice.

```text
PDF, EPUB, HTML, notes, image, audio, or transcript
  → text, layout, and media extraction
  → sections, concepts, examples, and prerequisites
  → flashcards, cloze questions, and exercises
  → source-support, ambiguity, and duplicate checks
  → human review
  → Anki export or built-in practice
  → review history and learner feedback
  → improved scheduling, selection, and generation
```

The program can emphasize either or both of these modes:

- **Knowledge study:** definitions, explanations, formulas, diagrams, comparisons, prerequisites, chapter questions, and image occlusion.
- **Language learning:** vocabulary in context, sentence cloze, grammar transformations, translation, listening, pronunciation, minimal pairs, and exercises based on recurring errors.

| Component | Possible responsibilities |
|---|---|
| **Content ingestion** | Import PDF, EPUB, HTML, Markdown, images, audio, transcripts, and metadata while retaining source locations |
| **Document processing** | Recover OCR text, layout, reading order, headings, tables, formulas, diagrams, and media |
| **Concept organization** | Identify terms, definitions, relationships, examples, sections, and possible prerequisites |
| **Practice generation** | Produce Q&A, cloze, definition, formula, image, listening, pronunciation, and transformation exercises |
| **Verification** | Check source support, answerability, ambiguity, contradictions, duplicate meaning, and leakage from question to answer |
| **Human review** | Accept, edit, reject, merge, split, tag, and trace an item back to its source |
| **Practice and scheduling** | Run sessions, grade answers, schedule reviews, provide hints, and retain learning history |
| **Integration** | Begin with CSV/TSV export; later add richer Anki packages, media, synchronization, or a built-in client |
| **Adaptation and analytics** | Track weak concepts, recurring language errors, difficulty, retention, review load, and generation quality |

Possible progress signals include:

| Dimension | Examples |
|---|---|
| **Generation quality** | Acceptance/edit rate, unsupported-answer rate, duplicate rate, ambiguity rate, source-reference accuracy, concept coverage |
| **Learning usefulness** | Time per accepted item, delayed recall, repeated-error rate, difficulty calibration, weak-concept improvement, review burden |
| **Language practice** | Vocabulary coverage, accepted-answer coverage, cloze ambiguity, grammar-error recurrence, listening/pronunciation performance |
| **Operations** | Extraction success by format, OCR/layout quality, processing time/cost, recovery from failed documents, export reliability |

Important limitations are also useful areas of study: a grammatical card may be educationally poor; a cloze may have several valid answers; a short passage may lack context; formulas and diagrams may be extracted incorrectly; excessive cards may increase review burden; and copyrighted, DRM-protected, or personal material may require restricted or local processing.

Document Intelligence can supply ingestion and extraction capabilities, while the Learning and Practice Platform adds an end-user feedback loop through review, correction, scheduling, and measured learning outcomes.

#### Feasible Data Starting Points

- Marketing or media intelligence can use regularly updated sources such as [GDELT](https://www.gdeltproject.org/data.html?source=post_page---------------------------), subject to source quality and licensing checks.
- GIS work can begin with regional [OpenStreetMap extracts](https://wiki.openstreetmap.org/wiki/Extracts) rather than planet-scale processing.
- Learning work can begin with owned, licensed, or public-domain PDFs and EPUBs, personal notes, open course material, subtitles, and transcripts; preserve page/section references and avoid bypassing DRM.
- A game, marketplace, logistics simulation, or agent tournament can generate controlled events, interactions, graphs, transactions, and rare cases.

---

### B. Capability Systems

These can be standalone studies, but often become more meaningful when attached to a domain program.

| Capability | Main question | Possible host programs | Example progress signals |
|---|---|---|---|
| **Search and retrieval** | Can the system return the most useful available information while keeping the index fresh and responsive? | Marketing, documents, GIS, research, games | Recall/MRR/NDCG, zero-result rate, freshness, latency, indexing throughput, cost |
| **Recommendation and ranking** | Can the system rank useful items for a user or context while maintaining coverage and freshness? | Products, content, locations, research sources, game items | Recall/NDCG, coverage, diversity, novelty, cold-start quality, freshness, latency |
| **Alerting and workflow automation** | Can meaningful changes trigger timely action without overwhelming users? | Marketing, GIS, simulated equipment, marketplaces, infrastructure | Detection delay, alert precision, missed-event rate, acknowledgement time, automation success |
| **Agentic research and analysis** | Can bounded research or analysis tasks be completed correctly, reproducibly, and with appropriate human involvement? | Marketing, GIS, documents, data exploration | Task completion, supported claims, calculation correctness, intervention rate, recovery, cost/latency |
| **OCR and information extraction** | Can unstructured documents become trustworthy structured records? | Documents, finance, public records, maps | Recognition/field accuracy, review rate, throughput, confidence calibration, schema validity |
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
