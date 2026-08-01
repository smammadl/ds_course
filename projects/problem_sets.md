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
