import { useEffect, useState } from "react";
import "./App.css";

interface Messages {
  role: "user" | "assistant";
  content: string;
  messageId?: string;
}

const API_URL = "http://localhost:8000";

function App() {
  const [openRequest, setOpenRequest] = useState<string>();
  const [message, setMessage] = useState<string>("");

  const [messages, setMessages] = useState<Messages[]>([
    { role: "assistant", content: "How can I help you?" },
  ]);

  const [status, setStatus] = useState("idle");

  useEffect(() => {
    if (!openRequest) return;

    const sse = new EventSource(`${API_URL}/message/${openRequest}`, {
      withCredentials: true,
    });

    function getMessageStream(data: any) {
      console.log(data);
      if (data === null) return;
      if (data.payload?.status) {
        setStatus(data.payload?.status);
      }
      if (data.payload?.message) {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            content: data.payload.message,
            messageId: data.messageId,
          },
        ]);
        setOpenRequest(undefined);
      }
    }

    sse.onmessage = (e) => getMessageStream(JSON.parse(e.data));

    sse.onerror = () => {
      setOpenRequest(undefined);
      sse.close();
    };

    return () => {
      setOpenRequest(undefined);
      sse.close();
    };
  }, [openRequest]);

  const sendMessage = async (content: string) => {
    try {
      setMessages((prev) => [...prev, { role: "user", content }]);

      const response = await fetch(`${API_URL}/message`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          url: "https://docs.hatchet.run/home",
          messages: [
            ...messages,
            {
              role: "user",
              content,
            },
          ],
        }),
      });

      if (response.ok) {
        // Handle successful response
        setOpenRequest((await response.json()).messageId);
      } else {
        // Handle error response
      }
    } catch (error) {
      // Handle network error
    }
  };

  return (
    <div className="App">
      <div className="Messages">
        {messages.map(({ role, content, messageId }, i) => (
          <p key={i}>
            <b>{role === "assistant" ? "Agent" : "You"}</b>: {content}
            {messageId && (
              <a
                target="_blank"
                rel="noreferrer"
                href={`http://localhost:8080/workflow-runs/${messageId}?tenant=707d0855-80ab-4e1f-a156-f1c4546cbf52`}
              >
                🪓
              </a>
            )}
          </p>
        ))}

        {openRequest && (
          <a
            target="_blank"
            rel="noreferrer"
            href={`http://localhost:8080/workflow-runs/${openRequest}?tenant=707d0855-80ab-4e1f-a156-f1c4546cbf52`}
          >
            {status}
          </a>
        )}
      </div>

      <div className="Input">
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        ></textarea>
        <button onClick={() => sendMessage(message)}>Ask</button>
      </div>
    </div>
  );
}

export default App;
