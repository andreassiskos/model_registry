import os
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_model_upload_and_retrieve():
    # Create a dummy model file
    model_path = "dummy_model.pkl"
    with open(model_path, "wb") as f:
        f.write(b"test model data")
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:

        # Upload the model
        with open(model_path, "rb") as file:
            response = await client.post(
                "/models",
                files={"file": ("dummy_model.pkl", file, "application/octet-stream")},
                data={"name": "TestModel", "version": "1.0", "accuracy": "0.99"},
            )
        assert response.status_code == 200

        # Check model metadata list
        response = await client.get("/models")
        assert response.status_code == 200
        models = response.json()
        assert any(m["name"] == "TestModel" for m in models)

        # Check specific model by name
        response = await client.get("/models/TestModel")
        assert response.status_code == 200
        assert response.json()["name"] == "TestModel"

    os.remove(model_path)
