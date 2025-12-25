from fastapi import FastAPI, Request
import uvicorn
from typing import Optional
from proxy import Proxy

class Server:
    def __init__(self, host: str = "0.0.0.0", port: int = 80):
        """
        Initialize the FastAPI server.
        
        Args:
            host: Host address to bind to
            port: Port number to listen on
            debug: Enable debug mode
        """
        self.host = host
        self.port = port
        self.app = FastAPI(title="Zero Green API", version="1.0.0")
        self.proxy = Proxy()
        
        # Register routes
        self._register_routes()
    
    def _register_routes(self):
        """Register API routes."""
        
        @self.app.get("/")
        async def root():
            return {"message": "Zero Green API is running"}
        
        @self.app.get("/health")
        async def health():
            return {"status": "healthy"}
        
        @self.app.post("/send")
        async def send_message(chatid: str, request: Request):
            """
            Send message endpoint.
            
            Args:
                chatid: Chat ID as URL parameter
                request: Request object to get raw body
            """
            body = await request.body()
            text = body.decode('utf-8')
            
            # Process the message using proxy
            result = self.proxy.send_notification(chatid, text)
            
            return {"status": "success", "chatid": chatid, "message": text, "result": result}
    
    def run(self):
        """Start the FastAPI server."""
        uvicorn.run(
            self.app,
            host=self.host,
            port=self.port
        )


if __name__ == "__main__":
    server = Server(debug=True)
    server.run()
