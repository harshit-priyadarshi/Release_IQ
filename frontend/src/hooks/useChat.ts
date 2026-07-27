import { useState } from "react";
import { api } from "../api/api";
import type {
    AnswerResponse,
    QuestionRequest,
} from "../types/chat";

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export function useChat() {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      role: "assistant",
      content:
        "Hello! Ask me anything about your release documentation.",
    },
  ]);

  const [loading, setLoading] = useState(false);

  async function askQuestion(question: string) {
    const userMessage: ChatMessage = {
      role: "user",
      content: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      const body: QuestionRequest = {
        question,
      };

      const response =
        await api.post<AnswerResponse>(
          "/ask",
          body
        );

      const assistantMessage: ChatMessage = {
        role: "assistant",
        content: response.data.answer,
      };

      setMessages((prev) => [
        ...prev,
        assistantMessage,
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Something went wrong while contacting the server.",
        },
      ]);
    }

    setLoading(false);
  }

  return {
    messages,
    loading,
    askQuestion,
  };
}