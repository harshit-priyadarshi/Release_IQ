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
    <div className="min-h-screen bg-slate-900 text-white">
      <div className="mx-auto flex max-w-5xl flex-col gap-8 p-8">

        <h1 className="text-4xl font-bold">
          ReleaseIQ
        </h1>

        <p className="text-slate-400">
          AI-Powered Release Documentation Assistant
        </p>

        <ChatBox messages={messages} />

        {loading && (
          <p className="text-slate-400">
            Thinking...
          </p>
        )}

        <QuestionInput
          onAsk={askQuestion}
        />

      </div>
    </div>
  );
}

export default App;