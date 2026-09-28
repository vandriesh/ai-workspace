// Multiple-choice quizzes with instant feedback.
//
// Markup:
//   <fieldset class="quiz" data-correct="1">          <!-- 0-based index of the right option -->
//     <legend>Question 1</legend>
//     <p>…the question…</p>
//     <div class="options"><button>a</button><button>b</button>…</div>
//     <div class="why" hidden>…explanation shown after answering…</div>
//   </fieldset>
//   <p class="quiz-tally"></p>                         <!-- optional running score -->
//
// The first answer counts: options lock after one click, so the tally reflects recall,
// not trial and error. "Try again" resets every quiz on the page for spaced review.

(() => {
  const quizzes = [...document.querySelectorAll(".quiz")];
  const tally = document.querySelector(".quiz-tally");

  function render() {
    if (!tally) return;
    const answered = quizzes.filter((q) => q.classList.contains("got-it") || q.classList.contains("missed"));
    const right = quizzes.filter((q) => q.classList.contains("got-it")).length;
    tally.textContent =
      answered.length < quizzes.length
        ? `${answered.length} of ${quizzes.length} answered.`
        : `${right} of ${quizzes.length} right on the first try.`;
    if (answered.length === quizzes.length) {
      const again = document.createElement("button");
      again.type = "button";
      again.textContent = "Try again";
      again.addEventListener("click", reset);
      tally.append(again);
    }
  }

  function reset() {
    for (const quiz of quizzes) {
      quiz.classList.remove("got-it", "missed");
      for (const button of quiz.querySelectorAll(".options button")) {
        button.disabled = false;
        button.classList.remove("correct", "wrong");
      }
      const why = quiz.querySelector(".why");
      if (why) why.hidden = true;
      quiz.querySelector(".verdict")?.remove();
    }
    render();
    quizzes[0]?.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  for (const quiz of quizzes) {
    const buttons = [...quiz.querySelectorAll(".options button")];
    const correct = Number(quiz.dataset.correct);
    buttons.forEach((button, index) => {
      button.type = "button";
      button.addEventListener("click", () => {
        const gotIt = index === correct;
        for (const b of buttons) b.disabled = true;
        buttons[correct].classList.add("correct");
        if (!gotIt) button.classList.add("wrong");
        quiz.classList.add(gotIt ? "got-it" : "missed");

        const verdict = document.createElement("p");
        verdict.className = "verdict";
        verdict.textContent = gotIt ? "Right." : "Not quite.";
        const why = quiz.querySelector(".why");
        if (why) {
          why.hidden = false;
          why.prepend(verdict);
        } else {
          quiz.append(verdict);
        }
        render();
      });
    });
  }

  render();
})();
