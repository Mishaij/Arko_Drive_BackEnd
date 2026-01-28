let slide_data = [
  {
    src: 'https://images.unsplash.com/photo-1506765336936-bb05e7e06295?auto=format&fit=crop&w=1050&q=80',
    title: 'Slide 1',
    copy: 'DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT.'
  },
  // … ещё объекты слайда
];

let slides = [], captions = [];
let autoplay = setInterval(nextSlide, 5000);
const container = document.getElementById('container');
const leftSlider = document.getElementById('left-col');
const downButton = document.getElementById('down_button');

downButton.addEventListener('click', e => {
  e.preventDefault();
  clearInterval(autoplay);
  nextSlide();
});

slide_data.forEach((data, i) => {
  const slide = document.createElement('div');
  slide.classList.add('slide');
  slide.style.background = `url(${data.src}) center/cover no-repeat`;

  const caption = document.createElement('div');
  caption.classList.add('caption');
  if (i === 0)      { slide.classList.add('current'); caption.classList.add('current-caption'); }
  else if (i === 1) { slide.classList.add('next');    caption.classList.add('next-caption'); }
  else if (i === slide_data.length - 1) {
                      slide.classList.add('previous');
                      caption.classList.add('previous-caption');
  }

  caption.innerHTML = `
    <div class="caption-heading"><h1>${data.title}</h1></div>
    <div class="caption-subhead"><span>${data.copy}</span></div>
    <a class="btn" href="#">Sit Amet</a>
  `;

  slides.push(slide);
  captions.push(caption);
  leftSlider.appendChild(slide);
  container.appendChild(caption);
});

function nextSlide() {
  slides[0].classList.replace('current', 'previous');
  slides[0].classList.add('change');
  slides[1].classList.replace('next', 'current');
  slides[2].classList.add('next');
  captions[0].classList.replace('current-caption', 'previous-caption');
  captions[0].classList.add('change');
  captions[1].classList.replace('next-caption', 'current-caption');
  captions[2].classList.add('next-caption');

  slides.push(slides.shift());
  captions.push(captions.shift());
}
