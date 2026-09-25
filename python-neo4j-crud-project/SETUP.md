# Setup Guide

## 1. Open the project

```powershell
cd path\to\python-neo4j-crud-project
code .
```

## 2. Create virtual environment

```powershell
python -m venv venv
```

## 3. Activate

```powershell
.\venv\Scripts\Activate.ps1
```

## 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## 5. Configure Neo4j Aura

Copy `.env.example` to `.env`:

```powershell
Copy-Item .env.example .env
```

Edit `.env` with your real Aura credentials.

## 6. Run the complete CRUD demonstration

```powershell
python -m app.main
```

## 7. GitHub

```powershell
git init
git add .
git commit -m "Implement Python Neo4j CRUD operations"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/python-neo4j-crud-project.git
git push -u origin main
```

## 8. Expected result

```text
Neo4j connection successful!
All Neo4j operations completed successfully.
```
