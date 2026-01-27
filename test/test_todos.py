from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import status
from fastapi.testclient import TestClient

from ToDoApp.database import Base
from ToDoApp.main import app
from ToDoApp.routers.admin import get_db, get_current_user

# Use a separate test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency overrides
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {
        "username": "lucky",
        "id": 1,
        "user_role": "admin",
    }


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)


def test_read_all_authenticated():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []
