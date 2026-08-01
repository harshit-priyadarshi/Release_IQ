import ChatBox from "./components/ChatBox";
import QuestionInput from "./components/QuestionInput";
import { useChat } from "./hooks/useChat";

function App() {
  const {
    messages,
    loading,
    askQuestion,
  } = useChat();

return (
  <div className="h-screen bg-slate-900 text-white">
    <div className="mx-auto flex h-full max-w-5xl flex-col p-6">

      {/* Header */}
      <div className="mb-6">
        <h1 className="text-4xl font-bold">
          ReleaseIQ
        </h1>

        <p className="mt-2 text-slate-400">
          AI-Powered Release Documentation Assistant
        </p>
      </div>

      {/* Chat Area */}
      <div className="flex-1 overflow-y-auto rounded-xl border border-slate-700 bg-slate-800 p-6">
        <ChatBox
          messages={messages}
          onSuggestionClick={askQuestion}
        />
      </div>

      {/* Input */}
      <div className="mt-6">
        <QuestionInput
          onAsk={askQuestion}
          loading={loading}
        />
      </div>

    </div>
  </div>
);
}

export default App;