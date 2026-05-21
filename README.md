# LoanAssist AI - Intelligent Financial RAG Assistant

AI-powered RAG application built using AWS Bedrock, OpenSearch, Lambda, API Gateway, and S3 for intelligent loan policy and financial document Q&A.

---

# 🚀 Features

**Retrieval-Augmented Generation (RAG):** Context-aware, precise generation using state-of-the-art foundation models natively grounded by financial document context.

**Hybrid Vector Search:** Combines semantic vector embeddings and traditional keyword search using Amazon OpenSearch Serverless for highly precise text block retrieval.

**Granular Security Controls:** Integrated with **AWS Bedrock Guardrails** to filter PII, enforce compliance boundaries, and mitigate malicious out-of-scope prompt injections.

**Serverless Architecture:** Infinite scaling with zero idle server overhead using AWS Lambda, Amazon API Gateway, and Amazon S3.

**Dynamic Citations Pipeline:** Extracts precise S3 metadata mappings to render clickable document references with content previews directly in the chat layer.

**Semantic Search using OpenSearch**
**AWS Bedrock Integration**
**Loan Policy Q&A Assistant**

---

## 🏗️ Architecture

User → S3 Hosted UI → API Gateway → Lambda → Bedrock Knowledge Base → OpenSearch

---

User ──> CloudFront Dist ──> S3 Static UI (HTML/CSS/JS)

│

(CORS REST API)

│

▼

Amazon API Gateway

│

▼

AWS Lambda Function (Python)

│

▼

Amazon Bedrock Agent Runtime

│

┌─────────────┴─────────────┐

▼                           ▼

Bedrock Knowledge Base    AWS Bedrock Guardrails

│                   (Boundary Security)

▼

Amazon OpenSearch Serverless
(Vector DB — Embeddings)

▲

│

Amazon S3 Data Source
(Financial Manuals & PDFs)

---

## 🛠️ Enterprise Tech Stack

* **Core Engine:** Amazon Bedrock (Knowledge Bases for Amazon Bedrock)
* **Foundation Models:** Amazon Nova Pro / Anthropic Claude
* **Vector Database:** Amazon OpenSearch Serverless (AOSS)
* **Compute:** AWS Lambda (Python 3.12 with adaptive retry configurations)
* **API Ingress:** Amazon API Gateway (REST API with CORS preflight handshakes)
* **Storage & Hosting:** Amazon S3 & Amazon CloudFront
* **Observability:** AWS CloudWatch Logs

---

## 📌 Project Flow

Document Ingestion: Raw financial manuals and policy files are securely pushed to a private Amazon S3 staging bucket.

Embedding & Vector Storage: Bedrock Knowledge Base ingests the data chunks, processes them via a Titan text embedding model, and indexes the resulting vectors inside an OpenSearch Serverless collection.

API Dispatch: User questions from the custom web panel hit an API Gateway endpoint, triggering a secure Lambda backend transaction.

Context-Aware Inference: The serverless compute layer unpacks the request payload and calls the Bedrock retrieve_and_generate API using hybrid search parameters before outputting a fully structured Markdown response with absolute S3 citations.

---

## 🔥 Future Improvements

* [ ] **Voice-Based Assistant:** Integrating Amazon Polly and Amazon Transcribe for full real-time speech-to-text and text-to-speech loan inquiries.
* [ ] **Multilingual Support:** Expanding the RAG pipeline to support regional and international languages for broader accessibility.
* [ ] **Customer-Facing Expansion:** Enhancing UI/UX workflows to scale the internal tool into a secure, public-facing portal for retail loan applicants.
* [ ] **Advanced Analytics:** Ingesting business usage metadata pipelines into Amazon QuickSight dashboards.

---

## 👨‍💻 Author
Mansuri Musaddiq Khan
