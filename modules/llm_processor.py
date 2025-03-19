import requests

class LLMProcessor:
    def __init__(self, model="llama2"):
        """Initialize the LLM processor with the specified model"""
        self.model = model
        self.ollama_url = "http://localhost:11434/api"
        self._ensure_model_available()
    
    def _ensure_model_available(self):
        """Check if the model is available and pull it if needed"""
        try:
            # Check if Ollama is running
            response = requests.get(f"{self.ollama_url}/tags")
            
            # Check if our model is in the list
            models = response.json().get("models", [])
            model_exists = any(m["name"] == self.model for m in models)
            
            if not model_exists:
                print(f"Model {self.model} not found. Pulling from Ollama...")
                self._pull_model()
            
        except requests.RequestException:
            print("Ollama service not detected. Please ensure Ollama is installed and running.")
            print("Visit https://ollama.ai/ for installation instructions.")
    
    def _pull_model(self):
        """Pull the model from Ollama"""
        try:
            response = requests.post(
                f"{self.ollama_url}/pull", 
                json={"name": self.model}
            )
            
            if response.status_code == 200:
                print(f"Successfully pulled {self.model}")
            else:
                print(f"Failed to pull {self.model}: {response.text}")
        except Exception as e:
            print(f"Error pulling model: {str(e)}")
    
    def process_content(self, content, instruction):
        """Process content with the LLM based on the given instruction"""
        try:
            prompt = f"""
            {instruction}
            
            Content to process:
            {content[:10000]}  # Limiting to first 10K chars to avoid token limits
            """
            
            response = requests.post(
                f"{self.ollama_url}/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "No response generated")
            else:
                return f"Error: {response.status_code} - {response.text}"
            
        except Exception as e:
            return f"Error processing content: {str(e)}"
    
    def summarize(self, content):
        """Summarize the provided content"""
        instruction = "Please provide a concise summary of the following content:"
        return self.process_content(content, instruction)
    
    def extract_key_points(self, content):
        """Extract key points from the provided content"""
        instruction = "Please extract the main points and key information from the following content:"
        return self.process_content(content, instruction)
    
    def analyze_sentiment(self, content):
        """Analyze the sentiment of the provided content"""
        instruction = "Please analyze the sentiment of the following content. Is it positive, negative, or neutral? Explain your reasoning:"
        return self.process_content(content, instruction)
