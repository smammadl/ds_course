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
