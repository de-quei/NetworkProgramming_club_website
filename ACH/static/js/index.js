// JavaScript 코드
window.addEventListener('DOMContentLoaded', function() {
    const slideWrapper = document.querySelector('.slide-wrapper');
    const slides = document.querySelectorAll('.slide-wrapper img');

    let counter = 0;
    const slideWidth = slides[0].clientWidth;

    setInterval(() => {
        counter++;
        slideWrapper.style.transition = 'transform 0.5s ease-in-out';
        slideWrapper.style.transform = `translateX(${-slideWidth * counter}px)`;

        if (counter === slides.length - 1) {
            setTimeout(() => {
                slideWrapper.style.transition = 'none';
                slideWrapper.style.transform = `translateX(0)`;
                counter = 0;
            }, 500);
        }
    }, 5000); // 이미지를 슬라이드할 시간 간격 (여기서는 2초)
});

document.querySelectorAll('nav ul li a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute('href'));

        window.scrollTo({
            top: target.offsetTop,
            behavior: 'smooth'
        });
    });
});