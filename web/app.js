const summaryEl = document.getElementById("summary");
const summarizeButton = document.getElementById("summarizeButton");

summarizeButton.addEventListener("click", () => {
  const text = document.getElementById("textInput").value;
  const ratio = parseFloat(document.getElementById("ratioInput").value);
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
