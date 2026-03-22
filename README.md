<div align="center">
  <img src="echoes-decoration.avif" width="200" alt="Echoes of Wisdom API">
</div>

# Echoes of Wisdom API

**A REST API serving data on all 127 echoes in *The Legend of Zelda: Echoes of Wisdom***

[![CI](https://github.com/lb930/EchoesOfWisdomAPI/actions/workflows/ci.yml/badge.svg)](https://github.com/lb930/EchoesOfWisdomAPI/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![Render](https://img.shields.io/badge/deployed%20on-Render-46E3B7?logo=render)](https://echoes-of-wisdom-api.onrender.com)

Built with [FastAPI](https://fastapi.tiangolo.com/) and deployed on [Render](https://render.com/).

**Base URL:** `https://echoes-of-wisdom-api.onrender.com`

---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/echoes/all/` | Return all echoes |
| GET | `/echoes/monsters/` | Return all monster echoes |
| GET | `/echoes/objects/` | Return all object echoes |
| GET | `/echoes/name/{name}` | Return a single echo by name |


---

## Usage
```bash
curl https://echoes-of-wisdom-api.onrender.com/echoes/name/Lynel
curl https://echoes-of-wisdom-api.onrender.com/echoes/monsters/
curl https://echoes-of-wisdom-api.onrender.com/echoes/objects/
curl https://echoes-of-wisdom-api.onrender.com/echoes/all/
```

---

## Example Response

```
GET /echoes/name/Lynel
```

```json
  {
    "name": "Lynel",
    "base_cost": 6,
    "description": "The most fearsome monster in all of Hyrule, this brute annihilates foes with mighty swings of its sword.",
    "image": "static/images/Lynel_-_EoW_icon.png",
    "health": 80,
    "attack_dmg": 10,
    "size": "2 x 2",
    "height": 4,
    "type": "monster"
  }
```

---

## Running Locally

```bash
git clone https://github.com/lb930/EchoesOfWisdomAPI.git
cd YOUR_REPO
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs at `http://127.0.0.1:8000/docs`.

---

*Data sourced from [ZeldaDungeon](https://www.zeldadungeon.net/wiki/Echo) and [ZeldaSpeedRuns](https://www.zeldaspeedruns.com/eow).*