from fastapi import FastAPI
from pydantic import BaseModel
from khaiii import KhaiiiApi
from typing import Set


class MorphemeResponse(BaseModel):
    morphemes: Set[str]


class MorphemeRequest(BaseModel):
    content: str


app = FastAPI()
api = KhaiiiApi()


async def get_morphemes(content: str) -> Set[str]:
    words = api.analyze(content)
    results = set()
    for word in words:
        make = ''
        for m in word.morphs:
            if m.tag == 'NNP' or m.tag == 'NNG' or m.tag == 'NNB' or m.tag == 'XR':
                make += str(m).replace(f'/{m.tag}', '')
        if make == '':
            continue
        results.add(make)
    return results


@app.post("/poppers")
async def read_root(content_request: MorphemeRequest) -> MorphemeResponse:
    morphemes: Set[str] = await get_morphemes(content_request.content)
    return MorphemeResponse(morphemes=morphemes)
