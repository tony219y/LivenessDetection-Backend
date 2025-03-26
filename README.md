# FastAPI Liveness Detection API

This project is a FastAPI-based web service for running liveness detection models. It is designed to handle requests efficiently and supports deep learning inference using TensorFlow.

## Key Dependencies

The following Python packages are essential for model loading and inference:

- **FastAPI** - Web framework for building APIs
- **Uvicorn** - ASGI server for running FastAPI
- **TensorFlow** - Deep learning framework for loading `.keras` models
- **NumPy** - For numerical operations
- **OpenCV (headless)** - Image processing library
- **Pydantic** - Data validation and serialization

## Model Loading

The API loads a pre-trained `.keras` model and performs liveness detection based on input images. Ensure the model file is placed in the appropriate directory before running the server.
