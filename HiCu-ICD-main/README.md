# HiCu-ICD
This repo contains code for our HiCu DLH 2023 paper [HiCu: Leveraging Hierarchy for Curriculum Learning in Automated ICD Coding](https://arxiv.org/abs/2208.02301).

Setup
-----
Install the following packages to run the code in this repository:
* gensim==4.3.0
* nltk==3.6.5
* numpy==1.23.5
* pandas==1.4.2
* scikit_learn==1.2.0
* scipy==1.10.0
* torch==1.13.1
* tqdm==4.62.3
* transformers==4.26.1
* geoopt==0.5.0

```bash
pip install -r requirements.txt
```

Data Preprocessing
-----
We use MIMIC-III for model training and evaluation. We use the same data preprocessing code as [MultiResCNN](https://github.com/wren93/HiCu-ICD). To set up the dataset, place the MIMIC-III files into `/data` as shown below:
```
data
|   D_ICD_DIAGNOSES.csv
|   D_ICD_PROCEDURES.csv
└───mimic3/
|   |   NOTEEVENTS.csv
|   |   DIAGNOSES_ICD.csv
|   |   PROCEDURES_ICD.csv
|   |   train_full_hadm_ids.csv
|   |   train_50_hadm_ids.csv
|   |   dev_full_hadm_ids.csv
|   |   dev_50_hadm_ids.csv
|   |   test_full_hadm_ids.csv
|   |   test_50_hadm_ids.csv
```
The `*_hadm_ids.csv` files can be found [here](https://github.com/jamesmullenbach/caml-mimic/tree/master/mimicdata/mimic3).

After setting up the files, run the following command to preprocess the data:
```sh
python preprocess_mimic3.py
```

Acknowledgement
-----
A large portion of the code in this repository is borrowed from https://github.com/wren93/HiCu-ICD. Thanks to their great work.
