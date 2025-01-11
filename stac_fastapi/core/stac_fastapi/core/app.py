app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with a specific domain, e.g., ["https://example.com"]
    allow_credentials=True,
    allow_methods=["*"],  # Or specify methods like ["GET", "POST", "OPTIONS"]
    allow_headers=["*"],  # Or specify headers like ["Authorization", "Content-Type"]
)