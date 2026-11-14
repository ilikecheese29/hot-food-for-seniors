(function () {
  "use strict";

  var cfg = window.WARMBOWL_CONFIG || {};

  // Mobile menu
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      toggle.textContent = open ? "Menu" : "Close";
      nav.classList.toggle("is-open", !open);
    });
  }

  // Footer year
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Deposit link
  document.querySelectorAll("[data-deposit]").forEach(function (block) {
    var link = block.querySelector("a");
    if (cfg.depositLink && link) {
      link.href = cfg.depositLink;
      block.hidden = false;
    } else {
      block.hidden = true;
    }
  });

  // Forms
  var email = cfg.contactEmail || "warmbowlmeals@gmail.com";

  function showStatus(form, message) {
    var status = form.querySelector(".form-status");
    if (!status) return;
    status.textContent = message;
    status.className = "form-status is-error";
    status.hidden = false;
  }

  document.querySelectorAll("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();

      var trap = form.querySelector('input[name="_gotcha"]');
      if (trap && trap.value) return;

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      var key = form.getAttribute("data-form");
      var endpoint = (cfg.forms || {})[key] || form.getAttribute("action");
      // data-lang: "zh" = Chinese only, "both" = English and Chinese, otherwise English.
      var lang = form.getAttribute("data-lang") || "en";
      function msg(en, zh) {
        if (lang === "zh") return zh;
        if (lang === "both") return en + " " + zh;
        return en;
      }

      if (!endpoint) {
        showStatus(
          form,
          msg(
            "This form isn't connected yet. Please email " + email + " and we'll get back to you.",
            "表格尚未连接。请发邮件至 " + email + "，我们会尽快回复。"
          )
        );
        return;
      }

      var button = form.querySelector('button[type="submit"]');
      var label = button ? button.innerHTML : "";
      if (button) {
        button.disabled = true;
        button.textContent = msg("Sending", "正在提交");
      }

      fetch(endpoint, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" }
      })
        .then(function (res) {
          if (!res.ok) throw new Error("Bad response");
          var success = document.querySelector('[data-success-for="' + key + '"]');
          form.hidden = true;
          if (success) {
            success.hidden = false;
            success.setAttribute("tabindex", "-1");
            success.focus();
            success.scrollIntoView({ behavior: "smooth", block: "start" });
          }
        })
        .catch(function () {
          showStatus(
            form,
            msg(
              "Something went wrong sending the form. Please try again, or email " + email + ".",
              "提交失败。请稍后再试，或发邮件至 " + email + "。"
            )
          );
        })
        .finally(function () {
          if (button) {
            button.disabled = false;
            button.innerHTML = label;
          }
        });
    });
  });
})();
