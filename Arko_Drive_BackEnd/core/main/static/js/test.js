/************  Таймер 30 минут  ************/
const TOTAL_SECONDS = 30 * 60;
let secondsLeft     = TOTAL_SECONDS;

const timerEl = document.getElementById('timer');
const form    = document.getElementById('test-form');
const summary = document.getElementById('results-summary');

function format(t){
  const m = String(Math.floor(t / 60)).padStart(2, '0');
  const s = String(t % 60).padStart(2, '0');
  return `${m}:${s}`;
}

function tick(){
  secondsLeft--;
  timerEl.textContent = format(secondsLeft);
  if (secondsLeft <= 300) timerEl.classList.add('red');
  if (secondsLeft <= 0) {
    clearInterval(interval);
    finalizeTest(true);  // timeExpired = true
  }
}

timerEl.textContent = format(secondsLeft);
const interval = setInterval(tick, 1000);

/************  Обработка отправки формы  ************/
form.addEventListener('submit', e => {
  e.preventDefault();
  // Проверяем, что все вопросы отвечены
  const unanswered = [...document.querySelectorAll('.question')]
                     .filter(q => !q.querySelector('input:checked'));

  if (unanswered.length) {
    alert('Խնդրում ենք պատասխանել բոլոր հարցերին, նախքան թեստը ավարտելը։');
    unanswered[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
    unanswered.forEach(q => q.classList.add('unanswered'));
    return; // не завершаем
  }

  finalizeTest(false);
});

/************  Подсчёт правильных/неправильных и вывод  ************/
function finalizeTest(timeExpired) {
  // После завершения теста — прокручиваем страницу в начало
  window.scrollTo({ top: 0, behavior: 'smooth' });

  clearInterval(interval);

  // Блокируем все варианты ответов
  form.classList.add('disabled');
  const btn = form.querySelector('.submit-btn');
  btn.disabled = true;
  btn.textContent = timeExpired ? 'Ժամանակը լրացավ' : 'Արդյունքներ';

  // Очищаем предыдущий контент, если был
  summary.innerHTML = '';

  // Показываем блок результатов (убираем класс "hidden")
  summary.classList.remove('hidden');

  // Заголовок
  const header = document.createElement('h2');
  header.textContent = 'Արդյունքների ամփոփում';
  summary.appendChild(header);

  // Считаем правильные/неправильные
  let correctCount = 0;
  let incorrectCount = 0;

  document.querySelectorAll('.question').forEach(q => {
    const chosen = q.querySelector('input:checked');
    const correctLabel = q.querySelector('label[data-correct]');
    const chosenLabel = chosen ? chosen.parentElement : null;

    // Если пользователь выбрал ответ и он совпадает с data-correct
    if (chosen && chosenLabel === correctLabel) {
      correctCount++;
    } else {
      // Либо не ответил (timeExpired), либо ответил неправильно
      incorrectCount++;
    }
    
    // Дополнительно помечаем правильный/неправильный визуально
    if (chosenLabel === correctLabel) {
      markLabel(correctLabel, true);
    } else {
      if (chosenLabel) {
        markLabel(chosenLabel, false);
      }
      markLabel(correctLabel, true);
    }
  });

  // Выводим строки с количеством
  const correctLine = document.createElement('div');
  correctLine.classList.add('summary-count1', 'correct');
  correctLine.textContent = `Ճիշտ: ${correctCount}`;
  summary.appendChild(correctLine);

  const incorrectLine = document.createElement('div');
  incorrectLine.classList.add('summary-count', 'incorrect');
  incorrectLine.textContent = `Սխալ: ${incorrectCount}`;
  summary.appendChild(incorrectLine);
}

/************  Функция для визуальной пометки label  ************/
function markLabel(label, isRight) {
  label.classList.add(isRight ? 'correct' : 'incorrect');
  if (!label.querySelector('.result-icon')) {
    const span = document.createElement('span');
    span.className = 'result-icon';
    span.textContent = isRight ? '✅' : '❌';
    label.append(span);
  }
}
