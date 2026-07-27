interface MessageProps {
  role: "user" | "assistant";
  content: string;
}

function Message({ role, content }: MessageProps) {
  const isUser = role === "user";

  return (
    <div
      className={`flex ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`max-w-3xl rounded-xl px-4 py-3 shadow-md whitespace-pre-wrap ${
          isUser
            ? "bg-blue-600 text-white"
            : "bg-slate-700 text-white"
        }`}
      >
        {content}
      </div>
    </div>
  );
}

export default Message;