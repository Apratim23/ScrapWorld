from flask import Flask, render_template, request, jsonify
from modules.scraper import WebScraper
from modules.llm_processor import LLMProcessor
from modules.search import WebSearch

app = Flask(__name__)

# Initialize modules
scraper = WebScraper()
llm = LLMProcessor()
search = WebSearch()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape_url():
    data = request.json
    url = data.get('url')
    scrape_method = data.get('method', 'bs4')  # Default to BeautifulSoup
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    try:
        # Scrape content based on the selected method
        if scrape_method == 'llamaindex':
            result = scraper.scrape_with_llamaindex(url)
        else:
            result = scraper.scrape_with_bs4(url)
        
        # Check if scraping was successful
        if not result.get('content'):
            return jsonify({"error": result.get('error', 'Failed to scrape content')}), 400
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/process', methods=['POST'])
def process_content():
    data = request.json
    content = data.get('content')
    processing_type = data.get('type', 'summarize')  # Default to summarize
    
    if not content:
        return jsonify({"error": "Content is required"}), 400
    
    try:
        # Process content based on the selected processing type
        if processing_type == 'keypoints':
            result = llm.extract_key_points(content)
        elif processing_type == 'sentiment':
            result = llm.analyze_sentiment(content)
        else:
            result = llm.summarize(content)
        
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search', methods=['POST'])
def search_topic():
    data = request.json
    topic = data.get('topic')
    
    if not topic:
        return jsonify({"error": "Topic is required"}), 400
    
    try:
        # Get URLs for the topic
        urls = search.get_urls_for_topic(topic)
        
        if not urls:
            return jsonify({"error": "No URLs found for the topic"}), 404
        
        return jsonify({"urls": urls})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/scrape-and-process', methods=['POST'])
def scrape_and_process():
    data = request.json
    url = data.get('url')
    topic = data.get('topic')
    processing_type = data.get('processingType', 'summarize')
    
    # Either URL or topic must be provided
    if not url and not topic:
        return jsonify({"error": "Either URL or topic is required"}), 400
    
    try:
        # If topic is provided but URL is not, search for URLs
        if topic and not url:
            urls = search.get_urls_for_topic(topic)
            if not urls:
                return jsonify({"error": f"No URLs found for topic: {topic}"}), 404
            url = urls[0]  # Use the first URL
        
        # Scrape the content
        result = scraper.scrape_with_bs4(url)
        
        if not result.get('content'):
            return jsonify({"error": result.get('error', 'Failed to scrape content')}), 400
        
        # Process the content based on the selected type
        if processing_type == 'keypoints':
            processed_result = llm.extract_key_points(result['content'])
        elif processing_type == 'sentiment':
            processed_result = llm.analyze_sentiment(result['content'])
        else:
            processed_result = llm.summarize(result['content'])
        
        return jsonify({
            "url": url,
            "title": result.get('title', 'No title'),
            "domain": result.get('domain', ''),
            "scraped_content": result['content'][:500] + "...",  # Preview of content
            "processed_result": processed_result
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
