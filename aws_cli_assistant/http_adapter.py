# src/http_adapter.py
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from core.nlp_utils import parse_nlp
from core.command_generator import generate_command, list_supported_services
from core.aws_validator import validate_command_safe
from core.telemetry import telemetry_log_event

app = FastAPI(title="MCP AWS CLI Adapter")

class GenerateRequest(BaseModel):
    query: str

@app.post("/generate")
async def generate(req: GenerateRequest):
    telemetry_log_event("http.request", {"path": "/generate", "query": req.query})
    intent, entities = parse_nlp(req.query)
    command, explanation = generate_command(intent, entities)
    validation = validate_command_safe(intent, entities)
    return {"command": command, "explanation": explanation, "validation": validation}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/services")
async def services():
    return {"services": list_supported_services()}

@app.get("/")
async def web_interface():
    """Simple HTML interface for testing"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS CLI Assistant - Web Interface</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
            .container { background: #f5f5f5; padding: 20px; border-radius: 8px; }
            input[type="text"] { width: 70%; padding: 10px; font-size: 16px; }
            button { padding: 10px 20px; font-size: 16px; background: #007cba; color: white; border: none; cursor: pointer; }
            .result { margin-top: 20px; padding: 15px; background: white; border-radius: 5px; }
            .command { font-family: monospace; background: #f0f0f0; padding: 10px; border-radius: 3px; }
        </style>
    </head>
    <body>
        <h1>🚀 AWS CLI Assistant - Web Interface</h1>
        <div class="container">
            <p>Enter your natural language request:</p>
            <input type="text" id="query" placeholder="e.g., list my s3 buckets" />
            <button onclick="generateCommand()">Generate Command</button>
            <div id="result" class="result" style="display:none;"></div>
        </div>
        
        <script>
            async function generateCommand() {
                const query = document.getElementById('query').value;
                if (!query) return;
                
                try {
                    const response = await fetch('/generate', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ query: query })
                    });
                    
                    const data = await response.json();
                    const resultDiv = document.getElementById('result');
                    
                    resultDiv.innerHTML = `
                        <h3>Generated Command:</h3>
                        <div class="command">${data.command}</div>
                        <p><strong>Explanation:</strong> ${data.explanation}</p>
                        <p><strong>Status:</strong> ${data.validation.status} - ${data.validation.reason}</p>
                    `;
                    resultDiv.style.display = 'block';
                } catch (error) {
                    alert('Error: ' + error.message);
                }
            }
            
            document.getElementById('query').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') generateCommand();
            });
        </script>
    </body>
    </html>
    """
    from fastapi.responses import HTMLResponse
    return HTMLResponse(content=html_content)

def run_http_app(app: FastAPI, host: str="127.0.0.1", port: int=8000):
    print(f"🌐 Web interface available at: http://{host}:{port}")
    print(f"📡 API endpoints: /generate, /health, /services")
    uvicorn.run(app, host=host, port=port)
