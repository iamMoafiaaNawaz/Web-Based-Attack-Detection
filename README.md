# Web Attack Detection using Hybrid LSTM + Transformer Architecture

## 1. Project Abstract
This research project focuses on the detection of malicious web-based traffic using deep learning. By combining **Bidirectional Long Short-Term Memory (Bi-LSTM)** networks with **Transformer Encoders**, the system effectively captures both sequential dependencies and global contextual patterns within HTTP requests. The model was trained on the CSIC 2010 dataset, achieving an overall classification accuracy of 91% with 100% precision for attack identification.

## 2. Dataset Specification
The model utilizes the **CSIC 2010 HTTP Dataset**, which simulates e-commerce traffic with both legitimate and malicious requests.

* **Total Samples:** 123,042 [cite: 42]
* **Normal Requests:** 88,000 (71.52%) [cite: 42]
* **Attack Requests:** 35,042 (28.48%) [cite: 42]
* **Attack Categories:** SQL Injection (SQLi), Cross-Site Scripting (XSS), and Path Traversal [cite: 19, 43]

## 3. Methodology & System Architecture
The pipeline is designed to process raw HTTP traffic into discriminative representations.

### 3.1 Preprocessing & Embedding
* **Tokenization:** Sub-word level custom vocabulary construction[cite: 60].
* **Sequence Length:** Fixed at 512 tokens[cite: 61, 63].
* **Vocabulary Size:** 82 unique tokens[cite: 62, 63].
* **Embedding Dim:** 128-dimensional dense vectors[cite: 63, 67].

### 3.2 Model Components
* **Bi-LSTM Layer:** Utilizes 128 hidden units per direction (256 total) to model bidirectional token dependencies[cite: 69, 70, 78].
* **Transformer Encoder:** A stacked encoder with 2 layers and 4 attention heads for global feature extraction through self-attention[cite: 71, 78].
* **Classification Head:** Fully connected layer with a softmax output for binary classification[cite: 77, 78].

## 4. Experimental Results
The system was optimized using the Adam optimizer and CrossEntropy loss over 10 epochs on a CUDA-enabled GPU[cite: 78, 80, 81].

### 4.1 Performance Metrics
The following results were recorded on the unseen test set of 18,457 samples:

| Class | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- |
| **Normal (0)** | 0.88 | 1.00 | 0.94 | 13,238 |
| **Attack (1)** | 1.00 | 0.67 | 0.80 | 5,219 |
| **Weighted Avg** | 0.92 | 0.91 | 0.90 | 18,457 |

[cite: 93]

### 4.2 Key Findings
* **Zero False Positive Rate:** The model achieved perfect recall (1.00) for normal traffic, ensuring no legitimate user requests are blocked[cite: 97, 140].
* **High-Precision Attacks:** Attack precision reached 1.00, meaning every flagged attack was confirmed malicious[cite: 103, 140].

## 5. System Setup and Execution
The project is modularized into seven distinct stages, from dataset collection to live deployment via a Streamlit interface[cite: 116, 121, 124].

### 5.1 Local Deployment
1. **Clone the Repository:**
   `git clone https://github.com/iamMoafiaaNawaz/Web-Based-Attack-Detection.git`
2. **Install Requirements:**
   `pip install torch streamlit numpy scikit-learn`
3. **Launch Interface:**
   `streamlit run app.py`

---
**Allah Moafi (22F-3181)** **Department of Computer Science** **FAST National University of Computer and Emerging Sciences** [cite: 2, 7, 9, 10]
