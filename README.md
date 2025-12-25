# Zero Green API

A FastAPI-based WhatsApp notification service that integrates with [Zerobyte](https://github.com/nicotsx/zerobyte) and [Green API](https://green-api.com/en) to send messages through WhatsApp.

## Features

- **REST API**: FastAPI-based web service
- **WhatsApp Integration**: Send messages via Green API
- **Docker Support**: Fully containerized application
- **Health Monitoring**: Built-in health check endpoint
- **Lightweight**: Python 3.11-slim based Docker image

## Prerequisites

- Docker and Docker Compose
- Green API account with:
  - Instance ID
  - API Token

## Project Structure

```
zero-green/
├── app/
│   ├── app.py          # Application entry point
│   ├── server.py       # FastAPI server implementation
│   └── proxy.py        # Green API integration
├── Dockerfile          # Docker image definition
├── docker-compose.yaml # Docker Compose configuration
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Installation

### Using Docker Compose

1. Clone or download this project

2. Set your Green API credentials as environment variables or update the docker-compose.yaml:

```yaml
environment:
  - ID_INSTANCE=your_instance_id
  - TOKEN=your_api_token
  - PYTHONUNBUFFERED=1
```

3. Add your Docker image name to docker-compose.yaml:

```yaml
services:
  zero-green:
    image: your-registry/zero-green:latest
```

4. Start the service:

```bash
docker-compose up -d
```

### Manual Docker Build

1. Build the image:

```bash
docker build -t zero-green .
```

2. Run the container:

```bash
docker run -d \
  -p 80:80 \
  -e ID_INSTANCE=your_instance_id \
  -e TOKEN=your_api_token \
  --name zero-green \
  zero-green
```

## API Endpoints

### GET /

Health check endpoint.

**Response:**
```json
{
  "message": "Zero Green API is running"
}
```

### GET /health

Service health status.

**Response:**
```json
{
  "status": "healthy"
}
```

### POST /send?chatid={chat_id}

Send a WhatsApp message.

**Parameters:**
- `chatid` (query parameter): WhatsApp chat ID (e.g., "1234567890@c.us")

**Request Body:**
- Raw text message

**Example:**
```bash
curl -X POST "http://localhost:80/send?chatid=1234567890@c.us" \
  -H "Content-Type: text/plain" \
  -d "Hello from Zero Green API!"
```

**Response:**
```json
{
  "status": "success",
  "chatid": "1234567890@c.us",
  "message": "Hello from Zero Green API!",
  "result": {...}
}
```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ID_INSTANCE` | Green API Instance ID | Yes |
| `TOKEN` | Green API Token | Yes |
| `PYTHONUNBUFFERED` | Python output buffering | No (default: 1) |

### Port Configuration

The default port is **80**. You can change it in:
- `app/app.py`: Update the `port` parameter
- `Dockerfile`: Update the `EXPOSE` directive
- `docker-compose.yaml`: Update the port mapping

## Dependencies

- **fastapi**: Modern web framework
- **uvicorn**: ASGI server
- **requests**: HTTP library
- **whatsapp-chatbot-python**: Green API integration
- **loguru**: Logging library

## Development

### Local Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set environment variables:

```bash
export ID_INSTANCE=your_instance_id
export TOKEN=your_api_token
```

3. Run the application:

```bash
python app/app.py
```

The server will start on `http://0.0.0.0:80`

## Logging

The application uses Loguru for logging. Logs include:
- Successful message deliveries
- Error messages with stack traces
- Request/response information
