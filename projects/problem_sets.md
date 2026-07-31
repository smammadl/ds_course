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

This section contains three different kinds of practice. They should not be treated as interchangeable:

| Track | Practice mode | Purpose |
|---|---|---|
| **A1** | Algorithm reconstruction | Implement foundational algorithms, understand their mechanics, and compare them with production libraries. |
| **A2** | Specialized library laboratories | Learn the capabilities, tradeoffs, and failure modes of important domain-specific tools. |
| **A3** | Applied problem families | Solve recurring real-world problems with suitable baselines, validation, metrics, and deployment constraints. |

> **Standard for every challenge:** Record the dataset version and license, create a data card, keep an untouched test set, measure runtime and memory, and include at least one deliberately corrupted or shifted-data test. The listed datasets are characteristic starting points—not endorsements or substitutes for understanding the target domain.

#### A1. Foundational Algorithms: Rebuild, Verify, Compare

The goal is not to replace mature libraries. Implement the smallest correct version, test it against analytically solvable cases, and then explain what the production implementation adds.

##### A1.1 Linear and Logistic Regression

- **Implement:** ordinary least squares using the normal equation and QR/SVD-based solving; batch and mini-batch gradient descent; binary logistic regression; L1/L2 regularization; probability prediction.
- **Verify:** finite-difference gradient checks, convergence curves, coefficient recovery on synthetic data, and behavior under collinearity, outliers, feature scaling, and class separation.
- **Compare:** scikit-learn `LinearRegression`, `Ridge`, `Lasso`, and `LogisticRegression`; statsmodels for inference and diagnostics.
- **Characteristic datasets:** [California Housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) for regression, [UCI Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) for count-like regression, and [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) for binary classification.
- **Deliverable:** serialized model format, coefficient report, benchmark table, unit tests, and a batch prediction CLI or API.

##### A1.2 Classification and Regression Trees

- **Implement:** CART-style recursive splitting, Gini/entropy and squared-error objectives, stopping rules, prediction, cost-complexity pruning, and basic numeric/categorical feature handling.
- **Verify:** hand-calculated splits, repeated values, constant features, missing values, depth limits, and overfitting as depth increases.
- **Compare:** scikit-learn decision trees and Graphviz export; explain optimized split search, pruning paths, and library behavior for missing/categorical values.
- **Characteristic datasets:** [UCI Adult](https://archive.ics.uci.edu/dataset/2/adult) for mixed tabular features, [Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) for classification/regression, and synthetic XOR data for interaction behavior.
- **Deliverable:** inspectable tree representation, pruning study, feature-importance caveat note, and browser or Graphviz visualization.

##### A1.3 Bagging and Random Forests

- **Implement:** bootstrap sampling, randomized feature selection, aggregation, out-of-bag scoring, reproducible parallel tree training, and permutation importance.
- **Verify:** variance reduction as trees are added, OOB/test agreement, deterministic seeding, correlated-feature importance, and class imbalance behavior.
- **Compare:** scikit-learn `RandomForest`, `ExtraTrees`, and a single decision tree; measure quality, training time, inference time, memory, and model size.
- **Characteristic datasets:** [UCI Covertype](https://archive.ics.uci.edu/dataset/31/covertype) for larger multiclass tabular data, Adult, and synthetic noisy nonlinear data.
- **Deliverable:** parallel trainer, OOB diagnostics, scaling plot, and documented differences between bagging, random forests, and extremely randomized trees.

##### A1.4 Gradient Boosted Trees

- **Implement:** regression trees fitted sequentially to residuals, learning rate, row/feature subsampling, early stopping, and at least squared-error and logistic objectives with first-order gradients.
- **Verify:** residual reduction by stage, overfitting with excessive rounds, learning-rate/tree-count tradeoff, and numerical stability of logistic loss.
- **Compare:** scikit-learn gradient boosting and histogram gradient boosting; then compare concepts with XGBoost, LightGBM, and CatBoost without attempting to reproduce all their optimizations.
- **Characteristic datasets:** [HIGGS](https://archive.ics.uci.edu/dataset/280/higgs) or a sampled version for scale, Adult for categoricals, and California Housing for regression.
- **Deliverable:** stage-wise training plots, benchmark matrix, feature handling analysis, and explanation of regularization and leakage-safe early stopping.

##### A1.5 k-Nearest Neighbors and Neighbor Search

- **Implement:** brute-force k-NN classification/regression, distance functions, feature scaling, weighted neighbors, and a KD-tree or ball-tree for low-dimensional search.
- **Verify:** ties, duplicate points, irrelevant dimensions, distance concentration, query latency, and memory growth.
- **Compare:** scikit-learn neighbors, SciPy spatial search, and FAISS or HNSW-based approximate search on larger embeddings.
- **Characteristic datasets:** [UCI Wine](https://archive.ics.uci.edu/dataset/109/wine), [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist), and synthetic datasets with increasing dimension.
- **Deliverable:** exact-versus-approximate recall/latency curves and a note explaining when indexing stops helping.

##### A1.6 Naive Bayes and a Sparse Text Classifier

- **Implement:** Gaussian, multinomial, and Bernoulli Naive Bayes; Laplace smoothing; log-space likelihoods; bag-of-words and TF-IDF.
- **Verify:** zero-count features, underflow, unknown vocabulary, calibration, class imbalance, and violations of feature independence.
- **Compare:** scikit-learn Naive Bayes and logistic regression on the same sparse features.
- **Characteristic datasets:** [20 Newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html), [IMDb Large Movie Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/), and a small spam dataset with documented provenance.
- **Deliverable:** reusable tokenizer/vectorizer, confusion analysis, calibration plot, and model-size/latency comparison.

##### A1.7 k-Means and Gaussian Mixture Models

- **Implement:** k-means++, Lloyd's algorithm, empty-cluster recovery, inertia, Gaussian mixtures with expectation-maximization, and soft assignments.
- **Verify:** sensitivity to initialization and scaling, non-spherical clusters, local minima, singular covariance matrices, and convergence.
- **Compare:** scikit-learn `KMeans`, `MiniBatchKMeans`, and `GaussianMixture`; compare internal metrics with domain usefulness.
- **Characteristic datasets:** [UCI Wholesale Customers](https://archive.ics.uci.edu/dataset/292/wholesale+customers), Wine, and synthetic blobs, moons, rings, and unequal-density clusters.
- **Deliverable:** stability study across seeds, cluster profiles, and a demonstration of why a visually plausible cluster is not necessarily actionable.

##### A1.8 Multilayer Perceptron and Backpropagation

- **Implement:** dense layers, activations, softmax cross-entropy, backpropagation, mini-batches, initialization, SGD/momentum/Adam, dropout, and model save/load using only array operations.
- **Verify:** numerical gradient checks, overfitting a tiny batch, exploding/vanishing gradients, reproducibility, and loss stability.
- **Compare:** an equivalent PyTorch, JAX, or TensorFlow model; profile automatic differentiation, accelerators, data loading, and mixed precision rather than only final accuracy.
- **Characteristic datasets:** [MNIST](https://www.openml.org/d/554), Fashion-MNIST, and a synthetic two-dimensional classification task.
- **Deliverable:** training engine, profiler report, learning curves, checkpoint format, and inference endpoint.

#### A2. Specialized Library Laboratories

These are controlled comparisons, not "import four libraries and print
scores." Use the same split, preprocessing, metric, compute budget, and
failure cases. Explain which tool should be selected under which
constraints.

##### A2.1 Production Gradient-Boosting Libraries

- **Compare:** XGBoost, LightGBM, and CatBoost on identical tabular classification and regression tasks.
- **Investigate:** categorical features, missing values, sparse data, monotonic constraints, early stopping, CPU/GPU training, probability calibration, model export, and inference latency.
- **Characteristic datasets:** Adult, HIGGS sample, California Housing, and a synthetic dataset with high-cardinality categoricals.
- **Deliverable:** decision matrix showing quality, speed, memory, operational complexity, and the concrete reason for each difference.

##### A2.2 Hyperparameter Optimization and AutoML

- **Compare:** random search and successive halving with Optuna or Ray Tune; compare a constrained AutoML system such as AutoGluon, FLAML, or H2O AutoML with a carefully built manual baseline.
- **Investigate:** search-space design, pruning, nested validation, compute budgets, experiment resumption, trial reproducibility, and leaderboard overfitting.
- **Characteristic datasets:** a small OpenML classification suite such as Adult, Bank Marketing, and Covertype rather than a single dataset.
- **Deliverable:** accuracy-versus-compute frontier, experiment store, reproducible best pipeline, and recommendation under fixed time and memory limits.

##### A2.3 Imbalanced-Learning Tooling

- **Compare:** imbalanced-learn pipelines for random under/oversampling, SMOTE variants, ensemble methods, and class weighting; implement focal loss in a deep-learning framework.
- **Investigate:** resampling inside rather than before cross-validation, probability calibration after resampling, threshold selection, and precision at a fixed review capacity.
- **Characteristic datasets:** [Credit Card Fraud Detection](https://www.openml.org/d/1597), [UCI Mammography](https://www.openml.org/d/310), and synthetic data with controllable rarity and class overlap.
- **Deliverable:** leakage demonstration, PR curves, calibration plots, cost matrix, and threshold policy.

##### A2.4 Time-Series Ecosystem

- **Compare:** statsmodels or StatsForecast, Prophet, MLForecast or sktime, gradient-boosted lag models, and one neural package such as Darts or NeuralForecast.
- **Investigate:** frequency inference, missing intervals, exogenous features, hierarchical series, probabilistic intervals, rolling backtests, and cold-start behavior.
- **Characteristic datasets:** [M4](https://github.com/Mcompetitions/M4-methods/tree/master/Dataset), [UCI Electricity Load Diagrams](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014), Bike Sharing, and a sparse/intermittent-demand series.
- **Deliverable:** seasonal-naive baseline, consistent backtest harness, accuracy/runtime table, residual diagnostics, and planning-oriented forecast report.

##### A2.5 Computer-Vision Ecosystem

- **Compare:** OpenCV preprocessing, torchvision or KerasCV, timm model backbones, Albumentations, and a current YOLO implementation for detection.
- **Investigate:** transfer learning, augmentation, class imbalance, annotation formats, non-maximum suppression, mixed precision, model export, and CPU/GPU/edge latency.
- **Characteristic datasets:** [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html), [Oxford-IIIT Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/), and a small [COCO](https://cocodataset.org/) subset.
- **Deliverable:** comparable training recipe, error gallery, latency and memory benchmarks, exported model, and inference service.

##### A2.6 NLP and Embedding Ecosystem

- **Compare:** spaCy for linguistic pipelines, Hugging Face Transformers for fine-tuning, Sentence Transformers for embeddings, and a simple TF-IDF baseline.
- **Investigate:** tokenization, truncation, batching, domain shift, multilingual behavior, quantization, calibration, model cards, and throughput.
- **Characteristic datasets:** 20 Newsgroups, IMDb, [AG News](https://huggingface.co/datasets/fancyzhx/ag_news), and a small domain-specific corpus created with a labeling guide.
- **Deliverable:** common evaluation harness, accuracy/latency/cost frontier, slice analysis, and deployable batch or online pipeline.

##### A2.7 OCR and Document-AI Libraries

- **Compare:** Tesseract, PaddleOCR, EasyOCR, and docTR or a cloud OCR service if available; keep image preprocessing constant.
- **Investigate:** orientation, layout, tables, handwriting, multilingual text, bounding boxes, confidence calibration, CPU/GPU throughput, and post-processing rules.
- **Characteristic datasets:** [IAM Handwriting](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database), [FUNSD](https://guillaumejaume.github.io/FUNSD/), and a synthetic receipt/invoice set with blur, rotation, shadows, and compression.
- **Deliverable:** character/word error rates, layout-aware error taxonomy, cost/latency comparison, and review interface for uncertain fields.

##### A2.8 Vector Search Engines

- **Compare:** FAISS for local indexing, pgvector for relational integration, and Qdrant, Milvus, Elasticsearch, or OpenSearch for a service-oriented system.
- **Investigate:** exact versus HNSW/IVF search, recall/latency/memory, filtering, index build/update, deletion, persistence, replication, multi-tenancy, and embedding-version migration.
- **Characteristic datasets:** [ANN Benchmarks](https://ann-benchmarks.com/), [BEIR](https://github.com/beir-cellar/beir) subsets, and synthetic vectors with controlled dimension and scale.
- **Deliverable:** benchmark harness, filtered-search test, operational comparison, and zero- or low-downtime reindex plan.

##### A2.9 Explainability, Validation, and Monitoring

- **Compare:** SHAP and permutation importance for model explanation; Pandera or Great Expectations for data contracts; Evidently or custom metrics for drift and performance monitoring.
- **Investigate:** correlated features, unstable explanations, local versus global importance, schema drift, delayed labels, reference windows, alert thresholds, and sensitive-data leakage.
- **Characteristic datasets:** Adult for fairness/slice analysis, California Housing for correlated regression features, and a synthetically shifted copy of either dataset.
- **Deliverable:** model/data validation suite, explanation stability report, drift dashboard, alert playbook, and false-alarm analysis.

##### A2.10 Geospatial Data Science Libraries

- **Compare:** GeoPandas and Shapely for vector operations, Rasterio or rioxarray for rasters, PyProj for coordinate systems, and DuckDB Spatial or PostGIS for larger queries.
- **Investigate:** coordinate reference systems, spatial joins, invalid geometries, raster/vector alignment, spatial indexes, map projection distortion, and spatial leakage in random splits.
- **Characteristic datasets:** [Natural Earth](https://www.naturalearthdata.com/), [OpenStreetMap extracts](https://download.geofabrik.de/), and a public land-cover or satellite-image tile set for one region.
- **Deliverable:** reproducible spatial pipeline, correctness checks, performance benchmark, spatial cross-validation, and interactive map.

#### A3. Applied Problem Families and Typical Solution Methods

Each problem-family challenge begins with a decision and a cheap
baseline. Use validation that matches how the system will encounter
future data. A more complex model is successful only if it improves the
decision under realistic constraints.

##### A3.1 General Tabular Classification and Regression

- **Typical methods:** rules and mean/majority baselines; linear/logistic models; trees; random forests; gradient boosting; calibrated ensembles.
- **Key practice:** missingness, categorical encoding, leakage, group/time-aware splits, calibration, confidence intervals, feature provenance, and business-cost thresholds.
- **Characteristic datasets:** Adult or Bank Marketing for classification; California Housing, Bike Sharing, or Wine Quality for regression.
- **Deliverable:** end-to-end pipeline, baseline ladder, slice-level errors, data/model card, and batch scoring job.

##### A3.2 Rare-Event and Imbalanced Classification

- **Typical methods:** anomaly/rules baseline, class weights, under/oversampling, SMOTE variants, balanced ensembles, focal loss, probability calibration, and cost- or capacity-based thresholds.
- **Key practice:** time-based splitting, delayed/noisy labels, precision-recall rather than accuracy, precision at K, expected cost, investigator capacity, and feedback-loop bias.
- **Characteristic datasets:** OpenML Credit Card Fraud, Mammography, and synthetic fraud streams with drift and controllable prevalence.
- **Deliverable:** review queue, threshold policy, PR/calibration plots, segment analysis, and drift simulation.

##### A3.3 Time-Series Forecasting

- **Typical methods:** last-value and seasonal-naive baselines; exponential smoothing; ARIMA/SARIMAX; Prophet; lag-feature gradient boosting; global neural models when many related series exist.
- **Key practice:** rolling-origin validation, prediction intervals, exogenous-variable availability, holidays, intermittent demand, hierarchy reconciliation, and forecast-value evaluation.
- **Characteristic datasets:** M4, Electricity Load Diagrams, Bike Sharing, and a retail-style hierarchical sales dataset.
- **Deliverable:** backtesting framework, interval coverage analysis, residual diagnostics, scenario interface, and planning recommendation.

##### A3.4 Anomaly and Change Detection

- **Typical methods:** domain rules; robust z-scores and seasonal residuals; isolation forest; local outlier factor; one-class SVM; autoencoders; Bayesian or CUSUM-style change-point detection.
- **Key practice:** event-based evaluation, alert grouping, label scarcity, seasonality, root-cause context, threshold stability, and false-alert cost.
- **Characteristic datasets:** [Numenta Anomaly Benchmark](https://github.com/numenta/NAB), [NASA C-MAPSS](https://data.nasa.gov/dataset/c-mapss-aircraft-engine-simulator-data/xaut-bemq/about_data), and synthetic sensor streams with injected point, contextual, and collective anomalies.
- **Deliverable:** streaming detector, alert explanations, detection delay/false-alarm report, and operator feedback loop.

##### A3.5 Customer or Entity Segmentation

- **Typical methods:** rule-based RFM segmentation; k-means/k-medoids; Gaussian mixtures; hierarchical clustering; DBSCAN/HDBSCAN; embeddings followed by clustering.
- **Key practice:** scaling, mixed data types, cluster stability, temporal stability, naming and profiling clusters, and measuring whether segments support different actions.
- **Characteristic datasets:** Wholesale Customers, an online-retail transactions dataset, and synthetic mixed-type customer records.
- **Deliverable:** reproducible segment assignment, stability report, profiles, action proposal, and evidence that clusters outperform a simpler business rule.

##### A3.6 Recommendation Systems

- **Typical methods:** popularity and recency baselines; user/item k-NN; matrix factorization; implicit-feedback methods; two-tower retrieval; content-based and hybrid systems.
- **Key practice:** temporal splits, negative sampling, cold start, seen-item filtering, implicit bias, diversity/novelty/coverage, feedback loops, and online experiment design.
- **Characteristic datasets:** [MovieLens](https://grouplens.org/datasets/movielens/), [Amazon Reviews 2023](https://amazon-reviews-2023.github.io/), and a small synthetic catalog with new users and items.
- **Deliverable:** candidate-generation service, offline evaluation, recommendation explanations, and exploration plan.

##### A3.7 Search and Learning to Rank

- **Typical methods:** BM25 lexical retrieval; field boosts and filters; embedding retrieval; cross-encoder reranking; pairwise/listwise learning-to-rank when judgments and interaction logs exist.
- **Key practice:** graded relevance judgments, NDCG/MRR/Recall@K, query slices, position bias, hard negatives, index freshness, and latency budgets.
- **Characteristic datasets:** BEIR subsets, [MS MARCO](https://microsoft.github.io/msmarco/), and a domain corpus with manually judged queries.
- **Deliverable:** search API, judgment set, offline relevance dashboard, zero-result analysis, and index migration procedure.

##### A3.8 NLP Classification and Information Extraction

- **Typical methods:** regex/rules; bag-of-words plus linear models; pretrained embeddings; transformer fine-tuning; token classification; constrained LLM extraction with schema validation.
- **Key practice:** annotation guidelines, inter-annotator agreement, long documents, rare labels, span-level metrics, calibration, multilingual/domain shift, and human review.
- **Characteristic datasets:** AG News or 20 Newsgroups for topic classification, IMDb for sentiment, and [CoNLL-2003](https://www.clips.uantwerpen.be/conll2003/ner/) for named entities.
- **Deliverable:** labeling guide, baseline ladder, per-class/span error taxonomy, throughput benchmark, and low-confidence review queue.

##### A3.9 Image Classification, Detection, and Segmentation

- **Typical methods:** classical image features plus a linear baseline; pretrained CNN/vision-transformer fine-tuning; YOLO-style detection; U-Net or mask-based segmentation.
- **Key practice:** duplicate and subject leakage, augmentation, annotation quality, class imbalance, precision/recall by object size, robustness to lighting/camera changes, and edge latency.
- **Characteristic datasets:** CIFAR-10 for classification, Oxford-IIIT Pet for classification/segmentation, and COCO subsets for detection.
- **Deliverable:** error gallery, dataset audit, exported model, latency/memory report, and uncertain-case review path.

##### A3.10 OCR and Document Understanding

- **Typical methods:** image cleanup and deskewing; text detection plus recognition; layout detection; key-value/token classification; table extraction; constrained post-processing and validation rules.
- **Key practice:** character/word error rate, field-level exact match, page layout, reading order, handwriting, multilingual text, confidence calibration, and private-information handling.
- **Characteristic datasets:** IAM for handwriting, FUNSD for forms, [RVL-CDIP](https://adamharley.com/rvl-cdip/) for document classes, and a synthetic receipt/invoice corruption suite.
- **Deliverable:** ingestion pipeline, structured JSON output, field provenance/bounding boxes, benchmark, and human-correction interface.

##### A3.11 Semantic Search

- **Typical methods:** BM25 baseline; bi-encoder embeddings; hybrid retrieval; query/document expansion; metadata filtering; cross-encoder reranking; approximate nearest-neighbor indexing.
- **Key practice:** domain-specific judgment sets, hard negatives, Recall@K/MRR/NDCG, multilingual queries, stale/deleted documents, embedding migrations, and latency/recall tradeoffs.
- **Characteristic datasets:** BEIR subsets, MS MARCO passage ranking, and a versioned domain corpus with 50--200 human-judged queries.
- **Deliverable:** retrieval API, evaluation harness, failure slices, index-update process, and exact-versus-approximate benchmark.

##### A3.12 Retrieval-Augmented Generation (RAG)

- **Typical methods:** naive chunk-and-retrieve baseline; query rewrite; hybrid retrieval; reranking; parent-child retrieval; multi-query or HyDE; metadata routing; graph retrieval only when relationships justify it.
- **Key practice:** evaluate ingestion, retrieval, and answer generation separately; test citation correctness, abstention, access control, prompt injection, document updates, cost, and latency.
- **Characteristic datasets:** BEIR for retrieval, [Natural Questions](https://ai.google.com/research/NaturalQuestions/), [HotpotQA](https://hotpotqa.github.io/) for multi-hop questions, and a small versioned documentation corpus with unanswerable questions.
- **Deliverable:** no-framework baseline followed by one framework-based implementation, trace viewer, regression suite, groundedness report, and per-query cost breakdown.

##### A3.13 Tool-Using Agents and Agent Frameworks

- **Typical methods:** deterministic workflow/state machine baseline; single-agent tool use; planner/executor; reflection or verification; multi-agent coordination only when roles add measurable value.
- **Compare:** implement one bounded task directly and then with LangGraph, AutoGen, CrewAI, and OpenAI Agents SDK where applicable; compare control flow, observability, recovery, portability, and cost.
- **Characteristic tasks/datasets:** a private synthetic tool-use suite, [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA), [SWE-bench](https://www.swebench.com/), or a small WebArena-style set; choose only tasks permitted by the available environment.
- **Deliverable:** versioned evaluation tasks, success and partial-credit metrics, tool-call traces, retry/budget policy, safety tests, and evidence that an agent improves on a fixed workflow.

##### A3.14 Causal Effect and Uplift Estimation

- **Typical methods:** randomized experiment baseline; regression adjustment; matching/weighting; difference-in-differences; causal forests; S/T/X/R-learners for heterogeneous treatment effects.
- **Key practice:** define the estimand, draw a causal graph, separate identification from estimation, inspect overlap/balance, prevent post-treatment leakage, and perform sensitivity/placebo tests.
- **Characteristic datasets:** [LaLonde/NSW](https://users.nber.org/~rdehejia/data/nswdata2.html), [IHDP](https://www.fredjo.com/), and synthetic data where the true treatment effect is known.
- **Deliverable:** assumptions register, naive-versus-causal comparison, balance diagnostics, uncertainty, uplift policy simulation, and a statement of what cannot be concluded.

##### A3.15 Survival and Time-to-Event Modeling

- **Typical methods:** Kaplan-Meier curves; log-rank tests; Cox proportional hazards; accelerated failure-time models; random survival forests; competing-risk models.
- **Key practice:** right/left censoring, time-varying covariates, proportional-hazards checks, concordance and calibration over time, leakage from future observations, and actionable horizons.
- **Characteristic datasets:** [METABRIC](https://www.cbioportal.org/study/summary?id=brca_metabric), the Rossi recidivism dataset distributed with lifelines, and synthetic censored equipment-failure data.
- **Deliverable:** survival curves, risk estimates at decision horizons, calibration analysis, assumption diagnostics, and maintenance or intervention policy.

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
