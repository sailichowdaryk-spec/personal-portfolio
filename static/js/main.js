document.addEventListener("DOMContentLoaded", function () {
  const pauseBtn = document.getElementById("pause-btn");
  if (pauseBtn) {
    pauseBtn.addEventListener("click", function () {
      const paused = document.body.classList.toggle("anim-paused");
      pauseBtn.textContent = paused ? "▶ play animations" : "⏸ pause animations";
    });
  }

  document.querySelectorAll(".proj-card").forEach(function (card) {
    card.addEventListener("mousemove", function (e) {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = "rotate(" + (x * 4) + "deg) translateY(-4px)";
    });
    card.addEventListener("mouseleave", function () {
      card.style.transform = "";
    });
  });
});
