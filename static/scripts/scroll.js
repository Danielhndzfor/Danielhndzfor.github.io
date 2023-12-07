const container = document.querySelector('.container');
const steps = document.querySelectorAll('.step');

function checkVisibility() {
    const containerPosition = container.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;

    if (containerPosition < windowHeight / 1.5) {
        container.classList.add('active');
    }

    steps.forEach((step, index) => {
        const stepPosition = step.getBoundingClientRect().top;
        if (stepPosition < windowHeight / 1.5) {
            step.classList.add('active');
        } else {
            step.classList.remove('active');
        }
    });
}

window.addEventListener('scroll', checkVisibility);
window.addEventListener('resize', checkVisibility);
window.addEventListener('load', checkVisibility);
