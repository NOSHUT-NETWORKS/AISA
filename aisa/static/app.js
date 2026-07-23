const state = {
  sessionId: null,
  answered: 0,
};

const welcome = document.querySelector("#welcome");
const consultation = document.querySelector("#consultation");
const result = document.querySelector("#result");
const errorBox = document.querySelector("#error");
const questionText = document.querySelector("#question-text");
const options = document.querySelector("#options");
const progressLabel = document.querySelector("#progress-label");

async function request(path, options = {}) {
  const response = await fetch(path, {
    headers: {"Content-Type": "application/json"},
    ...options,
  });
  const body = await response.json();
  if (!response.ok) {
    throw new Error(body.error || "AISA request failed");
  }
  return body;
}

function showError(error) {
  errorBox.textContent = error.message;
  errorBox.classList.remove("hidden");
}

function clearError() {
  errorBox.classList.add("hidden");
}

async function startConsultation() {
  clearError();
  try {
    const data = await request("/api/sessions", {
      method: "POST",
      body: "{}",
    });
    state.sessionId = data.session_id;
    state.answered = 0;
    render(data);
  } catch (error) {
    showError(error);
  }
}

async function answer(questionId, value) {
  clearError();
  options.querySelectorAll("button").forEach((button) => {
    button.disabled = true;
  });
  try {
    const data = await request(
      `/api/sessions/${state.sessionId}/answers`,
      {
        method: "POST",
        body: JSON.stringify({question_id: questionId, value}),
      },
    );
    state.answered += 1;
    render(data);
  } catch (error) {
    showError(error);
    options.querySelectorAll("button").forEach((button) => {
      button.disabled = false;
    });
  }
}

async function restart() {
  clearError();
  if (!state.sessionId) {
    await startConsultation();
    return;
  }
  try {
    const data = await request(
      `/api/sessions/${state.sessionId}/restart`,
      {method: "POST", body: "{}"},
    );
    state.answered = 0;
    render(data);
  } catch (error) {
    showError(error);
  }
}

function render(data) {
  welcome.classList.add("hidden");
  if (data.status === "question") {
    result.classList.add("hidden");
    consultation.classList.remove("hidden");
    renderQuestion(data.question);
    return;
  }
  consultation.classList.add("hidden");
  result.classList.remove("hidden");
  renderResult(data);
}

function renderQuestion(question) {
  progressLabel.textContent = `Question ${state.answered + 1} / 4`;
  questionText.textContent = question.text;
  options.replaceChildren();
  question.options.forEach((option) => {
    const button = document.createElement("button");
    button.className = "option";
    button.textContent = option.label;
    button.addEventListener("click", () => {
      answer(question.question_id, option.value);
    });
    options.append(button);
  });
}

function renderResult(data) {
  const report = data.report;
  const known = data.status === "diagnosis";
  document.querySelector("#result-badge").textContent = known
    ? "Pattern matched"
    : "Knowledge Unknown";
  document.querySelector("#result-title").textContent = known
    ? report.title
    : "AKEに適合するPatternがまだありません";
  document.querySelector("#result-summary").textContent = known
    ? report.summary
    : report.reason;

  const recommendations = document.querySelector("#recommendations");
  recommendations.replaceChildren();
  if (known) {
    const labels = {
      cost: "費用優先型",
      time: "時間短縮優先型",
      ai: "AI活用優先型",
    };
    Object.entries(report.recommendations).forEach(([key, text]) => {
      const section = document.createElement("section");
      section.className = "recommendation";
      const heading = document.createElement("h3");
      heading.textContent = labels[key] || key;
      const paragraph = document.createElement("p");
      paragraph.textContent = text;
      section.append(heading, paragraph);
      recommendations.append(section);
    });
  } else {
    const route = document.createElement("p");
    route.textContent = `Unknown Route: ${report.unknown_route.join(" → ")}`;
    recommendations.append(route);
  }

  const firstAction = document.querySelector("#first-action");
  firstAction.textContent = known
    ? `最初の行動: ${report.first_action}`
    : "この相談は破棄せず、Engineering Analysisへ引き継ぎます。";
  document.querySelector("#context-output").textContent = JSON.stringify(
    data.context,
    null,
    2,
  );
}

document.querySelector("#start-button").addEventListener(
  "click",
  startConsultation,
);
document.querySelector("#restart-button").addEventListener("click", restart);
document.querySelector("#result-restart-button").addEventListener(
  "click",
  restart,
);
