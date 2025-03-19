# 🌟 ScrapWorld 🌟

## 📚 Overview

This project implements a minimalistic web scraper application integrated with Large Language Models (LLMs) for intelligent content processing 🤖. The application allows users to input URLs or topics, scrape relevant content, and process it using LLMs to generate summaries, extract key points, or analyze sentiment 📊.

## 📸 Preview

[Website](./preview/WhatsApp%20Image%202025-03-19%20at%2018.41.59_ecc543b2.jpg)


## 🎯 Features

- **Web Scraping**: Uses BeautifulSoup and LlamaIndex for efficient content extraction 📄
- **LLM Integration**: Integrates with Ollama for open-source LLM processing 💻
- **Topic Search**: Finds relevant web pages based on a given topic 🔍
- **Content Processing**:
  - **Summarization**: Generates concise summaries 📝
  - **Key Points Extraction**: Extracts main points and key information 📋
  - **Sentiment Analysis**: Analyzes the sentiment of the content 🤔
- **Clean Interface**: Minimalistic web interface for easy use 🌐
- **RESTful API**: Backend API for handling scraping tasks and queries 📈

## 🚀 Installation

### 📝 Prerequisites

- Python 3.8 or higher 🐍
- Ollama (for local LLM processing) 🤖

### 🛠️ Setup

1. **Clone the Repository**:
```bash
git clone https://github.com/Apratim23/ScrapWorld.git
cd web-scraper-llm
```

2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

3. **Ensure Ollama is Running**:
   - Install Ollama from [ollama.ai](https://ollama.ai/)
   - Start the Ollama service

## 🗂️ Project Structure

```
web_scraper_llm/
├── app.py                  # Flask application 🌐
├── static/                 # Static files 📁
│   ├── css/                 
│   │   └── style.css       # CSS styles 💅
│   ├── js/
│   │   └── script.js       # Frontend JavaScript 📈
│   └── favicon.ico         # Website favicon 📊
├── templates/
│   └── index.html          # Main HTML page 📄
├── modules/
│   ├── scraper.py          # Web scraping functionality 📊
│   ├── llm_processor.py    # LLM integration 🤖
│   └── search.py           # Web search functionality 🔍
└── requirements.txt        # Dependencies 📝
```

## 🎮 Usage

1. **Start the Flask Application**:
```bash
python app.py
```

2. **Open Your Web Browser**:
   Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

3. **Use the Application**:
   - **Scrape by URL**: Enter a URL to scrape and select the scraping method and processing type 📄
   - **Scrape by Topic**: Enter a topic to search for, which will find relevant URLs and scrape the content 🔍

## 📚 Implementation Details


### 📊 Web Scraping Methods

The application provides two primary methods for scraping web content:

1. **BeautifulSoup Scraping**: Uses the BeautifulSoup library to extract and clean text content from web pages 📄
2. **LlamaIndex Scraping**: Uses the LlamaIndex library's web reader to scrape content 📊

### 🤖 LLM Integration

The application integrates with Ollama, a local LLM server that runs models directly on your machine. The LLM processor provides several content processing capabilities:

1. **Summarization**: Generates concise summaries of scraped content 📝
2. **Key Point Extraction**: Extracts main points and key information 📋
3. **Sentiment Analysis**: Analyzes the sentiment of the content 🤔

## 🚨 Troubleshooting

### 🤔 Common Issues

1. **LlamaIndex Import Errors**: If you encounter import errors with LlamaIndex, ensure you have the correct version installed and are using the proper import structure 📝
   ```bash
   pip install llama-index-core llama-index-readers-web
   ```

2. **Ollama Connection Issues**: Ensure Ollama is properly installed and running 🤖
   ```bash
   curl http://localhost:11434/api/tags
   ```

3. **Web Scraping Blocked**: Some websites block web scraping. Consider adding delays between requests or using a different User-Agent 🚫

## 📈 Contributing

Contributions are welcome! Please feel free to submit a Pull Request 🎉.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Apratim23/ScrapWorld/tree/main?tab=MIT-1-ov-file) file for details 📝.

## 📚 Acknowledgments

- **BeautifulSoup**: For HTML parsing 📄
- **Flask**: For the web framework 🌐
- **Ollama**: For local LLM processing 🤖
- **LlamaIndex**: For advanced document processing 📊


## 👨‍💻 Developer

Developed by [@Apratim23](https://github.com/Apratim23) 🌟

[LinkedIn](https://www.linkedin.com/in/apratim-dutta-78b5ba216/)
[GitHub](https://github.com/Apratim23)
