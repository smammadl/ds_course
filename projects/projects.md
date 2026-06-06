# Claimed topics

1. Arzu
    - recommendation system (raw)
        - fashion item detection
        - clip
        - vectorization
        - vector db
        - streamlit UI
    - recommendation system (ideal)
2. Nijat 
    - data cleaning
        - data source, 
            - raw htmls
            - quality level
            - db (OLTP): sqlite (postgres)
        - cleaning
            - db (OLAP): duckdb (clickhouse)
    - UI for duckdb
3. Farida
    - recommendation system 
        - dataset: 
            - [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/) or [MovieLens 100K](https://www.kaggle.com/datasets/fakhrealam0786/movielens-100k-dataset)
            - [MovieLens 1M](https://grouplens.org/datasets/movielens/1m/) or [MovieLens 1M](https://www.kaggle.com/datasets/odedgolden/movielens-1m-dataset)
        - Model A: neural networks, e.g. Two-Tower Architecture, DeepFM, DCN, etc.
        - Model B: specialized models, using `scikit-surprise` library
        - Model C: no learning, just filtering, e.g. item-based collaborative filtering
        - model, training, performance, etc
4. Elton
    - parking lot utilisation
        - create dataset (static)
        - annotation: parking lots
        - preprocessing: augmentation
        - model: existing or custom
        - working model
    - raw video input - annotated video out
5. Murad
    - binaaz scraping: explanation
    - dataset cleaning
        - text encoding methods
            - ifidf
            - embedding
            - hybrid model, X
    - classic model
    - Live hosting, UI, 
        - null cases
        - edge cases
        - range
        - default
6. Turkan
    - timeseries dataset
        - [Chemical Process Monitoring Time-Series Dataset](https://www.kaggle.com/datasets/rohit8527kmr7518/chemical-process-monitoring-time-series-dataset)
    - Model A: Sequence-Based Neural Network Approach (anomaly detection)
        - ideally LSTM (at least RNN)
    - Model B: PCA or Autoencoder based approach
    - performance, evaluation
    - program to predict
7. Aliyar
    - search
        - telegram (1 time)
        - json -> csv
        - engagement analytics
            - powerbi
        - vector based search
            - based on data
            - prompt based search
            - model? (ready)
    - classification
        - topic 
        - vulgarity
        - labelling
8. Asgar
10. Aynur
11. Lala
12. Aytaj
13. Isa 
14. Seymur
15. Mahammad
16. Karam

---

# Potential Unclaimed problems:

## Tabular Data
- Recommendation System
    - [Amazon Product Graph](https://snap.stanford.edu/data/amazon/productGraph/)
- Regression
    - [Home Credit Default Risk](https://www.kaggle.com/competitions/home-credit-default-risk/data)
- Anomaly Detection
    - [NSL-KDD99 Dataset](https://www.kaggle.com/datasets/kaggleprollc/nsl-kdd99-dataset)
    - Yahoo Webscope S5
    - Melbourne University Seizure Prediction (EEG)

## Time Series
- Rossmann Store Sales
    - [Rossmann Store Sales](https://www.kaggle.com/competitions/rossmann-store-sales/data)
    - [Walmart Recruiting - Store Sales Forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)
    - PJM Electricity Hourly Load
    - 

## Computer Vision
### Easy tier
- classification
    - ImageNet
- Age estimation
    - UTKFace
- Facial keypoint detection
    - AFLW (Annotated Facial Landmarks in the Wild)
### Mid tier
- Object detection
    - Vehicle Registration Plates Detection Dataset
    - ID Card Detection Dataset
- Semantic segmentation
    - Cityscapes
- Instance segmentation
    - COCO

### Advanced tier
- Liveness Detection (Anti-Spoofing)
- Face Verification
- Face Identification


## Audio
### Easy tier
- Audio/Sound Classification
    - UrbanSound8K
- Music Genre Classification
    - GTZAN
- Keyword Spotting
    - Google Speech Commands

### Mid-Advanced tier
- Sound Event Detection
    - DCASE
    - AudioSet
- Audio Source Separation
    - MUSDB18
    - LibriMix / WSJ0-2mix
- Speech Enhancement
    - Microsoft DNS Challenge
    - VCTK + DEMAND
- Automatic Speech Recognition
    - LibriSpeech
    - Common Voice (Mozilla)
- Speech Emotion Recognition
    - RAVDESS
    - IEMOCAP