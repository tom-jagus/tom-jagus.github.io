(() => {
  const root = document.documentElement;
  const header = document.querySelector(".site-header");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const isHome = document.body.dataset.page === "home";
  let frame = 0;

  const cursorToggle = document.getElementById("cursor-toggle");
  if (cursorToggle) {
    function updateCursorAvailability() {
      cursorToggle.hidden = reducedMotion.matches;
      root.classList.toggle("cursor-ready", !reducedMotion.matches);
    }
    cursorToggle.addEventListener("click", () => {
      const paused = root.classList.toggle("cursor-paused");
      cursorToggle.setAttribute("aria-pressed", String(paused));
    });
    reducedMotion.addEventListener("change", updateCursorAvailability);
    updateCursorAvailability();
  }

  const contents = document.querySelector("details.contents");
  if (contents) {
    const wideReading = window.matchMedia("(min-width: 75rem)");
    const updateContents = () => { contents.open = wideReading.matches; };
    wideReading.addEventListener("change", updateContents);
    updateContents();
  }

  function updateScrollEffects() {
    frame = 0;
    const scroll = Math.max(0, window.scrollY);
    const progress = Math.min(1, scroll / 300);
    const headerProgress = reducedMotion.matches ? Number(scroll > 0) : Math.min(1, scroll / 120);
    root.style.setProperty("--header-progress", String(headerProgress));
    root.style.setProperty("--background-progress", String(isHome && !reducedMotion.matches ? progress : 1));
  }

  function scheduleScrollEffects() {
    if (!frame) frame = window.requestAnimationFrame(updateScrollEffects);
  }

  function measureHeader() {
    root.style.setProperty("--header-height", `${header.getBoundingClientRect().height}px`);
  }

  root.classList.add("scroll-ready");
  updateScrollEffects();
  measureHeader();
  window.addEventListener("scroll", scheduleScrollEffects, { passive: true });
  window.addEventListener("pageshow", updateScrollEffects);
  reducedMotion.addEventListener("change", updateScrollEffects);
  if (typeof ResizeObserver === "function") new ResizeObserver(measureHeader).observe(header);
  else window.addEventListener("resize", measureHeader);

  const menu = document.getElementById("mobile-menu");
  const trigger = document.querySelector(".menu-toggle");
  if (!menu || !trigger || typeof menu.showModal !== "function") return;

  const mobileWidth = window.matchMedia("(max-width: 850px)");
  const closeButton = menu.querySelector(".menu-close");
  let focusAfterClose = trigger;
  root.classList.add("menu-ready");

  function closeMenu(focusTarget = trigger) {
    focusAfterClose = focusTarget;
    document.body.classList.remove("menu-open");
    trigger.setAttribute("aria-expanded", "false");
    menu.close();
  }

  trigger.addEventListener("click", () => {
    if (menu.open) return;
    focusAfterClose = trigger;
    menu.showModal();
    document.body.classList.add("menu-open");
    trigger.setAttribute("aria-expanded", "true");
    closeButton.focus();
  });

  closeButton.addEventListener("click", () => closeMenu());
  menu.addEventListener("cancel", event => {
    event.preventDefault();
    closeMenu();
  });
  menu.addEventListener("close", () => {
    document.body.classList.remove("menu-open");
    trigger.setAttribute("aria-expanded", "false");
    focusAfterClose.focus({ preventScroll: true });
  });

  menu.addEventListener("keydown", event => {
    if (event.key !== "Tab") return;
    const items = [...menu.querySelectorAll("button, a[href]")];
    const first = items[0];
    const last = items[items.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });

  menu.addEventListener("click", event => {
    const link = event.target.closest("a[href]");
    if (!link) return;
    const destination = new URL(link.href);
    const samePage = destination.origin === location.origin && destination.pathname === location.pathname && destination.search === location.search;
    const target = samePage && destination.hash ? document.getElementById(decodeURIComponent(destination.hash.slice(1))) : null;
    if (target) {
      event.preventDefault();
      if (!target.hasAttribute("tabindex")) target.setAttribute("tabindex", "-1");
      closeMenu(target);
      history.pushState(null, "", destination.hash);
      target.scrollIntoView({ block: "start" });
    } else {
      closeMenu();
    }
  });

  mobileWidth.addEventListener("change", event => {
    if (!event.matches && menu.open) closeMenu(document.querySelector(".home-link"));
  });
})();
