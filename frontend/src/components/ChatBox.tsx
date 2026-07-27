import Message from "./message";

interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

interface ChatBoxProps {
  messages: ChatMessage[];
}

function ChatBox({ messages }: ChatBoxProps) {
  return (
    <div className="flex flex-col gap-4">
      {messages.map((message, index) => (
        <Message
          key={index}
          role={message.role}
          content={message.content}
        />
      ))}
    </div>
  );
}

export default ChatBox;