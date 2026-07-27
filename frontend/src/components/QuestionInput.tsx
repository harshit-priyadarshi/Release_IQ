import { useState } from "react";

interface QuestionInputProps {
  onAsk: (question: string) => void;
}

function QuestionInput({ onAsk }: QuestionInputProps) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    if (!question.trim()) return;

    onAsk(question);

    setQuestion("");
  };

  return (
    <div className="flex gap-3">
      <input
        className="flex-1 rounded-lg border border-slate-600 bg-slate-800 px-4 py-3 text-white outline-none"
        value={question}
        placeholder="Ask ReleaseIQ..."
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSubmit();
          }
        }}
      />

      <button
        onClick={handleSubmit}
        className="rounded-lg bg-blue-600 px-6 py-3 text-white hover:bg-blue-700"
      >
        Ask
      </button>
    </div>
  );
}

export default QuestionInput;