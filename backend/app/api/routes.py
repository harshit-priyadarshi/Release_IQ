from fastapi import APIRouter

from app.llm.rag_service import RAGService
from app.schemas.chat import (
    QuestionRequest,
    AnswerResponse,
)

router = APIRouter()

rag = RAGService()


@router.get("/")
def root():
    return {
        "message": "ReleaseIQ API is running!"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/ask", response_model=AnswerResponse)
def ask(request: QuestionRequest):

    answer = rag.ask(request.question)

    return AnswerResponse(answer=answer)