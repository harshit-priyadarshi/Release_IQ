import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

interface MessageProps {
  role: "user" | "assistant";
  content: string;
}

function Message({ role, content }: MessageProps) {
  const isUser = role === "user";

  const [copied, setCopied] = useState(false);

  const copyToClipboard = async (text: string) => {
    try {
      await navigator.clipboard.writeText(text);

      setCopied(true);

      setTimeout(() => {
        setCopied(false);
      }, 2000);
    } catch (error) {
      console.error("Failed to copy:", error);
    }
  };

  return (
    <div
      className={`flex ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`max-w-3xl rounded-xl px-5 py-4 shadow-md ${
          isUser
            ? "bg-blue-600 text-white"
            : "bg-slate-700 text-white"
        }`}
      >
        <ReactMarkdown
          remarkPlugins={[remarkGfm]}
          components={{
            code(props) {
              const { children, className, ...rest } = props;

              const match = /language-(\w+)/.exec(className || "");

              const code = String(children).replace(/\n$/, "");

              if (match) {
                return (
                  <div className="relative">
                    <button
                      onClick={() => copyToClipboard(code)}
                      className="absolute right-3 top-3 rounded-md bg-slate-800 px-3 py-1 text-xs text-white transition hover:bg-slate-600"
                    >
                      {copied ? "✅ Copied" : "📋 Copy"}
                    </button>

                    <SyntaxHighlighter
                      language={match[1]}
                      style={oneDark}
                      PreTag="div"
                    >
                      {code}
                    </SyntaxHighlighter>
                  </div>
                );
              }

              return (
                <code
                  className="rounded bg-slate-800 px-1 py-0.5"
                  {...rest}
                >
                  {children}
                </code>
              );
            },
          }}
        >
          {content}
        </ReactMarkdown>
      </div>
    </div>
  );
}

export default Message;