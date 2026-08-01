import { useEffect, useRef, useState } from "react";

interface QuestionInputProps {
  onAsk: (question: string) => void;
  loading: boolean;
}

function QuestionInput({ onAsk, loading }: QuestionInputProps) {
  const [question, setQuestion] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleSubmit = () => {
    if (!question.trim() || loading) return;

    onAsk(question.trim());
    setQuestion("");
  };

  useEffect(() => {
    const textarea = textareaRef.current;

    if (!textarea) return;

    textarea.style.height = "auto";
    textarea.style.height = `${textarea.scrollHeight}px`;
  }, [question]);

  return (
    <div className="flex gap-3 items-end">
      <textarea
        ref={textareaRef}
        rows={1}
        disabled={loading}
        value={question}
        placeholder="Ask ReleaseIQ anything about your documentation..."
        className="flex-1 resize-none rounded-lg border border-slate-600 bg-slate-800 px-4 py-3 text-white outline-none disabled:opacity-60"
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSubmit();
          }
        }}
      />

      <button
        disabled={loading}
        onClick={handleSubmit}
        className="rounded-lg bg-blue-600 px-6 py-3 text-white hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading ? "Thinking..." : "Ask"}
      </button>
    </div>
  );
}

export default QuestionInput;