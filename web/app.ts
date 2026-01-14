const summaryEl = document.getElementById("summary") as HTMLParagraphElement;
const summarizeButton = document.getElementById("summarizeButton") as HTMLButtonElement;

summarizeButton.addEventListener("click", () => {
  const text = (document.getElementById("textInput") as HTMLTextAreaElement).value;
  const ratio = parseFloat((document.getElementById("ratioInput") as HTMLInputElement).value);
  fetch("/api/summarize", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text, ratio }),
  })
    .then((res) => res.json())
    .then((data) => {
      summaryEl.textContent = data.summary || "";
    });
});
