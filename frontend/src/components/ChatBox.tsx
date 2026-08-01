import { useEffect, useRef } from "react";
import Message from "./Message";

interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

interface ChatBoxProps {
  messages: ChatMessage[];
  onSuggestionClick: (question: string) => void;
}

function ChatBox({
  messages,
  onSuggestionClick,
}: ChatBoxProps) {

  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

return (
  <div className="flex flex-col gap-4">
    {messages.length === 0 ? (
      <div className="rounded-2xl border border-slate-700 bg-slate-800 p-8 text-center">
        <div className="mb-4 text-5xl">🤖</div>

        <h2 className="mb-2 text-2xl font-bold">
          Welcome to ReleaseIQ
        </h2>

        <p className="mb-6 text-slate-400">
          Ask questions about release notes, deployments,
          rollback procedures, Kubernetes, Helm, and internal documentation.
        </p>

        <div className="rounded-xl bg-slate-900 p-5 text-left">
          <p className="mb-3 font-semibold">
            Try asking:
          </p>

          <div className="flex flex-col gap-3">
            {[
              "How do I rollback the API deployment?",
              "What changed in Release 2.2?",
              "What are the deployment steps?",
              "Show me the rollback procedure.",
            ].map((question) => (
              <button
                key={question}
                onClick={() => onSuggestionClick(question)}
                className="rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-left text-slate-300 transition hover:border-blue-500 hover:bg-slate-700 hover:text-white"
              >
                💬 {question}
              </button>
            ))}
          </div>
        </div>
      </div>
    ) : (
      <>
        {messages.map((message, index) => (
          <Message
            key={index}
            role={message.role}
            content={message.content}
          />
        ))}

        <div ref={bottomRef} />
      </>
    )}
  </div>
);
}

export default ChatBox;