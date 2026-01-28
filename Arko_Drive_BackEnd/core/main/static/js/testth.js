// test.js

document.querySelectorAll('.question').forEach(question => {
  const inputs = question.querySelectorAll('input[type="radio"]');
  inputs.forEach(input => {
    input.addEventListener('change', () => {
      if (question.classList.contains('answered')) return;
      question.classList.add('answered');

      const selLabel = input.closest('label');
      const rightLabel = question.querySelector('label[data-correct="true"]');

      if (selLabel.dataset.correct === "true") {
        selLabel.classList.add('correct');
      } else {
        selLabel.classList.add('incorrect');
        if (rightLabel) rightLabel.classList.add('correct');
      }

      inputs.forEach(i => i.disabled = true);
    });
  });
});
