# Engineering Practice Roadmap

> A structured collection of short engineering challenges and larger systems projects for building production-oriented capability.

## Contents

- [Philosophy](#philosophy)
- [Group 1: Engineering Challenges](#group-1-engineering-challenges)
  - [A. Data Science and Machine Learning](#a-data-science--machine-learning)
  - [B. Programming](#b-programming)
  - [C. Infrastructure](#c-infrastructure)
  - [D. Mathematics](#d-mathematics)
- [Group 2: Systems Projects](#group-2-systems-projects)
- [What Makes These Valuable?](#what-makes-these-valuable)

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

> **For every challenge:** record the dataset version and license, keep an untouched test set, measure runtime and memory, and test corrupted or shifted data.

#### A1. Foundational Algorithms: Rebuild, Verify, Compare

Build the smallest correct version; use mature libraries as the benchmark.

| ID and challenge | Build | Verify and compare | Data → output |
|---|---|---|---|
| **A1.1 Linear/logistic regression** | OLS via normal equation and QR/SVD; gradient descent; logistic loss; L1/L2 | Gradient checks; collinearity, scaling, outliers, separation; compare scikit-learn and statsmodels | [California Housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html), [Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset), [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) → model file, coefficient report, API/CLI |
| **A1.2 Decision trees** | CART splits; classification/regression loss; stopping; pruning; missing/categorical values | Hand-check splits; test constant/repeated features and depth; compare scikit-learn | [Adult](https://archive.ics.uci.edu/dataset/2/adult), [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality), XOR → inspectable tree, pruning study, visualization |
| **A1.3 Random forests** | Bootstrap samples; feature subsampling; OOB score; parallel trees; permutation importance | Measure variance, OOB/test agreement, seeding, correlated features; compare `RandomForest` and `ExtraTrees` | [Covertype](https://archive.ics.uci.edu/dataset/31/covertype), Adult, synthetic nonlinear data → trainer, scaling plot, OOB diagnostics |
| **A1.4 Gradient boosting** | Residual trees; learning rate; subsampling; early stopping; regression and logistic loss | Track stage loss and overfitting; compare scikit-learn, XGBoost, LightGBM, CatBoost concepts | [HIGGS](https://archive.ics.uci.edu/dataset/280/higgs), Adult, California Housing → training curves and benchmark matrix |
| **A1.5 k-NN and neighbor search** | Brute-force k-NN; distance metrics; weighting; KD-tree or ball-tree | Test ties, dimensions, latency, memory; compare scikit-learn, SciPy, FAISS/HNSW | [Wine](https://archive.ics.uci.edu/dataset/109/wine), [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist), synthetic vectors → recall/latency curves |
| **A1.6 Naive Bayes** | Gaussian, multinomial, Bernoulli; smoothing; log likelihoods; TF-IDF | Test zero counts, underflow, unknown terms, calibration; compare logistic regression | [20 Newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html), [IMDb](https://ai.stanford.edu/~amaas/data/sentiment/) → vectorizer, error analysis, size/latency report |
| **A1.7 k-Means and GMMs** | k-means++; Lloyd's algorithm; empty-cluster recovery; EM; soft assignment | Test initialization, scaling, cluster shapes and covariance failure; compare scikit-learn | [Wholesale Customers](https://archive.ics.uci.edu/dataset/292/wholesale+customers), Wine, synthetic clusters → stability study and cluster profiles |
| **A1.8 MLP and backpropagation** | Dense layers; activations; cross-entropy; backprop; SGD/Adam; dropout; checkpoints | Gradient checks; tiny-batch overfit; gradient stability; compare PyTorch, JAX, or TensorFlow | [MNIST](https://www.openml.org/d/554), Fashion-MNIST, synthetic 2-D data → training engine, profiler report, endpoint |
| **A1.9 Support vector machines** | Linear hinge-loss solver; soft margin; kernels; simplified SMO | Check KKT conditions, margins, scaling, support-vector count; compare `LinearSVC` and `SVC` | Synthetic margins, [Wine](https://archive.ics.uci.edu/dataset/109/wine), Fashion-MNIST subset → solver, boundary plots, quality/speed report |
| **A1.10 Hidden Markov models** | Forward/backward; Viterbi; Baum–Welch; log-space probabilities | Check likelihood monotonicity, decoding, missing observations; compare hmmlearn/pomegranate | Synthetic state sequences, [UCI HAR](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones), speech/activity sequences → decoder and diagnostics |
| **A1.11 Factorization machines** | Matrix factorization; pairwise interactions; SGD/ALS; implicit feedback | Check sparse updates, regularization, ranking, cold start; compare implicit/LightFM | [MovieLens](https://grouplens.org/datasets/movielens/), [Amazon Reviews](https://amazon-reviews-2023.github.io/) → recommender benchmark and serialized model |

#### A2. Specialized Library Laboratories

Use identical splits, preprocessing, metrics, and compute budgets.

| ID and lab | Compare | Test | Data → output |
|---|---|---|---|
| **A2.1 Gradient boosting** | XGBoost, LightGBM, CatBoost | Categoricals, missing/sparse data, constraints, calibration, CPU/GPU, export, latency | Adult, HIGGS, California Housing, synthetic categoricals → quality/speed/memory decision matrix |
| **A2.2 HPO and AutoML** | Random search, successive halving, Optuna/Ray Tune; AutoGluon, FLAML, or H2O | Search spaces, pruning, nested validation, resumption, reproducibility, fixed budgets | Adult, Bank Marketing, Covertype → accuracy/compute frontier and reproducible pipeline |
| **A2.3 Imbalanced learning** | Under/oversampling, SMOTE, balanced ensembles, class weights, focal loss | Resample inside CV; calibration; thresholding; precision at capacity | [Credit Card Fraud](https://www.openml.org/d/1597), [Mammography](https://www.openml.org/d/310), synthetic rare events → leakage demo and threshold policy |
| **A2.4 Time series** | statsmodels/StatsForecast, Prophet, MLForecast/sktime, Darts/NeuralForecast | Missing intervals, exogenous features, hierarchies, intervals, rolling backtests, cold start | [M4](https://github.com/Mcompetitions/M4-methods/tree/master/Dataset), [Electricity Load](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014), intermittent demand → backtest and planning report |
| **A2.5 Computer vision** | OpenCV, torchvision/KerasCV, timm, Albumentations, YOLO | Transfer learning, augmentation, NMS, mixed precision, export, edge latency | [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html), [Oxford Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/), [COCO](https://cocodataset.org/) subset → error gallery and inference service |
| **A2.6 NLP and embeddings** | spaCy, Transformers, Sentence Transformers, TF-IDF | Tokenization, truncation, batching, domain/language shift, quantization, calibration | 20 Newsgroups, IMDb, [AG News](https://huggingface.co/datasets/fancyzhx/ag_news), domain corpus → quality/latency/cost frontier |
| **A2.7 OCR and document AI** | Tesseract, PaddleOCR, EasyOCR, docTR or cloud OCR | Orientation, layout, tables, handwriting, languages, confidence, throughput | [IAM](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database), [FUNSD](https://guillaumejaume.github.io/FUNSD/), corrupted receipts → CER/WER report and review UI |
| **A2.8 Vector search** | FAISS, pgvector, Qdrant/Milvus, Elasticsearch/OpenSearch | Exact vs HNSW/IVF, recall/latency/memory, filters, updates, replication, migrations | [ANN Benchmarks](https://ann-benchmarks.com/), [BEIR](https://github.com/beir-cellar/beir), synthetic vectors → benchmark and reindex plan |
| **A2.9 Explainability and monitoring** | SHAP/permutation importance; Pandera/Great Expectations; Evidently/custom metrics | Correlation, explanation stability, schema/drift alerts, delayed labels, sensitive data | Adult, California Housing, shifted copies → validation suite, dashboard, alert playbook |
| **A2.10 Geospatial tools** | GeoPandas/Shapely, Rasterio/rioxarray, PyProj, DuckDB Spatial/PostGIS | CRS, joins, invalid geometry, raster alignment, indexes, projection and spatial leakage | [Natural Earth](https://www.naturalearthdata.com/), [OSM extracts](https://download.geofabrik.de/), land-cover tiles → spatial pipeline and map |
| **A2.11 Audio and speech tools** | FFmpeg/TorchCodec for I/O; librosa; torchaudio transforms; Hugging Face Transformers; SpeechBrain | Resampling, channels, spectrograms/MFCCs, augmentation, batching, streaming, export, CPU/GPU latency | [UrbanSound8K](https://urbansounddataset.weebly.com/urbansound8k.html), [Speech Commands](https://www.tensorflow.org/datasets/catalog/speech_commands), [LibriSpeech](https://www.openslr.org/12), [MUSDB18](https://sigsep.github.io/datasets/musdb.html) → shared preprocessing pipeline and quality/speed benchmark |
| **A2.12 Probabilistic programming** | PyMC, Stan, NumPyro | MCMC vs variational inference; convergence, effective sample size, divergences, posterior predictive checks | Eight Schools, radon-style hierarchy, synthetic mixtures → posterior report and sampler benchmark |
| **A2.13 Online machine learning** | River vs incremental/batch scikit-learn | Progressive validation, drift detection, delayed labels, memory, update latency, recovery | [Electricity](https://www.openml.org/d/151), synthetic abrupt/gradual drift → streaming learner and drift dashboard |
| **A2.14 Graph machine learning** | PyTorch Geometric, DGL, NetworkX/non-neural baseline | Message passing, sampling, batching, explainability, memory, large-graph scaling | Cora/Citeseer, [Open Graph Benchmark](https://ogb.stanford.edu/), MovieLens graph → node/link benchmark |
| **A2.15 Conformal prediction** | MAPIE vs calibrated probabilities, quantile regression, ordinary intervals | Marginal/group coverage, interval width, exchangeability, shift, calibration-set size | California Housing, Adult, M4 → coverage dashboard and abstention policy |
| **A2.16 Distributed data processing** | Polars, DuckDB, Dask, Spark, Ray | Larger-than-memory scans, joins, skew, partitioning, lazy execution, failure recovery | [NYC Taxi](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), ClickBench, generated scale tests → correctness/performance matrix |
| **A2.17 Model-serving runtimes** | Framework-native inference, ONNX Runtime, TensorRT, OpenVINO | Export parity, dynamic shapes, quantization, batching, warm-up, throughput, tail latency | ResNet, small transformer, boosted trees → deployment decision matrix and load test |

#### A3. Applied Problem Families and Typical Solution Methods

Start with a cheap baseline. Match validation to future use; add complexity only when it improves the decision.

| ID and problem | Methods | Validate | Data → output |
|---|---|---|---|
| **A3.1 Tabular classification/regression** | Rules/mean; linear models; trees; forests; boosting; calibrated ensembles | Missingness, categoricals, leakage, group/time splits, calibration, business thresholds | Adult, Bank Marketing, California Housing, Bike Sharing, Wine Quality → pipeline, slice errors, batch scorer |
| **A3.2 Rare-event classification** | Rules; class weights; sampling/SMOTE; balanced ensembles; focal loss; calibrated thresholds | Time splits, delayed/noisy labels, PR metrics, precision@K, expected cost, review capacity | Credit Card Fraud, Mammography, synthetic drifting fraud → review queue and threshold policy |
| **A3.3 Forecasting** | Seasonal naive; ETS; ARIMA/SARIMAX; Prophet; lagged boosting; global neural models | Rolling origin, interval coverage, available exogenous data, holidays, intermittency, hierarchies | M4, Electricity Load, Bike Sharing, retail sales → backtester and planning report |
| **A3.4 Anomaly/change detection** | Rules; robust z-scores; seasonal residuals; isolation forest; LOF; one-class SVM; autoencoders; CUSUM/Bayesian methods | Event metrics, alert grouping, seasonality, threshold stability, delay and false-alert cost | [NAB](https://github.com/numenta/NAB), [NASA C-MAPSS](https://data.nasa.gov/dataset/c-mapss-aircraft-engine-simulator-data/xaut-bemq/about_data), synthetic sensor faults → streaming detector and operator feedback |
| **A3.5 Segmentation** | RFM rules; k-means/k-medoids; GMM; hierarchical clustering; DBSCAN/HDBSCAN | Scaling, mixed types, cluster/temporal stability, actionability | Wholesale Customers, retail transactions, synthetic customer data → stable assignments and profiles |
| **A3.6 Recommendations** | Popularity/recency; k-NN; matrix factorization; implicit models; two-tower; hybrid | Temporal splits, negative sampling, cold start, diversity, coverage, feedback loops | [MovieLens](https://grouplens.org/datasets/movielens/), [Amazon Reviews](https://amazon-reviews-2023.github.io/), synthetic catalog → candidate service and exploration plan |
| **A3.7 Search/ranking** | BM25; boosts/filters; embedding retrieval; cross-encoder; pairwise/listwise ranking | NDCG/MRR/Recall@K, query slices, position bias, hard negatives, freshness, latency | BEIR, [MS MARCO](https://microsoft.github.io/msmarco/), judged domain corpus → search API and relevance dashboard |
| **A3.8 NLP classification/extraction** | Rules; TF-IDF plus linear model; embeddings; transformer fine-tuning; token classification; schema-bound LLM | Label agreement, long documents, rare labels, span metrics, calibration, domain/language shift | AG News, 20 Newsgroups, IMDb, [CoNLL-2003](https://www.clips.uantwerpen.be/conll2003/ner/) → labeling guide and review queue |
| **A3.9 Vision: classification → detection → segmentation → verification** | CNN/ViT classification; YOLO/Faster R-CNN detection; U-Net/Mask R-CNN segmentation; embedding/metric-learning verification | Duplicate/subject leakage; class metrics; mAP; IoU/Dice; verification ROC; camera shift; edge latency | CIFAR-10 → COCO → Oxford Pet/Cityscapes → LFW → staged evaluation suite, exported models, review path |
| **A3.10 OCR/document understanding** | Cleanup/deskew; detection and recognition; layout; key-value extraction; tables; validation rules | CER/WER, field exact match, reading order, handwriting/languages, confidence, privacy | IAM, FUNSD, [RVL-CDIP](https://adamharley.com/rvl-cdip/), corrupted receipts → structured JSON and correction UI |
| **A3.11 Semantic search** | BM25; bi-encoder; hybrid retrieval; expansion; filters; reranking; ANN | Judged queries, hard negatives, Recall@K/MRR/NDCG, stale documents, migration, latency/recall | BEIR, MS MARCO, versioned domain corpus → retrieval API and evaluation harness |
| **A3.12 RAG** | Chunk/retrieve baseline; query rewrite; hybrid search; reranking; parent-child; HyDE; routing | Test ingestion, retrieval, and answers separately; citations, abstention, permissions, injection, cost, latency | BEIR, [Natural Questions](https://ai.google.com/research/NaturalQuestions/), [HotpotQA](https://hotpotqa.github.io/), versioned docs → traces and regression suite |
| **A3.13 Tool-using agents** | Workflow baseline; single-agent tools; planner/executor; verification; multi-agent only if useful | Task success, partial credit, tool traces, retries, budgets, safety, recovery, cost | Synthetic tasks, [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA), [SWE-bench](https://www.swebench.com/) → framework comparison and eval suite |
| **A3.14 Causal/uplift estimation** | Experiment baseline; adjustment; matching/weighting; DiD; causal forests; S/T/X/R learners | Estimand, causal graph, overlap/balance, post-treatment leakage, sensitivity/placebos | [LaLonde/NSW](https://users.nber.org/~rdehejia/data/nswdata2.html), [IHDP](https://www.fredjo.com/), synthetic effects → diagnostics and policy simulation |
| **A3.15 Survival analysis** | Kaplan–Meier; log-rank; Cox; AFT; survival forests; competing risks | Censoring, time-varying features, PH assumption, concordance, time calibration, leakage | [METABRIC](https://www.cbioportal.org/study/summary?id=brca_metabric), Rossi, synthetic failures → risk curves and intervention policy |
| **A3.16 Audio problem families** | Audio/music classification → keyword spotting → sound-event detection → ASR → enhancement/source separation → speaker verification | Speaker/device/session-disjoint splits; clip leakage; macro F1/mAP; WER; SI-SDR; EER; noise robustness; real-time factor | UrbanSound8K/GTZAN → Speech Commands → DCASE/AudioSet → LibriSpeech/Common Voice → MUSDB18/DNS Challenge → task pipelines and streaming demo |
| **A3.17 Facial and biometric vision** | Face detection/landmarks → age estimation → liveness/PAD → 1:1 verification → 1:N identification | Identity-disjoint splits; age MAE; FAR/FRR/EER and TAR@FAR; demographic slices; spoofing; consent, retention, and dataset licenses | [WIDER FACE](http://shuoyang1213.me/WIDERFACE/) → [300-W](https://ibug.doc.ic.ac.uk/resources/300-W/) → [UTKFace](https://susanqq.github.io/UTKFace/)/[FairFace](https://github.com/joojs/fairface) → [CelebA-Spoof](https://github.com/Davidzhangyuanhan/CelebA-Spoof) → [LFW](http://vis-www.cs.umass.edu/lfw/) → consent-based demo and system card |
| **A3.18 Uncertainty/conformal prediction** | Calibrated probabilities; quantile regression; conformal intervals/sets; selective prediction | Coverage and width; calibration by slice; exchangeability; distribution shift; abstention cost | California Housing, Adult, M4 → risk-aware prediction API and coverage report |
| **A3.19 Online learning/concept drift** | Incremental linear/tree models; sliding windows; ensembles; drift detectors; retraining policies | Prequential metrics; delayed labels; abrupt/gradual/recurring drift; memory and update latency | Electricity, click streams, synthetic drift → streaming scorer, alarms, rollback policy |
| **A3.20 Graph prediction** | Graph heuristics; embeddings; GCN/GAT/GraphSAGE; link prediction; graph classification | Temporal edge splits, negative sampling, neighborhood leakage, inductive nodes, sampling bias | Cora/Citeseer, OGB, molecular or transaction graphs → node/link service and explanations |
| **A3.21 Active, weak, and semi-supervised learning** | Uncertainty/diversity sampling; pseudo-labeling; consistency training; labeling functions; label models | Label efficiency, annotator disagreement, selection bias, confirmation bias, class coverage | 20 Newsgroups, CIFAR-10, synthetic rare classes → labeling UI and performance-per-label curves |
| **A3.22 Multi-label/hierarchical classification** | Binary relevance; classifier chains; label embeddings; hierarchy-aware loss; constrained decoding | Micro/macro/sample F1, precision@K, rare labels, hierarchy violations, calibration | Bibtex/EUR-Lex, Open Images subset, product taxonomy → taxonomy-aware API and error report |
| **A3.23 Contextual bandits** | Random policy; epsilon-greedy; UCB; Thompson sampling; linear/neural contextual bandits | Cumulative regret, exploration safety, delayed rewards, non-stationarity, off-policy evaluation | Synthetic simulator, [Open Bandit Dataset](https://research.zozo.com/data.html) → policy simulator and replay evaluation |
| **A3.24 Multimodal learning** | Early/late fusion; contrastive embeddings; cross-attention; multimodal retrieval; missing-modality fallback | Alignment leakage, modality ablation, missing/noisy inputs, retrieval metrics, compute cost | Flickr30k, VQA subset, AudioCaps or a text/image catalog → multimodal search or classification API |
| **A3.25 Geospatial prediction** | Spatial baselines; hotspot detection; spatial regression; routing; raster classification | Spatial/temporal holdouts, autocorrelation, CRS, boundary effects, resolution, map uncertainty | NYC Taxi, OSM, SpaceNet or land-cover tiles → spatial model, map, and validation report |
| **A3.26 Privacy-preserving ML** | Federated averaging; secure aggregation simulation; differential privacy; local/on-device learning | Privacy budget, membership inference, utility loss, client imbalance/dropout, communication cost | FEMNIST/LEAF, Adult, synthetic client partitions → privacy/utility report and federated simulator |
| **A3.27 Synthetic-data evaluation** | Parametric simulation; resampling; GAN/VAE/diffusion or tabular synthesizers; constraint-based generation | Fidelity, downstream utility, rare-case coverage, memorization/privacy leakage, bias amplification | Adult, Credit Card Fraud, time series, domain simulator → dataset card and real-vs-synthetic benchmark |

#### A4. Language and Runtime Implementations

Reuse the same model, preprocessing, dataset split, and golden test vectors across implementations. Keep general API and concurrency exercises in Section B.

| ID and challenge | Build | Validate | Data → output |
|---|---|---|---|
| **A4.1 Cross-language inference** | Train in Python; export ONNX; run in Python, C++, C#, Java, and JavaScript | Preprocessing/tensor parity, numeric tolerance, unsupported operators, latency, memory | MNIST or Adult → golden vectors and cross-runtime benchmark |
| **A4.2 Rust inference engine** | Load and run a linear, tree, or k-NN model without Python; add typed schema and optional SIMD | Prediction parity, malformed models, zero-copy loading, concurrency, throughput | Adult or Fashion-MNIST features → Rust library/CLI and benchmark |
| **A4.3 Go streaming scorer** | Event ingestion, online features, batching, scorer, bounded goroutine pipeline | Ordering, duplicates, backpressure, graceful shutdown, tail latency | Synthetic fraud/click stream → service, load test, failure report |
| **A4.4 SQL-native ML pipeline** | Recreate feature engineering and linear/tree scoring in DuckDB or PostgreSQL | Point-in-time joins, nulls, types, SQL/Python feature and prediction parity | Bike Sharing or transaction data → versioned SQL pipeline and parity tests |
| **A4.5 JVM distributed pipeline** | Feature preparation and training with Java/Scala and Spark | Partitioning, skew, serialization, reproducibility, local/distributed agreement | NYC Taxi, HIGGS, or generated large tables → scaling and cost report |
| **A4.6 Browser inference** | TypeScript app using ONNX Runtime Web with WASM/WebGPU; cache model locally | Browser compatibility, preprocessing parity, offline mode, memory, latency | MNIST, small vision/audio classifier → offline web demo and compatibility matrix |
| **A4.7 Native performance kernel** | Matrix multiplication, convolution, softmax, or distance search in C/C++ | Reference parity, cache/thread/SIMD profiling, input-shape scaling, numerical stability | Generated tensors → library, profiler evidence, regression benchmark |
| **A4.8 GPU kernel** | Implement one operation in CUDA or Triton; add tiling and mixed precision | CPU/reference parity, memory access, occupancy, warm-up, shape sensitivity | Generated matrices/tensors → kernel benchmark and optimization report |
| **A4.9 Portable model package** | Language-neutral schema for model, preprocessing, labels, metadata, and checksums | Schema versioning, backward compatibility, corruption handling, three-language loading | Linear/tree model and golden vectors → specification, readers, compatibility suite |
| **A4.10 R statistical service** | Build with tidymodels/mlr3; package model and expose a Plumber API | Reproducibility, package tests, coefficient/prediction parity, API behavior | Bank Marketing or survival data → R package, API, comparison report |

---

### B. Programming

| # | Challenge | Suggested technologies or focus |
|---:|---|---|
| 11 | REST API | FastAPI, ASP.NET, Go, or Node.js |
| 12 | Authentication | JWT, OAuth, and API keys |
| 13 | CLI tool | Python versus Rust |
| 14 | ORM comparison | SQLAlchemy, Django ORM, Entity Framework, and raw SQL |
| 15 | Concurrency | Threading, async, multiprocessing, and distributed queues |
| 16 | Plugin architecture | Interfaces, discovery, isolation, and lifecycle |
| 17 | Caching | Redis, memory, and file caches |
| 18 | Message queues | RabbitMQ, Kafka, and Redis Streams |
| 19 | API gateway | Authentication, rate limiting, and logging |
| 20 | Event-driven application | Events, handlers, delivery guarantees, and recovery |

---

### C. Infrastructure

| # | Challenge | Suggested technologies or focus |
|---:|---|---|
| 21 | Containers and orchestration | Docker, Compose, and Kubernetes |
| 22 | CI/CD | Build, test, release, deploy, and rollback |
| 23 | Monitoring and tracing | Grafana, Prometheus, OpenTelemetry, and Jaeger |
| 24 | Structured logging | Correlation IDs and cross-service diagnostics |
| 25 | Reverse proxy | Nginx, Caddy, and Traefik |
| 26 | Database backup and recovery | Backups and point-in-time recovery (PITR) |
| 27 | High availability | Replication, failover, and degraded operation |
| 28 | Load testing | Throughput, latency, saturation, and bottlenecks |
| 29 | Secret management | Vault, Docker Secrets, and Kubernetes Secrets |
| 30 | Infrastructure as code | Terraform and Ansible |

---

### D. Mathematics

| # | Challenge | Suggested scope |
|---:|---|---|
| 31 | Matrix library | Storage, operations, correctness, and performance |
| 32 | Singular value decomposition | Derivation, implementation, and verification |
| 33 | PCA without `eig()` | Centering, SVD, explained variance, and reconstruction |
| 34 | Fast Fourier transform | Implementation, complexity, and signal examples |
| 35 | Optimization methods | Gradient descent, Newton, Adam, and L-BFGS |
| 36 | Automatic differentiation | Forward mode, reverse mode, and gradient checks |
| 37 | Kalman filter | State estimation, uncertainty, and noisy sensors |
| 38 | Monte Carlo methods | Simulation, error estimation, and variance reduction |
| 39 | Graph algorithms | A*, Dijkstra, and Bellman–Ford |
| 40 | Bayesian inference | Gibbs sampling and convergence diagnostics |

---

## Group 2: Systems Projects

> **Typical duration:** 1 month to 6+ months per project.

These projects combine multiple disciplines into production-like systems. Scope and operational depth should increase at each level.

### Level 1

| # | Project |
|---:|---|
| 1 | Marketing Intelligence Platform |
| 2 | Fraud Detection Platform |
| 3 | Predictive Maintenance Platform |
| 4 | OCR Document Platform |
| 5 | Recommendation System |

### Level 2

| # | Project |
|---:|---|
| 6 | Data Platform |
| 7 | MLOps Platform |
| 8 | Agentic Research Platform |
| 9 | GIS Intelligence Platform |
| 10 | Financial Risk Platform |

### Level 3

| # | Project |
|---:|---|
| 11 | Distributed Search Engine |
| 12 | Feature Store |
| 13 | Lakehouse |
| 14 | Enterprise AI Platform |
| 15 | Autonomous Data Scientist |

---

## What Makes These Valuable?

Increase project difficulty with constraints such as:

- Use an unfamiliar language such as Go or Rust.
- Compare high-level frameworks with minimal-dependency implementations.
- Handle datasets larger than memory.
- Meet strict latency and throughput budgets.
- Deploy to Kubernetes, serverless, or air-gapped environments.
- Add retries, backups, disaster recovery, and graceful degradation.
- Implement metrics, tracing, dashboards, and structured logging.
- Integrate existing open-source platforms before building simplified versions.
- Add authentication, authorization, encryption, auditing, and secret management.
- Produce architecture diagrams, API documentation, automated tests, and runbooks.

The goal is to become capable of designing, building, deploying,
operating, and maintaining production-quality systems rather than merely
implementing algorithms.
