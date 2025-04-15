const notifications = document.querySelector(".dyoxfy-notifications");


const toastDetails = {
  timer: 5000,
  success: {
    icon: "fa-circle-check",
    text: "Success: This is a success toast.",
  },
  error: {
    icon: "fa-circle-xmark",
    text: "Error: This is an error toast.",
  },
  warning: {
    icon: "fa-triangle-exclamation",
    text: "Warning: This is a warning toast.",
  },
  info: {
    icon: "fa-circle-info",
    text: "Info: This is an information toast.",
  },
};

const removeToast = (toast) => {
  toast.classList.add("hide");
  if (toast.timeoutId) clearTimeout(toast.timeoutId);
  setTimeout(() => toast.remove(), 500);
};

const dyoxfy = (type, message) => {
  const { icon } = toastDetails[type];
  const text = message;
  const toast = document.createElement("li");
  toast.className = `dyoxfy-toast ${type}`;

  toast.innerHTML = `<div class="column">
    <i class="fa-solid ${icon}"></i>
    <span>${text}</span>
    </div>
    <i class="ms-3 fa-solid fa-xmark" onclick="removeToast(this.parentElement)"></i>`;
  notifications.appendChild(toast);

  toast.timeoutId = setTimeout(() => removeToast(toast), toastDetails.timer);
};
