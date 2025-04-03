from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/.well-known/ai-plugin.json")
def plugin_manifest():
    return {
        "schema_version": "v1",
        "name_for_model": "personal_helper",
        "description_for_model": "Custom tools to help me with work and tasks.",
        "auth": {"type": "none"},
        "api": {"type": "openapi", "url": "http://localhost:3333/openapi.json"},
    }

@app.get("/openapi.json")
def openapi_spec():
    return app.openapi()

@app.get("/tool/hello")
def say_hello():
    return {"message": "Hey, Copilot. It's working."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3333)
