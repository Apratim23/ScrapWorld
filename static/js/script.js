document.addEventListener('DOMContentLoaded', function() {
    // Tab switching
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Deactivate all tabs
            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));
            
            // Activate selected tab
            btn.classList.add('active');
            const tabId = btn.getAttribute('data-tab');
            document.getElementById(tabId).classList.add('active');
        });
    });
    
    // Result tab switching
    const resultTabBtns = document.querySelectorAll('.result-tab-btn');
    const resultTabContents = document.querySelectorAll('.result-tab-content');
    
    resultTabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Deactivate all result tabs
            resultTabBtns.forEach(b => b.classList.remove('active'));
            resultTabContents.forEach(c => c.classList.remove('active'));
            
            // Activate selected result tab
            btn.classList.add('active');
            const tabId = btn.getAttribute('data-result-tab') + '-content';
            document.getElementById(tabId).classList.add('active');
        });
    });
    
    // Scrape URL button click handler
    document.getElementById('scrape-url-btn').addEventListener('click', () => {
        const url = document.getElementById('url-input').value.trim();
        if (!url) {
            alert('Please enter a URL to scrape');
            return;
        }
        
        const scrapeMethod = document.querySelector('input[name="scrape-method"]:checked').value;
        const processingType = document.querySelector('input[name="processing-type"]:checked').value;
        
        // Show loading state
        showLoading();
        
        // Make API call to scrape and process
        fetch('/scrape-and-process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                url: url,
                scrapeMethod: scrapeMethod,
                processingType: processingType
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            displayResults(data);
        })
        .catch(error => {
            hideLoading();
            alert('Error: ' + error.message);
        });
    });
    
    // Search topic button click handler
    document.getElementById('search-topic-btn').addEventListener('click', () => {
        const topic = document.getElementById('topic-input').value.trim();
        if (!topic) {
            alert('Please enter a topic to search');
            return;
        }
        
        const processingType = document.querySelector('input[name="processing-type"]:checked').value;
        
        // Show loading state
        showLoading();
        
        // Make API call to search, scrape and process
        fetch('/scrape-and-process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                topic: topic,
                processingType: processingType
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            displayResults(data);
        })
        .catch(error => {
            hideLoading();
            alert('Error: ' + error.message);
        });
    });
    
    // Function to display results
    function displayResults(data) {
        // Hide loading indicator
        hideLoading();
        
        // Display results container
        document.getElementById('results-container').style.display = 'block';
        
        // Fill in result data
        document.getElementById('result-title').textContent = data.title || 'No Title';
        const urlElement = document.querySelector('#result-url a');
        urlElement.textContent = data.url;
        urlElement.href = data.url;
        
        document.getElementById('processed-result').textContent = data.processed_result;
        document.getElementById('raw-result').textContent = data.scraped_content;
        
        // Show the results section
        document.getElementById('results').style.display = 'block';
        
        // Scroll to results
        document.getElementById('results-container').scrollIntoView({
            behavior: 'smooth'
        });
    }
    
    // Function to show loading state
    function showLoading() {
        document.getElementById('results-container').style.display = 'block';
        document.getElementById('loading').style.display = 'flex';
        document.getElementById('results').style.display = 'none';
    }
    
    // Function to hide loading state
    function hideLoading() {
        document.getElementById('loading').style.display = 'none';
    }
});
