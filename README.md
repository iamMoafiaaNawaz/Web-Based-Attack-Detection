# Web Attack Detection using Hybrid LSTM and Transformer Architecture

## 1. Abstract
This project presents the design and evaluation of a deep learning-based system for detecting malicious HTTP traffic[cite: 17]. The architecture integrates a Bidirectional Long Short-Term Memory (Bi-LSTM) network with a Transformer encoder to capture both sequential dependencies and global contextual patterns within HTTP requests[cite: 18]. Evaluated on the CSIC 2010 HTTP Dataset, the system achieves a 91% classification accuracy, demonstrating strong precision for attack detection (100%) and high recall for normal traffic identification (100%)[cite: 20].

## 2. Dataset Specification
The model was trained using the CSIC 2010 HTTP Dataset, which simulates realistic e-commerce traffic[cite: 39].

### 2.1 Dataset Composition
| Metric | Value |
| :--- | :--- |
| Total HTTP Requests | 123,042 [cite: 42] |
| Normal Requests (Label 0) | 88,000 (71.52%) [cite: 42] |
| Attack Requests (Label 1) | 35,042 (28.48%) [cite: 42] |

### 2.2 Attack Categories Covered
The dataset includes diverse malicious vectors[cite: 43]:
* **SQL Injection (SQLi)**: Manipulation of database queries via malicious input[cite: 44].
* **Cross-Site Scripting (XSS)**: Injection of client-side scripts[cite: 45].
* **Path Traversal**: Unauthorized access to restricted server directories[cite: 46].

## 3. Methodology and Architecture
The system employs a four-stage hybrid pipeline to extract discriminative features from raw traffic[cite: 65, 66].

### 3.1 Architecture Configuration
| Component | Specification |
| :--- | :--- |
| Embedding Dimension | 128 [cite: 78] |
| LSTM Hidden Units | 128 (Bidirectional -> 256 effective) [cite: 78] |
| Transformer Layers | 2 [cite: 78] |
| Attention Heads | 4 [cite: 78] |
| Max Sequence Length | 512 tokens [cite: 63] |

### 3.2 Technical Workflow
1. **Embedding Layer**: Maps integer tokens to 128-dimensional dense vectors[cite: 67].
2. **Bi-LSTM**: Captures bidirectional sequential structure within request tokens[cite: 69, 70].
3. **Transformer Encoder**: Relates non-local structural patterns via self-attention[cite: 71, 72].
4. **Classification Head**: Softmax output over binary classes (Normal vs. Attack)[cite: 77].

## 4. Performance Evaluation
The model was optimized using the Adam optimizer and CrossEntropy Loss over 10 training epochs[cite: 80].

### 4.1 Classification Results
Results recorded on 18,457 unseen test samples[cite: 93, 95]:

| Class | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- |
| Normal (Class 0) | 0.88 | 1.00 | 0.94 | 13,238 [cite: 93] |
| Attack (Class 1) | 1.00 | 0.67 | 0.80 | 5,219 [cite: 93] |
| **Overall Accuracy** | | | **0.91** | **18,457** [cite: 93] |

### 4.2 Key Findings
* **False Positive Mitigation**: Perfect recall (1.00) for normal traffic ensures legitimate users are not blocked[cite: 97, 98].
* **High Specificity**: Attack precision (1.00) indicates that all flagged requests were confirmed malicious[cite: 103].

## 5. Deployment and Installation
The project includes a live demonstration interface built with Streamlit for real-time inference[cite: 124, 126].

### 5.1 Installation
1. Clone the repository:
   `git clone https://github.com/iamMoafiaaNawaz/Web-Based-Attack-Detection.git`
2. Install dependencies:
   `pip install torch streamlit numpy scikit-learn`

### 5.2 Usage
Launch the interactive dashboard:
`streamlit run app.py`

---
